#Q20) Write a Python program to perform the following using list:
#a. Check if all elements in list are numbers or not
#b. If it is a numeric list, then count number of odd values in it
#c. If list contains all Strings, then display largest String in the list
#d. Display list in reverse form
#e. Find a specified element in list
f. Remove the specified element
def check_list(lst) :
    n=1
    ch=type(n)
    f=0
    for i in range(0,len(lst)) :
        if type(lst[i])!=ch :
            f=1
            break
    return f,lst
def count_odd(lst) :
    count=0
    for i in range(0,len(lst)) :
        if lst[i]%2==1 :
            count=count+1
    return count
def check_string(lst) :
    c='b'
    ch1=type(c)
    for i in range(0,len(lst)) :
        f=0
        if type(lst[i])!=ch1 :
            f=1
            break
    if f==1 :
        print("All elements of list are not of string type, so cannot compare them.")
        return None
    else :
        maximum=lst[0]
        print(maximum)
        for i in range(1,len(lst)) :
            if maximum<lst[i] :
                maximum=lst[i]
        return maximum
def reverse_list(lst) :
    rev=lst.reverse()
    return rev
def find(lst,element) :
    c=lst.count(element)
    if c==0 :
        print("The element is not present.")
    else :
        i=lst.index(element)
    return i
def remove_element(lst,element) :
    c=lst.count(element)
    r=0
    while c!=r :
        lst.remove(element)
        r=r+1
    return lst
    
def main() :
    ch='y'
    while ch=='y' :
          lst=eval(input("Enter the elements of list"))
          print()
          print("Enter 1 to check if all elements of list are numeric or not")
          print("Enter 2 to count odd vaues in list, if it is a numeric list")
          print("Enter 3 to print maximum string,if all elements are string")
          print("Enter 4 to display list in reverse form")
          print("Enter 5 to find a specified element")
          print("Enter 6 to remove a specified element")
          choice=int(input("Enter your choice : "))
          assert choice>=1 and choice<=6
          if choice==1 :
              f1,lst1=check_list(lst)
              if f1==0 :
                  print("It is a numeric list.")
              else :
                  print("All the elements of list are not numeric.")
          elif choice==2 :
               if f1==0 :
                   c1=count_odd(lst)
                   print("The number of odd values are :",c1)
               else :
                   print("All the values in list are not numeric")
          elif choice==3 :
               str=check_list(lst)
               if str!=None :
                   print("The maximum string in the list is :",str)
          elif choice==4  :
               rev1=reverse_list(lst)
               print("The elements in reverse order are :",rev1)
          elif choice==5 :
               print("Specify the type of element you want to find")
               print("if type s string,enter s ; if type is integer, enter i")
               ty=input("Enter type")
               if ty=='s' :
                   element=input("Enter element")
               else :
                    element=int(input("Enter element"))
                
               c1=lst.count(element)
               if c1==0 :
                    print("Element is not present")
               else :
                    i=index.lst(element)
                    print("The element is present at index",i)
          elif choice==6 :
               print("Specify the type of element you want to find")
               print("if type s string,enter s ; if type is integer, enter i")
               ty=input("Enter type")
               if ty=='s' :
                   element=input("Enter element")
               else :
                   element=int(input("Enter element"))
                
               lst2=remove_element(lst,element)
               print("The list after removing element is :",lst2)
              
          print("If you want to continue,enter 'y' ; else enter 'n'")
          ch=input("Do u want to continue")
    
if __name__=="__main__" :
    main()
        
