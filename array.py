#ARRAY
#HOW TO CREATE BY IMPORTING
#import array
import array as arr #   most commonly used
#from array import*
a=arr.array('i',[1,2,3,4,5])
print(a[2],len(a))
print(a[-1])
a.append(6)
print(a)
a.extend([7,8,9,10,11,12])
print(a)
a.insert(0,0)
print(a)
print(a.pop())
print(a.pop(-1))
print(a)
a.remove(10)
print(a)
#concatenation
b=arr.array('i',[10,11,12])
c=arr.array('i')
c=a+b
print('ARRAY C=',c)
print(c[10:])
print(c[:-2])
#array('i')
print(c[-2:-5])
print(c[::-1])
#reverse the array but doesnt change the  original
print(c)
#for loop
for x in c:
    print(x)
print('now while')
b=0
while b<len(c):
    print(c[b])
    b=b+1
temp=0
while temp<c[5]:
    print(c[temp])
    temp+=1