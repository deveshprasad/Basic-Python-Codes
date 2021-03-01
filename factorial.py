#factorial
num=int(input("Enter a no :"))
i=num
while(i>1):
	i=i-1
	num=i*num
print("Factorial value =",num)


import math 
number = int(input(" Please enter any Number to find factorial : "))
fact = math.factorial(number)
print("The factorial of %d  = %d" %(number, fact))


number = int(input(" Please enter any Number to find factorial : "))
fact = 1
for i in range(1, number + 1):
    fact = fact * i
print("The factorial of %d  = %d" %(number, fact))







def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i



number = int(input(" Please enter any Number to find factorial : "))

factorial(number)
print("The factorial of %d  = %d" %(number, facto))
