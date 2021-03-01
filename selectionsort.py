A = input('ENTER A LIST: ')
for i in range(len(A)):
   min= i
   for j in range(i+1, len(A)):
      if A[min] > A[j]:
         min = j
   #swap
A[i], A[min] = A[min], A[i]
# main
for i in range(len(A)):
   print(A[i])

