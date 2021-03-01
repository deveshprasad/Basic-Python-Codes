# Python Program to find Total, Average, and Percentage of Five Subjects
 
english = float(input("Please enter English Marks: "))
math = float(input("Please enter Math score: "))
economics = float(input("Please enter Economics Marks: "))
physics = float(input("Please enter Physics Marks: "))
chemistry = float(input("Please enter Chemistry Marks: "))

total = english + math + economics + physics + chemistry
average = total / 5
percentage = (total / 500) * 100
print("Total Marks =",total)
print("Average Marks =",average)
print("Marks Percentage =",percentage)
if percentage>33:
    print("PASS BITCH")
else:
    print("FAIL MOTHERFUCKER")

