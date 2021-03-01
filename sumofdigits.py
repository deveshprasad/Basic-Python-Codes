Number=int(input("Enter a no. :"))
sum=0
while(Number>0):
	i=Number%10
	sum=sum+i
	Number=Number//10
print("Sum of digits =",sum)	