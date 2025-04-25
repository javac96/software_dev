"""
Robiul Hasan
April 24, Conditional Statement
"""
print("\n---------example 1: if statement-----------")
age=20
agecode=123

if age>=21:
    print("You are an adult!")
    agecode=200
else:
    print("Your are under 21")
    agecode=100
print(f"After the 'if' statement, agecode={agecode}")

print("\n---------example 2: if-else statement-----------")
age=20
agecode=123

if age>=21:
    print("You are an adult!")
    agecode=200
print(f"After the 'if' statement, agecode={agecode}")

print("\n---------example 3: multi statemnt-----------")
age=32
if 0<=age<21:
    print ("You are minor!")
elif 21<=age<65:
    print("You are an adult!")
elif 65<=age<=130:
    print("Your are a senior citizen")
else:
    print("Unable to read age!")

print("\n---------example 4: AND operator----------")
temparature=90
humidity=60
if 70<=temparature<=90 and humidity<80:
    print("The weather is pleasant")
else:
    print("The weather is not ideal")

print("\n---------example 5: OR operator----------")
day='Monday'
is_holiday=True

if day=='Saturday' or day=='Sunday' or is_holiday:
    print("You can relax today")
else:
    print("Is is a workday")

print("\n---------example 6: nestd conditional statement----------")
number=int(input("Enter a number: "))
if number>=0:
    if number==0:
        print(f"{number} is zero")
    else:
        print(f"{number} is positive")
    print(f"{number} is positive")
else:
    print(f"{number} is negative")

print("\n---------example 7: usename validation----------")
#username validation, it must have 3+ chars
username=input("Enter a username: ").strip()
len_username=len(username)
if len_username>=3:
    print(f"{username} has 3+ chars")
    index_whitespace=username.find("  ")
    if index_whitespace == -1:
        print(f"{username} is valid")
    else:
        print(f"Username CANNOT have whitespace")
else:
    print(f"{username} is INVALID. Username must have 3+ chars")

print("\n---------example 8: match-case statement----------")
response_code=400
match response_code:
    case 400:
        print(f"Code= {response_code}. Server CANNOT understand")
    case 401 | 403:
        print(f"Code= {response_code}. Server refused to send back")
    case 404:
        print(f"Code= {response_code}. Server CAN'T find")
    case _:
        print("Invalid code!")
print("\n---------LAB EXERCISE----------")
grade1= float(input("Enter grade 1: "))
grade2= float(input("Enter grade 2: "))
average=(grade1+grade2)/2
if 0<=average<=100:
    if 90<=average<=100:
        print(f"For the average of {average}, you GPA is A")
    elif 70<=average<=89.99:
        print(f"For the average of {average}, you GPA is B")
    elif 60<=average<=69.99:
        print(f"For the average of {average}, you GPA is C")
    else:
        print(f"For the average of {average}, you GPA is FAIL!")
else:
    print(f"UNDEFINED!")


    



