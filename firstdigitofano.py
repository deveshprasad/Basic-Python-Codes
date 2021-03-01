n=int(input("ENTER A NO:"))
first_digit=n
while(first_digit>=10):
    first_digit=first_digit//10
print("The First Digit from a Given Number {0} = {1}".format(n, first_digit))
last_digit = n % 10
print("The Last Digit in a Given Number",last_digit)
