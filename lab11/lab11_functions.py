"""
Robiul Hasan
Apr 27, 2025 Functions
"""
import math
#Example 3
def greeting():
    print("Welcome to functions")

#example 4:function with parameter
def printusername(username):
    print(f"Welcome to function {username}")

#example 5:function with default parameter
def user_country(username="Unknown", country="USA"):
    print(f"{username} is living in {country}")

#example 6: function having return
def product(n1=1,n2=3):
    return n1*n2
#example 7: boolean function
def multiple3(n):
    if n%3 == 0 and n!=0:
        return True
    else:
        return False
    
#example 8: Composition function
def collectnum():
    n=float(input("Enter an number between 1 and 9(inclusive)"))
    while(not(1<=n<=9)):
        n=float(input("Re-enter a number again: "))
    return n
#function that adds totalnumbser amount of numbers and returns the sum fo the numbers
def sumnumbers(totalnumbers):
    sum=0
    for n in range(totalnumbers):
        sum+=collectnum() #composition functions
    return sum

#function to print result
def printresult(totalsum):
    print(f"Sum of all numbers is = {totalsum}")

#example 9: using built in 
#find area
def areacircle(radius):
    a=math.pow(radius,2)*math.pi
    return round(a,2)
#function to print radius
def areaprint(area, radius=0):
    print(f"The of a circle with {radius} radius  is {area}") 

#example 10:try-except
def ratio_hour(hour):
    try:
        dayhour=24
        return dayhour/hour
    except ZeroDivisionError:
        print("Number can't be divided by zero")
        return 0
    except ValueError:
        print("Number was not provided")
        return 0
    except:
        print("There was an error in the division")
    else:
        return r
    finally:
        print("-----------Process completed-------------")

    #Example 11: Class
class Myclass:
    id=12345 #property attribute

        #method
    def msg(self):
            return "Welcome to Python class"

#example 12
class Complexnumber():
    #instantiation
    def __init__(self, realnumber, imgnumber):
        self.r=realnumber
        self.i=imgnumber

#example 13
class Car:
    def __init__(self, make, model, year):
        self.carmake=make
        self.carmodel=model
        self.caryear=year

    odometer_reading=0

    def get_car_description(self):
        return f"{self.carmake} with model {self.carmodel} was made on {self.caryear}"
    
    def read_odometer(self):
        return f"This car has {self.odometer_reading} miles on it"
    
    def update_odometer(self, mileage):
        if mileage>self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print ("Odometer cann't roll back")

    def increment_odometer(self, miles):
        if miles>0:
            self.odometer_reading+=miles
        else:
            print("Can't add negative miles")