 #Implementation of class
#Class definition to find area and perimeter of rectangle

class Rectangle :
    def ___init__(self,length,breadth) :                  #constructor
        self.length=length
        self.breadth=breadth
    def perimeter(self,length,breadth) :                  #to compute perimeter
        peri=2*(length+breadth)
        return peri
    def area(self,length,breadth) :                       #to compute area
        area1=length*breadth
        return area1
    def __del__(self) :                                    #destructor
        print("The object is deleted.")
def main() :
    length=int(input("Enter the length of rectangle : "))
    breadth=int(input("Enter the breadth of rectangle : "))
    R= Rectangle ()                                      # an instance is created
    print("Enter 1 to compute area of rectangle")
    print("Enter 2 to compute perimeter of rectangle")
    ch=int(input("Enter your choice : "))
    assert ch>=1 and ch<=2
    if ch==1 :
        area2=R.area(length,breadth)
        print("The area of rectangle is :",area2)
    else :
        perim=R.perimeter(length,breadth)
        print("The perimeter of rectangle is :",perim)
if __name__=="__main__" :
    main()
    
               
