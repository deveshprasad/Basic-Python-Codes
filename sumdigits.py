Number = int(input("Please Enter any Number: "))
Sum = 0

while(Number > 0):
    Reminder = Number % 10
    Sum = Sum + Reminder
    Number = Number //10

print("\n Sum of the digits of Given Number = %d" %Sum)

def Sum_Of_Digits(Number1):
    Sum1 = 0
    while(Number1 > 0):
        Reminder = Number1 % 10
        Sum1 = Sum1 + Reminder
        Number1 = Number1 //10
    

Number1 = int(input("Please Enter any Number: "))
sum=Sum_Of_Digits(Number1)
print("\n Sum of the digits of Given Number = %d",sum)
