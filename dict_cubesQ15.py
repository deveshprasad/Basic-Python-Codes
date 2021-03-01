# Q15)To print a dictionary whose keys are numbers and values are their cubes:

def dictcubes(dct) :
    for i in range(1,n+1) : 
        dct[i]=i*i*i                               
    print("The dictionary is : ",dct)
n=int(input("Enter a no:"))
dct={}                                          
dictcubes(dct)


 
squares1 = [x**2 for x in range(1,n+1)]
print(squares1) 

a=[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(a)   
