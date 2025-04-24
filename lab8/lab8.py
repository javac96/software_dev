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

print('\n---------Example : 13 Strin() method-----------')
username="        peterpan123     "
print(f"The username= {username}. End od username")    
username=username.strip() 
print(f"The whitespace removed username= {username}. End od username")
username=username.upper() 
print(f"The uppercase username= {username}. End od username")
username=username.lower() 
print(f"The lowercase username= {username}. End od username")
username=(username).upper().replace('p', '%') 
print(f"The repalced u in  username= {username}. End od username")

print('\n------ Example 16: split method ------')
msg = "Introduction to Python Programming! Today we are learning string methods"
print(f"Message = {msg}")
print(f"Message after split method = {msg.split('!')}")

print('\n------ Example 17: find method ------')
# find the letter 'P'
index_P = msg.find('P')
print(f"Index of letter P is = {index_P}")

# find the second letter 'P'
sec_index_P = msg.find('P', index_P + 1)
print(f"Next index of letter P is = {sec_index_P}")

# find a non-existing letter 'Y'
index_Y = msg.find('Y')
print(f"The index of letter Y is = {index_Y}")

print('\n------ Example 18: in, not in statement ------')
# check if the word 'we' is in the msg 
answer_we = "we" in msg
print(f"Is the word 'we' in the 'msg' string? = {answer_we}")

# check if the word 'Today' is NOT in the msg 
answer_today = "Today" not in msg
print(f"Is the word 'Today' NOT in the 'msg' string? = {answer_today}")


print('\n------ Example 19: list indexing ------')
colors = ["orange", "magenta", "olive"]
numbers = [6, 20, -9, 5, -12]
mixedlist = [False, 20, "Peter", True, -9]
emptylist = []

print(f"Colors list = {colors}")
print(f"Numbers list = {numbers}")
print(f"Empty list = {emptylist}")
print(f"Mixed list = {mixedlist}")

print(f"2nd color = {colors[1]}")
print(f"1st number = {numbers[0]}")
# print(f"3rd value = {emptylist[2]}")  # can not return empty character

print(f"Last color = {colors[-1]}")
print(f"3rd last number = {numbers[-3]}")

print('\n------ Example 20: + * operator on list ------')
# concatenate the first with the last color
new_color = colors[0] + colors[-1]
print(f"The new color is = {new_color}")

print('\n------ Example 21: remove items from a list ------')
# remove the 2nd last color
colors.pop(-2)
print(f"Colors after pop = {colors}")

print('\n------ Example 22: adding items to the list ------')
# add items to the end of list colors
colors.append("PINK")
print(f"Colors after append = {colors}")

# add a new list to a list
colors.append(["blue", "green"])
print(f"Colors after append = {colors}")

print('\n------ Example 23: sort method ------')
colors = ["orange", "magenta", "olive", "Magenta"]
print(f"Color list = {colors}")
colors.sort()
print(f"Color list sorted = {colors}")

bool_list = [True, True, False]
bool_list.sort()
print(f"Bool list sorted = {bool_list}")

print('\n------ Example 24: count method ------')
count_true = bool_list.count(True)
print(f"There is {count_true} True values")

count_red = colors.count("red")
print(f"There is/are {count_red} red colors")

print('\n------ Example 25: length of a list ------')
length_colors = len(colors)
print(f"There is/are {length_colors} colors")

print('\n------ Example 26: index of an item in a list ------')

# index of color 'olive'
index_olive = colors.index("olive")
print(f"The index of color olive is {index_olive}")







