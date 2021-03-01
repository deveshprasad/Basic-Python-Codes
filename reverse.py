Number = int(input("Please Enter any Number: "))
Reverse = 0
while(Number > 0):
    Reminder = Number %10
    Reverse = (Reverse *10) + Reminder
    Number = Number //10

print("\n Reverse of entered number is = %d" %Reverse)

def Reverse_Integer(Number):
    Reverse = 0
    while(Number > 0):
        Reminder = Number %10
        Reverse = (Reverse *10) + Reminder
        Number = Number //10
    

Number = int(input("Please Enter any Number: "))
Reverse_Integer(Number)
print("\n Reverse of entered number is = %d" %Reverse)
