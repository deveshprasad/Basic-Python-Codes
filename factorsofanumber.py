# Python Program to find Factors of a Number
 
number = int(input("Please Enter any Number: "))

value = 1
print("Factors of a Given Number",number,"are:")

while (value <= number):
    if(number % value == 0):
        print(value)
    value = value + 1
