# Python Program to find Sum of Arithmetic Progression Series

a = int(input("Please Enter First Number of an A.P Series: : "))
n = int(input("Please Enter the Total Numbers in this A.P Series: : "))
d = int(input("Please Enter the Common Difference : "))

total = (n * (2 * a + (n - 1) * d)) / 2
tn = a + (n - 1) * d

print("\nThe Sum of Arithmetic Progression Series = " , total)
print("The tn Term of Arithmetic Progression Series = " , tn)

a = int(input("Please Enter First Number of an A.P Series: : "))
n = int(input("Please Enter the Total Numbers in this A.P Series: : "))
d = int(input("Please Enter the Common Difference : "))

# Python Program to find Sum of Geometric Progression Series
import math

a = int(input("Please Enter First Number of an G.P Series: : "))
n = int(input("Please Enter the Total Numbers in this G.P Series: : "))
r = int(input("Please Enter the Common Ratio : "))

total = (a * (1 - math.pow(r, n ))) / (1- r)
tn = a * (math.pow(r, n - 1))

print("\nThe Sum of Geometric Progression Series = " , total)
print("The tn Term of Geometric Progression Series = " , tn)


# Python Program to calculate Sum of Series 1²+2²+3²+….+n²
 
number = int(input("Please Enter any Positive Number  : "))
total = 0

total = (number * (number + 1) * (2 * number + 1)) / 6

print("The Sum of Series upto {0}  = {1}".format(number, total))

# Python Program to calculate Sum of Series 1³+2³+3³+….+n³
import math 

number = int(input("Please Enter any Positive Number  : "))
total = 0

total = math.pow((number * (number + 1)) /2, 2)

print("The Sum of Series upto {0}  = {1}".format(number, total))
