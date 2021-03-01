#Implementation of linear search

def linear_search(lst,value) :
    for i in range(0,len(lst)) :
        if lst[i]==value :                           #checking the value
            return i
    return None
lst=eval(input("Enter alist"))                         #entering the list
search=eval(input("Enter the value to be searched :"))
result=linear_search(lst,value)
print(result)