n=int(input("Enter a no. :"))
for i in range(n-1,0,-2):
	for j in range(1,i+1):
		print(j,end=" ")
	print("\n")	