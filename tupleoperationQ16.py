#Tuple Operation:

#To print half values of the tuple in one line and the other half in next line

def halfprint(t1) :                                   
    length=len(t1)
    print("The tuple is : ",end=" ")
    for i in range (0,(length//2)) :
        print(t1[i],end=" ")
    print()
    for i in range((length//2),length) :
        print(t1[i],end=" ")

#To find even values and storing it in another tuple
def eventuple(t1) :
    t3=()
    for i in range(0,len(t1)) :
        if t1[i] % 2 == 0 :
            t3=t3+(t1[i],)
    print()
    print("The tuple containing even values of ",t1,"is : ",t3)

 # to concatenate another tuple to existing tuple
def concatenate(t1) :
    t2=(11,13,15)
    t3=t1+t2
    print("The tuple t1 after concatination is : ",t3)
    return t3

# To find maximum value of the tuple
def maximum(t4) :
    maxv=max(t4)
    print("The maximum value in this tuple is : ",maxv)

#To find minimum value of the tuple
def minimum(t4) :
    minv=min(t4)
    print("The minimum value in this tuple is : ",minv)

def main() :
    t1=(1,2,5,7,9,2,4,6,8,10)
    print("The various operations on",t1," is : ")
    halfprint(t1)
    eventuple(t1)
    t4=concatenate(t1)
    maximum(t4)
    minimum(t4)
if __name__=="__main__" :
    main()
