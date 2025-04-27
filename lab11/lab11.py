"""
Robiul Hasan
Apr 27 2025, Python applications
"""
from lab11_functions import * #Import all from funtions file
import math
print("n\------------example 1: Pythong Dictionary---------------")
#create a dictonary
car={
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
#print a complete dictionary
print(car)

#accesing items in a dictionary we use [], where [] goes the key's name
print(f"The year of the car is = {car['year']}")
#update the value of the key
car["year"]=1980
print(f"Year updated to ={car['year']}")
print("Year updated to =", {car['year']})
#add key value
car['color']="red"
print(car)

print ("\n loop through each key in the dictionary")
for k in car:
    print(k)
print ("\n loop through each value in the dictionary")
for k in car:
    print(car[k])
print ("\n loop through each pair in the dictionary")
for k in car:
    print(f"{k} has value={car[k]}")

print("n\------------example 2: Python dictionary application---------------")
# Create a dictionary that counts the number of times that counts the number of times
phrase = "to be or not to be"
print(f"Original phrase = {phrase}")
phrase_split = phrase.split()
print(f"Splitted phrase = {phrase_split}")
#create a dictionary
word_count_dict={}
#loop thru the list
for word in phrase_split:
    print(word)
    if word in word_count_dict:
        word_count_dict[word]+=1
    else:
        word_count_dict[word]=1

#print result
print("Result of dictonary: ")
for w in word_count_dict:
    print(f"'{w}'={word_count_dict[w]}")

print("n\------------example 3: Function that does not return values---------------")
#call funtion 'greeting'
greeting()

print("n\------------example 4: function with params---------------")
#call fuction
printusername("Testuser")
print("n\------------example 5: function with default params---------------")
user_country("testuser", "Chile")
user_country("Anna")
user_country()

print("n\------------example 6: function with return value---------------")
num1=2
num2=-6
prod1=product(num1, num2)
print(f"The product of {num1} and {num2} is = {prod1}")
prod1=product(num1)
print(f"The product of {num1} and {num2} is = {prod1}")
prod1=product()
print(f"The product of {num1} and {num2} is = {prod1}")

print("n\------------example 7: function with boolean value---------------")
checknum1= multiple3(num1)
checknum2= multiple3(num2)
print (f"Is {num1} multiple of 3? {checknum1}")
print (f"Is {num2} multiple of 3? {checknum2}")

print("n\------------example 8: composition function---------------")
#test collectnum()
#number=collectnum()
#print(number)
#test sumnumbers()

sumall=sumnumbers(3)
#print(sumall)
printresult(sumall)

print("n\------------example 9: built-in function---------------")
r=2
a=areacircle(r)
areaprint(a,r)

print("n\------------example 10: try-except--------------")
r1=ratio_hour(0)#zero exception
r2=ratio_hour(3) 
r3=ratio_hour("Peter")

print("n\------------example 11: Python class--------------")
#Create an instance of the class
x=Myclass()
print(f"An instance of the class = {x}")
x_id=x.id
print(f"id is = {x_id}")
print(f"Calling the function here: {x.msg()}")

print("n\------------example 12: Instantiation of class--------------")
#initialization 
paircomplexnumber=Complexnumber(2, 3)
real=paircomplexnumber.r
print(f"Real part is {real}")


print("n\------------example 13: class--------------")
#initialization  of car class
car1=Car("Tesla", "S", 2023) 
car_reading=car1.odometer_reading
print(f"Car miles reading = {car_reading}")
print(car1.get_car_description())
print(car1.read_odometer())
car1.update_odometer(10)
print(car1.read_odometer())
car1.update_odometer(5)
print(car1.read_odometer)

#add 20 miles to the odometer
car1.increment_odometer(20)
print(car1.read_odometer())
car1.increment_odometer(-5)
print(car1.read_odometer())
car1.increment_odometer(8)
print(car1.read_odometer())