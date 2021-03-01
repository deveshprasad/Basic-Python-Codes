#To find reverse of a number and sum of its digit
number=int(input("Enter number to compute its reverse and sum of digits: "))
def reverse(number):
    Reverse = 0
    while(number > 0):
        Reminder = number %10
        Reverse = (Reverse *10) + Reminder
        number = number //10
        
def sumofdigits(number) :
    temp=number
    sum1=0
    while temp>0 :
        digit=temp % 10                                           
        sum1 = sum1 + digit                                       
        temp=temp//10
    
reverse(number)
sumofdigits(number)
print("The reverse of ",number,"is : ",reverse)
print("The sum of digits is : ",sum1)



                
