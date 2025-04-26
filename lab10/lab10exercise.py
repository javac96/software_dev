"""
Robiul Hasan
Lab 10: Loops in Python
"""
colors = ['red', 'orange', 'olive', 'magenta', 'green']
usercolor=input("Please enter a color name: ").strip().lower()

is_found=False #a flag to indicate when the color is found

for color in colors:
    if color == usercolor: #check if user entered color is in the list
        is_found = True #color found
        print(f"{usercolor} is in the list")
        break #Exit the loop if color is found
else:
    print(f"{usercolor} is NOT in the list")



        
        
        
    