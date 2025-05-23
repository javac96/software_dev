"""
Robiul Hasan
May 13, 2025 Project 2
"""
#import Flask
from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
import uuid


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Takia0928@localhost/bookstore'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '7895' 

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Models
class UserDetails(db.Model, UserMixin):
    __tablename__ = 'user_details'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    phn_num = db.Column(db.String(20))
    carts = db.relationship('Cart', backref='user', lazy=True)
    orders = db.relationship('Order', backref='user', lazy=True)
    #payment_methods = db.relationship('PaymentMethod', backref='user', lazy=True)

    def set_password(self, password):
        self.password = password

    def get_id(self):
        return str(self.user_id)

class Book(db.Model):
    __tablename__ = 'books'
    book_id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    description = db.Column(db.Text)
    stock_quantity = db.Column(db.Integer, default=0, nullable=False)
    image_path = db.Column(db.String(255), nullable=False)
    carts = db.relationship('Cart', backref='book', lazy=True)
    order_items = db.relationship('OrderItem', backref='book', lazy=True)

class PaymentMethod(db.Model):
    __tablename__ = 'pmt_mthd'
    pmt_mthd_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_details.user_id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Order(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_details.user_id'), nullable=False)
    order_dt = db.Column(db.DateTime, default=datetime.utcnow)
    ttl_amt = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pending')
    shipping_address = db.Column(db.Text, nullable=False)
    pmt_mthd_id = db.Column(db.Integer, db.ForeignKey('pmt_mthd.pmt_mthd_id'))
    items = db.relationship('OrderItem', backref='order', lazy=True)
    pmt_mthd_id = db.Column(db.Integer, db.ForeignKey('pmt_mthd.pmt_mthd_id'), nullable=True)
    payment_method = db.relationship('PaymentMethod', backref='orders')  # This was missing
    items = db.relationship('OrderItem', backref='order', lazy=True, cascade='all, delete-orphan')

class OrderItem(db.Model):
    __tablename__ = 'order_items'
    order_item_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price_at_purchase = db.Column(db.Numeric(10, 2), nullable=False)

class Cart(db.Model):
    __tablename__ = 'cart'
    cart_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_details.user_id'))
    session_id = db.Column(db.String(100))
    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'), nullable=False)
    quantity = db.Column(db.Integer, default=1, nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return UserDetails.query.get(int(user_id))

# Helper functions
def get_session_id():
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())
    return session['session_id']

def get_cart_count():
    if current_user.is_authenticated:
        return Cart.query.filter_by(user_id=current_user.user_id).count()
    else:
        return Cart.query.filter_by(session_id=get_session_id(), user_id=None).count()

def get_cart_items():
    if current_user.is_authenticated:
        return Cart.query.filter_by(user_id=current_user.user_id).all()
    else:
        return Cart.query.filter_by(session_id=get_session_id(), user_id=None).all()

def get_cart_total():
    items = get_cart_items()
    return sum(float(item.book.price) * item.quantity for item in items)

def transfer_guest_cart_to_user(user_id):
    session_id = get_session_id()
    guest_items = Cart.query.filter_by(session_id=session_id, user_id=None).all()
    for item in guest_items:
        existing = Cart.query.filter_by(user_id=user_id, book_id=item.book_id).first()
        if existing:
            existing.quantity += item.quantity
            db.session.delete(item)
        else:
            item.user_id = user_id
            item.session_id = None

    db.session.commit()

# Routes
@app.route('/')
def home():
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if password != confirm_password:
            flash('Passwords do not match', 'danger')
            return redirect(url_for('register'))
        
        if UserDetails.query.filter_by(username=username).first():
            flash('Username already taken', 'danger')
            return redirect(url_for('register'))
        
        if UserDetails.query.filter_by(email=email).first():
            flash('Email already registered', 'danger')
            return redirect(url_for('register'))
        
        user = UserDetails(
            username=username,
            email=email,
            first_name=request.form.get('first_name'),
            last_name=request.form.get('last_name'),
            phn_num=request.form.get('phone_number')
        )
        user.set_password(password)
        
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    # Get the 'next' parameter from either GET or POST request
    next_page = request.args.get('next') or request.form.get('next')
    is_checkout = next_page and 'cart' in next_page
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = UserDetails.query.filter_by(username=username).first()
        
        if user and user.password:
            login_user(user)
            transfer_guest_cart_to_user(user.user_id)
            flash(f'Welcome back, {user.first_name or user.username}!', 'success')
            
            # Redirect logic
            if is_checkout:
                return redirect(url_for('view_cart'))
            elif next_page and url_parse(next_page).netloc == '':
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html', next=request.args.get('next'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('home'))

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    book_id = request.form.get('book_id', type=int)
    if not book_id:
        flash('Invalid book', 'danger')
        return redirect(url_for('home'))
    
    book = Book.query.get_or_404(book_id)
    
    if book.stock_quantity <= 0:
        flash('This book is out of stock', 'warning')
        return redirect(url_for('home'))
    
    if current_user.is_authenticated:
        cart_item = Cart.query.filter_by(user_id=current_user.user_id, book_id=book_id).first()
    else:
        session_id = get_session_id()
        cart_item = Cart.query.filter_by(session_id=session_id, book_id=book_id, user_id=None).first()
    
    if cart_item:
        cart_item.quantity += 1
    else:
        cart_item = Cart(
            book_id=book_id,
            quantity=1,
            user_id=current_user.user_id if current_user.is_authenticated else None,
            session_id=None if current_user.is_authenticated else get_session_id()
        )
        db.session.add(cart_item)
    
    db.session.commit()
    flash(f'Added {book.book_title} to your cart', 'success')
    return redirect(url_for('home'))

@app.route('/cart')
def view_cart():
    cart_items = get_cart_items()
    cart_total = get_cart_total()
    return render_template('cart.html', cart_items=cart_items, cart_total=cart_total)

@app.route('/remove_from_cart/<int:cart_id>', methods=['POST'])
def remove_from_cart(cart_id):
    if current_user.is_authenticated:
        item = Cart.query.filter_by(cart_id=cart_id, user_id=current_user.user_id).first_or_404()
    else:
        item = Cart.query.filter_by(cart_id=cart_id, session_id=get_session_id(), user_id=None).first_or_404()
    
    db.session.delete(item)
    db.session.commit()
    flash('Item removed from cart', 'success')
    return redirect(url_for('view_cart'))


@app.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    # Get cart items - adjust based on your implementation
    cart_items = get_cart_items()
    if not cart_items:
        flash('Your cart is empty', 'warning')
        return redirect(url_for('view_cart'))
    
    cart_total = get_cart_total()  # Implement this function
    
    # Get user's saved payment methods
    payment_methods = PaymentMethod.query.filter_by(user_id=current_user.user_id).all()
    
    if request.method == 'POST':
        shipping_address = request.form.get('shipping_address')
        payment_option = request.form.get('payment_option')
        
        # Validate shipping address
        if not shipping_address:
            flash('Please provide shipping address', 'danger')
            return redirect(url_for('checkout'))
        
        # Process payment based on selection
        if payment_option == 'new':
            # Validate new card details
            card_name = request.form.get('card_name')
            card_number = request.form.get('card_number')
            card_expiry = request.form.get('card_expiry')
            card_cvv = request.form.get('card_cvv')
            
            if not all([card_name, card_number, card_expiry, card_cvv]):
                flash('Please provide all card details', 'danger')
                return redirect(url_for('checkout'))
            
            # Save payment method if requested
            if request.form.get('save_payment'):
                try:
                    payment_method = PaymentMethod(
                        user_id=current_user.user_id,
                        name=f"{card_name}'s Card",
                        description=f"•••• •••• •••• {card_number[-4:]}"
                    )
                    db.session.add(payment_method)
                    db.session.commit()
                    flash('Payment method saved successfully', 'success')
                except Exception as e:
                    db.session.rollback()
                    flash('Error saving payment method', 'danger')
            
            # Process payment with card details
            # (Add your payment processing logic here)
            
        elif payment_option == 'saved':
            pmt_mthd_id = request.form.get('pmt_mthd_id')
            if not pmt_mthd_id:
                flash('Please select a payment method', 'danger')
                return redirect(url_for('checkout'))
        
        # Create order
        try:
            order = Order(
                user_id=current_user.user_id,
                ttl_amt=cart_total,
                shipping_address=shipping_address,
                pmt_mthd_id=pmt_mthd_id if payment_option == 'saved' else None
            )
            db.session.add(order)
            db.session.commit()
            
            flash('Order placed successfully!', 'success')
            return redirect(url_for('order_confirmation', order_id=order.order_id))
        except Exception as e:
            db.session.rollback()
            flash('Error placing order', 'danger')
            return redirect(url_for('checkout'))
    
    # GET request - show checkout form
    return render_template('checkout.html',
                         cart_items=cart_items,
                         cart_total=cart_total,
                         payment_methods=payment_methods)


@app.route('/place_order', methods=['GET', 'POST'])
@login_required
def place_order():
    try:
        # Validate form data
        if not all([request.form.get('shipping_address'), 
            request.form.get('payment_option')]):
            flash('Missing required fields', 'danger')
            return redirect(url_for('checkout'))
        
        # Get cart items
        cart_items = get_cart_items()
        if not cart_items:
            flash('Your cart is empty', 'warning')
            return redirect(url_for('view_cart'))
        
        # Process payment
        payment_option = request.form['payment_option']
        pmt_mthd_id = None
        
        if payment_option == 'new':
            # Validate card details
            card_fields = ['card_name', 'card_number', 'card_expiry', 'card_cvv']
            if not all(field in request.form for field in card_fields):
                flash('Missing card details', 'danger')
                return redirect(url_for('checkout'))
            
            # Save payment method if requested
            if 'save_payment' in request.form:
                payment_method = PaymentMethod(
                    user_id=current_user.user_id,
                    name=f"{request.form['card_name']}'s Card",
                    description=f"•••• •••• •••• {request.form['card_number'][-4:]}"
                )
                db.session.add(payment_method)
                db.session.flush()
                pmt_mthd_id = payment_method.pmt_mthd_id
        
        elif payment_option == 'saved':
            pmt_mthd_id = request.form.get('pmt_mthd_id')
            if not pmt_mthd_id:
                flash('Please select a payment method', 'danger')
                return redirect(url_for('checkout'))
        
        # Create order
        order = Order(
            user_id=current_user.user_id,
            ttl_amt=sum(item.book.price * item.quantity for item in cart_items),
            shipping_address=request.form['shipping_address'],
            pmt_mthd_id=pmt_mthd_id,
            status='processing'
        )
        db.session.add(order)
        db.session.flush()
        
        # Add order items
        for item in cart_items:
            if item.quantity > item.book.stock_quantity:
                raise ValueError(f"Not enough stock for {item.book.book_title}")
            
            db.session.add(OrderItem(
                order_id=order.order_id,
                book_id=item.book_id,
                quantity=item.quantity,
                price_at_purchase=item.book.price
            ))
            item.book.stock_quantity -= item.quantity
        
        # Clear cart
        Cart.query.filter_by(user_id=current_user.user_id).delete()
        
        db.session.commit()
        return redirect(url_for('order_confirmation', order_id=order.order_id))
    
    except Exception as e:
        db.session.rollback()
        flash(f'Order failed: {str(e)}', 'danger')
        return redirect(url_for('checkout'))

@app.route('/order_confirmation/<int:order_id>')
@login_required
def order_confirmation(order_id):
    order = Order.query.filter_by(order_id=order_id, user_id=current_user.user_id).first_or_404()
    return render_template('confirmation.html', order=order)

@app.context_processor
def inject_cart_count():
    return {'cart_count': get_cart_count()}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)