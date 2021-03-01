# Python Program to display Multiplication Table

i = int(input(" Please Enter any Positive Integer lessthan 10 : "))

print(" Multiplication Table ")

while(i>=0):
    j = 1
    print('TABLE OF',i)
    while(j <= 10):
        print('{0}  *  {1}  =  {2}'.format(i, j, i*j))
        j = j + 1
    break
  