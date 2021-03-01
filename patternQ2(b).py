#toprintpattern2(b)
def pattern2() :
    for i in range (1,5,1) :
        for j in range (4,0,-1) :
            if i < j :
                print(" ",end=" ")
        for k in range (1,i+1,1) :
            print(k,end=" ")
        for w in range(i-1,0,-1) :
            print(w,end=" ")
        print()

    for i in range(3,0,-1) :
        for j in range(i-1,3,1) :
            print(" ",end=" ")
        for k in range(1,i+1,1) :
            print(k,end=" ")
        for w in range(i-1,0,-1) :
            print(w,end=" ")
        print()

def main() :
    print("The pattern is :")
    pattern2()

if __name__=="__main__" :
    main()
            
            
