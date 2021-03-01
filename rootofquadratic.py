import math
a=int(input("ENTER VALUE OF a IN QUADRATIC EQUATION:"))
b=int(input("ENTER VALUE OF b IN QUADRATIC EQUATION:"))
c=int(input("ENTER VALUE OF c IN QUADRATIC EQUATION:"))
d=(b*b)-(4*a*c)
if d>0:
    root1=int(-b+math.sqrt(d)/(2*a))
    root2=int(-b-math.sqrt(d)/(2*a))
    print("Two Distinct Real Roots Exists:",root1,"and", root2)
elif(d == 0):
    root1 = root2 =int(-b /(2 * a))
    print("Two Equal and Real Roots Exists:",root1,"and", root2)
elif(d < 0):
    root1 = root2 = int(-b/(2 * a))
    imaginary =int( math.sqrt(-d) / (2 * a))
    print("Two Distinct Complex Roots Exists:root1 =",(root1+imaginary),"and",(root2-imaginary))

    
