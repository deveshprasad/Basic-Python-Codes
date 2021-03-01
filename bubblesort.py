def bubble_sort(list):
   # We go through the list as many times as there are elements
    for i in range(len(list)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(list) - 1):
            if list[j] >list[j+1]:
                # Swap
                list[j], list[j+1] = list[j+1], list[j]
#Now, let's populate a list and call the algorithm on it:

list = [19, 13, 6, 2, 18, 8]
bubble_sort(list)
print(list)