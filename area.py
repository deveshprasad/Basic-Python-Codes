import math

def Area_of_Circle(radius):
    a =  math.pi * radius * radius
    
    print("\n The Surface area of a Sphere = %.2f" %a)
    

Area_of_Circle(6)

# Python Program to find Diameter, Circumference, and Area Of a Circle


def find_Diameter(radius):
    return 2 * radius

def find_Circumference(radius):
    return 2 * math.pi * radius

def find_Area(radius):
    return math.pi * radius * radius

r = float(input(' Please Enter the radius of a circle: '))

diameter = find_Diameter(r)
circumference = find_Circumference(r)
area = find_Area(r)

print("\n Diameter Of a Circle = %.2f" %diameter)
print(" Circumference Of a Circle = %.2f" %circumference)
print(" Area Of a Circle = %.2f" %area)

# Python Program to find Area of an Equilateral Triangle


side = float(input('Please Enter Length of any side of an Equilateral Triangle: '))

# calculate the area
Area = (math.sqrt(3)/ 4)*(side * side)

# calculate the Perimeter
Perimeter = 3 * side

# calculate the semi-perimeter
Semi = Perimeter / 2

# calculate the Altitude
Altitude = (math.sqrt(3)/2)* side

print("\n Area of Equilateral Triangle = %.2f" %Area)
print(" Perimeter of Equilateral Triangle = %.2f" %Perimeter)
print(" Semi Perimeter of Equilateral Triangle = %.2f" %Semi)
print(" Altitude of Equilateral Triangle = %.2f" %Altitude)

# Python Program to find Angle of a Triangle if two angles are given

def triangle_angle(a, b):
    return 180 - (a + b)

a = float(input('Please Enter the First Angle of a Triangle: '))
b = float(input('Please Enter the Second Angle of a Triangle: '))

# Finding the Third Angle
c = triangle_angle(a, b)
print("Third Angle of a Triangle = ", c)