n=int(input("Enter a no. :"))
for i in range(0,n+1):
	for j in range(n-i,0,-1):
		print(j,end=" ")
	print("\n")	