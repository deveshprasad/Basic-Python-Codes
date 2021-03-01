#armstrongno.
Number = int(input(" Enter the Number to Check for Armstrong: "))
Sum = 0
Times = 0
Temp = Number
while Temp > 0:
           Times = Times + 1
           Temp = Temp // 10
Temp = Number
while Temp > 0:
           Reminder = Temp % 10
           Sum = Sum + (Reminder ** Times)
           Temp //= 10
if Number == Sum:
           print(Number,"is armstrong number")
else:
           print(Number,"is not an armstrong number")