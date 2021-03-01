print("CODE1")
a = int(input(" Please Enter the First Value a: "))
b = int(input(" Please Enter the Second Value b: "))

i = 1
while(i <= a and i <= b):
    if(a % i == 0 and b % i == 0):
        hcf = i
    i = i + 1
    
print("HCF is ",hcf)

print("CODE2")
x = int(input("Enter first number: "))  
y = int(input("Enter second number: "))  
if x > y:  
    smaller = y  
else:  
    smaller = x  
for i in range(1,smaller + 1):
    if((x % i == 0) and (y % i == 0)):  
        hcf = i  

print("The H.C.F. of", x,"and", y,"is", hcf)  


print("CODE3")
def hcf(a,b):
    i=1
    while(i <= a and i <= b):
        if(a % i == 0 and b % i == 0):
            hcf = i
        i = i + 1
        return hcf
a = int(input(" Please Enter the First Value a: "))
b = int(input(" Please Enter the Second Value b: "))
gcd=hcf(a,b)
print("HCF is ",gcd)
   
    