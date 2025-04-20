""" Robiul Hasan
April 20, Introduction Python"""
' Robiul Hasan\nApril 20, Introduction Python'
#Single comment. This line WILL NOT run
print('\n---------Example 1: String characters---------------')
print("\tGood morning! \nThis is my first \"Python\" code!")
print('\n---------Example 2: Data Type---------------')
print(f"Data type of 3.56={type(3.56)}")
print(f"Data type of -25={type(-25)}")
print(f"Data type of 'Hello World!'={type('Hello World!')}")
print(f"Data type of '$'={type('$')}")
print(f"Data type of ''={type('')}")
print(f"Data type of False={type(False)}")
print(f"Data type of False={type(False)}")
print('\n---------Example 3: Variables---------------')
#Declare a variable
number1=25.5
number2=-12
username="Robiul Hasan"
add_numbers=number1+number2
is_raining=True
#prompt results
print(f"{username}, the sum of {number1} and {number2} is {add_numbers}")
print(f"Is it raining today?={is_raining}")
print('\n---------Example 4: assigning values to multiple Variables---------------')
#declare multiple variables
item1, item2, item3="apples", 23, False
print(f"item 1={item1}, item 2={item2}, item 3={item3}")
#declare multiple variables with the same value
score1=score2=score3=88
print(f"score 1={score1}, score 2={score2}, score 3={score3}")
print('\n---------Example 5: Input command-------------')
print("Enter username:")
username=input()
print(username)
print(f"Collected username={username}")

#cast from string to integer
luckynumber=int(input("Enter a lucky number:"))
print(f"Lucky number= {luckynumber}")

#double the lucky number, 
dblucky=luckynumber*2
print (f"Double of lucky={dblucky}")
#cast from string to integer
triplenumber=luckynumber*3
print (f"Tripled of lucky={triplenumber}")

#cast integer to bool, 0 is False, any other number is True
completed_task=0
print(f"completed task={bool(completed_task)}")

print('\n---------Example 6: Arithmatic operators------------')
num1=10
num2=9

print(f"The sum of {num1} and {num2} is {num1+num2}")
print(f"The difference of {num1} and {num2} is {num1-num2}")
print(f"The product of {num1} and {num2} is {num1*num2}")
print(f"The quotient of {num1} and {num2} is {num1/num2}")
print(f"The modulus of {num1} and {num2} is {num1%num2}")
print(f"The integer of quotient of {num1} and {num2} is {num1//num2}")
print(f"The result of {num1} and {num2} is to the power of 3 is {num2**3}")

print('\n---------Example 7: Hypotenuse calculation------------')
#declare and asaign value
x=float(input("Enter side 1: "))
y=float(input("Enter side 2: "))
#calculation the hypotenuse
hyp=(x**2+y**2)**0.5
#promt the result
print(f"The hypotenuse fo {x:0.1f} and {y} is {hyp:0.2f}")

print('\n---------Example : 8 Assignment operators------------')
n=2
print(f"number={n}")
n+=3
print(f"number+3={n}")
n-=2
print(f"updated number={n}")

print('\n---------Example : 9 Comparison operators------------')
n1=10
n2=3
n3=7
compare1=n1==n2
compare2=n1==(n2+n3)
print(f"is n1 equal n2?   {compare1}")
print(f"is n1=n2+n3 equal n2?   {compare2}")
compare3=n1>n2
compare4=n2<=n3
print(f"is n1 greater than n2?    {compare3}")
print(f"is n2 less than or equal to n3?   {compare4}")

print('\n---------Example : 10 String indexing------------')
username="rhasan123"
print(f"The fifth character = {username[4]}")

#Positive indexing
print(f"The fifth character = {username[4]}")
#negative indexing
print(f"The fifth last character = {username[-5]}")

print('\n---------Example : 11 String slicing------------')
print(f"Slice from beginning to 4th character  {username[:4]}")
print(f"Slice from 5th to end {username[4:]}")

#slice from the 3rd to the 8th chars
print(f"slice from the 3rd to the 8th chars= {username[2:8]}")

print(f"slice from the 4rth to the 6th chars using negative index= {username[-8:-5]}")

print('\n---------Example : 12 total chars in a string is len method-----------')
print(f"username has ={len(username)} characters")





