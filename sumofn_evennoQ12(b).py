#sumofnevennumbers
n=int(input("Enter a no. :"))
sum=0
for x in range(1,2*n+1):
	if(x%2==0):
		print(x,"+",end=" ")
		sum=sum+x
print("\n The sum is ",sum)		