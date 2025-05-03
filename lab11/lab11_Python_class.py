"""
Robiul Hasan
Lab 11: Python class (extra points)
"""

class Student():
    
    #initialized attributes
    def __init__(self, name, age):
        self.name=name
        self.age=age 
        self.grades={}

    #method to add grade
    def add_grade(self, subject, grade):
         self.grades[subject] = grade
         
    #method to calculate average grade
    def get_average_grade(self):
        if not self.grades:
            return 0  # Return 0 if no grades have been added
        else:
            total = sum(self.grades.values())
            average = total/ len(self.grades)
            return average



## call the class and use each methods
Student1=Student("Alan", 20)

Student1.add_grade("Math", 3.8)
Student1.add_grade("Science", 4.6)
Student1.add_grade("ELA", 4.4)
Student1.add_grade("Social Studies", 4.9)


print(f"{Student1.name} average grade is {Student1.get_average_grade()}")


    