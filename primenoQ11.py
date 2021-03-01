n=int(input("Enter a no:"))
count=0
for i in range(2,(n//2)+1):
	if(n%i==0):
		count=count+1
		break
if(count==0):
	print(n,"is a prime number")
else:
	print(n,"is not a prime number ")		
