"""
Robiul Hasan
April 25, loops
"""

print("n\------------Example 1: for loop as a counter------------------")
#print Hellow from 0 to 4
for x in range(0,5):
    print(f"Hello = {x}")
    print('Hello', x)

print("n\------------Example 2: for loop in a list------------------")
fruits=['apples', 'oranges', 'grapes', 'kiwis', 'pineapple']
for eachfruiteInd in range(0,len(fruits)):
    print(f"Fruit with index  {eachfruiteInd}={fruits[eachfruiteInd]}")

#alternative way to loop through
print("\n---alternative way--")
for eachfruite in fruits:
    print(eachfruite)

print("n\------------Example 3: for loop with different increment------------------")
#for loop to print from 2 to 30 with an increment of 3
for num in range(2, 30, 3):
    print(num)

print("n\------------Example 4: for loop with different deccrement------------------")
#for loop to print from 10 to 0 with a decrement of 2
for num in range(10, 0, -2):
    print(num)

print("n\------------Example 5: loop through a string------------------")
username="rtypan123"
for eachcharacter in username:
    print(eachcharacter)

print("n\------------Example 6: nested conditional statement in for loop------------------")
#for loop to get count of negative numbes
numbers = [5,-2,0,8,9,-1]
negativecounter=0
for eachnumber in numbers:
    if eachnumber<0:
        negativecounter+=1 #the same as negativenumber=negativenumber+1
#promt the result
print(f"There is/are {negativecounter} negative numbers")

print("n\------------Example 7: nested conditional statement:operation------------------")
#for loop to add all odd numbers
sumodd = 0
for eachnumber in numbers:
    if (eachnumber%2==1):
        sumodd+=eachnumber
#promt result
print(f"The sum of all odd number is {sumodd}" )

print("n\------------Example 8: break statement in a loop------------------")
#for loop to print  from 0 to 10(exclusive), and terminate the loop when it reaches to 5
for n in range(10):
    if n==5:
        print("Counter reaches to 5")
        break
    else:
        print(n)

print("n\------------Example 9: continue statement in a loop------------------")
#for loop to add numbers from 0 to 10(exclusive), except number 5
sumall=0
for n in range(10):
    if n==5:
        print("skipping 5")
        continue
    sumall+=n
    print(n)
    print(f"\tsum={sumall}")

print("n\------------Example 10: else statement in a for loop------------------")
for n in range(6):
    if n==3:
        break
    print(n)
else:
    print("Loop completed")

print("n\------------Example 11: while loop as a counter------------------")
#while loop to print o to 5 (inclusive)
n=0
while n<6:
    print(n)
    n+=1

print("n\------------Example 12: while loop as a checkpoint------------------")
#while loop to collect and add numbers between -5 to 5
sumusernumber=0
while(True):
    number=int(input("Enter a number between -5 and 5: "))
    if number<-5 or number>5:
        break
    sumusernumber+=number
#promt result
print(f"The total sum is = {sumusernumber}")

print("n\------------Example 13: while loop as couting operator------------------")
#while loop to count the even numbers in the list
numbers=[2,0,-5,1,8,-6,-7,-3]
index=0
len_numbers=len(numbers)
eventcount=0
while index<len_numbers:
    if numbers[index]%2==0 and not(numbers[index]==0):
        eventcount+=1
    index+=1
else:
    print(f"There is/are {eventcount} even numbers")


