pos=-1
def search(list,n):
    i=0
    while(i<len(list)):
        if list[i]==n:
            globals()["pos"]=i
            return True
        i=i+1
    return False
        
list=input("enter list:")
n=input('enter search value :')
if search(list,n):
    print("FOUND at index ",pos)
else:
    print("NOT FOUND")
