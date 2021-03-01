def dim(l,b,h):
    l=int(input("Enter length of building : "))
    b=int(input("Enter breadth of building : "))
    h=int(input("Enter heigth of building : "))
def area(l,b,h):
    area=l*b*h
def perimeter(l,b,h):
    perimeter=2(l*b+b*h+h*l)
a1=area(l,b,h)
p1=perimeter(l,b,h)
print("The area of builing is : ",a1,p1)