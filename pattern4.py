n=int(input("Enter a no. :"))
for i in range(0,n+1):
	for j in range(n-1,0,-1):
		print(end=" ")
	for j in range(i,0,-1):
		print(j,end=" ")
	for j in range(2,i+1):
		print(j,end=" ")
	print("\n")