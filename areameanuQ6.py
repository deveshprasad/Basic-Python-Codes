#Menu included program  to compute area of building
#1)to enter length , breadth, height,
def dim() :
     length=int(input("Enter length of building : "))                  
     assert length>0                        
     breadth=int(input("Enter breadth of building : ") )               
     assert breadth>0                      
     height=int(input("Enter height of building : "))                 
     assert height>0                       
     return length,breadth,height
#to find area of given building    
def area(length,breadth,height) :
    area=length*breadth*height
    return area
def main() :
    ch='y'
    while ch=='y' :
          print("Enter 1 to input length,breadth and height")
          print("Enter 2 to compute area")
          choice=int(input("Enter your choice : "))
          assert choice>=1 and choice<=2
          if choice==1 :
             dim()
          else :
             l,b,h= dim()
             area1=area(l,b,h)
             print("The area of builing is : ",area1)
          print("You want to compute area of another building? ")
          print("If yes , type y ")
          print("If no , type n ")
          ch=input("Enter your choice")
if __name__=="__main__" :
   main()
