"""
Robiul Hasan
May 4, 2025 Flask application
"""
#import Flask
from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy

"""
 create an object 'app' from the Flask module. 
 __name__ set to __main__ if the script is running directly from the main file
"""

#create an instance of the Flask class
app = Flask(__name__)

# connecting to Postrgresql
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Takia0928@localhost/demoDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create a database object db
db=SQLAlchemy(app)

#create a secret key to handle data withing our server
import os
app.config['SECRET_KEY'] = os.urandom(24)

#define a model (create table in teh 'demoDB' databse)
class UserLogin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable = False)

#define an employee model
class Employee(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    employee_id=db.Column(db.String(20), unique=True, nullable=False)
    employee_name=db.Column(db.String(100), nullable=False)

#set the routing to the main page
# 'route' decorator is used to access the root URL
#Define routes using the @app.route decorator
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=='POST':
        return 'Successfully requested! Entered password = '+ request.form['password']
    name="Robiul Hasan"
    checkfruit="Pineapple"
    fruits=['apple', 'orange', 'grapes']
    return render_template('index.html', username=name, listfruits=fruits, checkfruit=checkfruit)

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method=='POST':
        try:
            form = request.form
            #collect the form data
            emp_name = form['employee_name']
            emp_id= form['employee_id']

             #check if employee already exists by name or usee employee id if that's unique
            existing_employee = Employee.query.filter_by(employee_name = emp_name).first()  #boolean -True/False
            existing_id = Employee.query.filter_by(employee_id = emp_id).first()  #boolean -True/False
        
            if existing_employee:
                flash(f"Employee with name '{emp_name}' already exists!")
            if existing_id:
                flash(f"Employee with id '{emp_id}' already exists!")

            # create a new employee object and add form data into the database
            new_employee = Employee(employee_id=emp_id, employee_name=emp_name)

            #store first employee name in session
            session['employee1'] = new_employee.employee_name
            #sdd the new object to our database
            db.session.add(new_employee)
            db.session.commit()

            #message using fladh
            flash(f"{request.form['employee_name']}  successfully added!")
        
        except:
            flash("Fail to insert data! Try again")

        
    return render_template('users.html')



@app.route('/quotes')
def quotes():
    return redirect(url_for('index'))
    

#set the 'app' to run if you execute the file directly (not when it is imported)
if __name__ == '__main__':
    with app.app_context():db.create_all()
    app.run(debug=True)