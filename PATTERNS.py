# Python Program to Print Square Number Pattern
 
side = int(input("Please Enter any Side of a Square  : "))

print("Square Number Pattern") 

for i in range(side):
    for i in range(side):
        print('*', end = '  ')
    print()

# Python Program to Print Right Angled Triangle Star Pattern

rows = int(input("Please Enter the Total Number of Rows  : "))

print("Right Angled Triangle Star Pattern") 
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print('*', end = '  ')
    print()

# Python Program to Print Right Triangle Number Pattern
 
rows = int(input("Please Enter the total Number of Rows  : "))

print("Right Triangle Pattern of Numbers") 
 
for i in range(1, rows + 1):
    for j in range(1, i + 1):        
        print(rows, end = '  ')
    print()

# Python Program to Print Reverse Mirrored Right Triangle Star Pattern

rows = int(input("Please Enter the Total Number of Rows  : "))

print("Reverse Mirrored Right Triangle Star Pattern") 
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if(j < i):
            print(' ', end = '  ')
        else:
            print('*', end = '  ')
    print()

# Python Program to Print Hollow Square Star Pattern

side = int(input("Please Enter any Side of a Square  : "))

print("Hollow Square Star Pattern") 
for i in range(side):
    for j in range(side):
        if(i == 0 or i == side - 1 or j == 0 or j == side - 1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
    print()

# Python Program to Print Hollow Rectangle Star Pattern

rows = int(input("Please Enter the Total Number of Rows  : "))
columns = int(input("Please Enter the Total Number of Columns  : "))

print("Hollow Rectangle Star Pattern") 
for i in range(rows):
    for j in range(columns):
        if(i == 0 or i == rows - 1 or j == 0 or j == columns - 1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
    print()
    
# Python Program to Print Floyd's Triangle

rows = int(input("Please Enter the total Number of Rows  : "))
number = 1

print("Floyd's Triangle") 
for i in range(1, rows + 1):
    for j in range(1, i + 1):        
        print(number, end = '  ')
        number = number + 1
    print()

# Python Program to Print Exponentially Increasing Star Pattern
import math

rows = int(input("Please Enter the total Number of Rows  : "))

print("Exponentially Increasing Stars") 
i = 0
while(i <= rows):
    j = 1
    while(j <= math.pow(2, i)):        
        print('*', end = '  ')
        j = j + 1
    i = i + 1
    print()
    
# Python Program to Print 1 and 0 in alternative rows
 
rows = int(input("Please Enter the total Number of Rows  : "))
columns = int(input("Please Enter the total Number of Columns  : "))

print("Print Number Pattern - 1 and 0 in alternative rows") 
 
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        if(j % 2 != 0):          
            print('1', end = '  ')
        else:
            print('0', end = '  ')
    print()
    