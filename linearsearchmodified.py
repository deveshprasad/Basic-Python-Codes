def linearSearch(lst,searchvalue):
    for i in range(len(lst)):
        if lst[i]==searchvalue:
            return i
    return none
lst=eval(input('ENTER A LIST: '))
searchvalue=int(input('ENTER THE VALUE TO BE SEARCHED:'))
searchresult=linearSearch(lst,searchvalue)
print(searchvalue,'found at index',searchresult)
if result==-1:
     print("Element not found in the list")
else:
     print( "Element " + str(x) + " is found at position %d" %(result))
