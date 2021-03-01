# Python Program to find Volume and Surface Area of Sphere using Functions

import math

def Area_of_SPHERE(radius):
    sa =  4 * math.pi * radius * radius
    Volume = (4 / 3) * math.pi * radius * radius * radius
    print("\n The Surface area of a Sphere = %.2f" %sa)
    print("\n The Volume of a Sphere = %.2f" %Volume)

Area_of_SPHERE(10)

# Python Program to find Volume & Surface Area of a Cylinder using Functions


def Vol_Sa_Cylinder(radius, height):
    sa = 2 * math.pi * radius * (radius + height)
    Volume = math.pi * radius * radius * height
    L = 2 * math.pi * radius * height
    T = math.pi * radius * radius

    print("\n The Surface area of a Cylinder = %.2f" %sa)
    print(" The Volume of a Cylinder = %.2f" %Volume)
    print(" Lateral Surface Area of a Cylinder = %.2f" %L)
    print(" Top OR Bottom Surface Area of a Cylinder = %.2f" %T)

Vol_Sa_Cylinder(6, 4)
# Python Program to find Volume and Surface Area of a Cube Using Functions

def Vo_Sa_CUBE(l):
    sa = 6 * (l * l)
    Volume = l * l * l
    LSA = 4 * (l * l)

    print("\n Surface Area of Cube = %.2f" %sa)
    print(" Volume of cube = %.2f" %Volume)
    print(" Lateral Surface Area of Cube = %.2f" %LSA)

Vo_Sa_CUBE(6)

# Python Program to find Volume and Surface Area of a Cone using functions


def Vo_Sa_Cone(radius, height):
    # Calculate Length of a Slide (Slant)
    l = math.sqrt(radius * radius + height * height)

    # Calculate the Surface Area
    SA = math.pi * radius * (radius + l)

    # Calculate the Volume
    Volume = (1.0/3) * math.pi * radius * radius * height

    # Calculate the Lateral Surface Area
    LSA = math.pi * radius  * l

    print("\n Length of a Side (Slant)of a Cone = %.2f" %l)
    print(" The Surface Area of a Cone = %.2f " %SA)
    print(" The Volume of a Cone = %.2f" %Volume)
    print(" The Lateral Surface Area of a Cone = %.2f " %LSA)

Vo_Sa_Cone(6,10)

# Python Program to find Volume and Surface Area of a Cuboid using Functions

def Vo_Sa_Cuboid(length, width, height):
    # Calculate the Surface Area
    SA = 2 * (length * width + length * height + width * height)

    # Calculate the Volume
    Volume = length * width * height

    # Calculate the Lateral Surface Area
    LSA = 2 * height * (length + width)

    print("\n The Surface Area of a Cuboid = %.2f " %SA)
    print(" The Volume of a Cuboid = %.2f" %Volume)
    print(" The Lateral Surface Area of a Cuboid = %.2f " %LSA)

Vo_Sa_Cuboid(9, 4, 6)
