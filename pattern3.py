n=int(input("Enter :"))
k=2*n-2
for i in range(1,n):
	for j in range(1,k):
		print(end=" ")
	k=k-2
	for j in range(1,i+1):
		print("*",end=" ")
	print("\n")	
	
	