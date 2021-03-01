number = int(input("Please Enter any Number: "))
total = 0

for value in range(1, number + 1):
    total = total + value

average = total / number

print("The Sum of Natural Numbers ",total)
print("Average of Natural Numbers ",average)
