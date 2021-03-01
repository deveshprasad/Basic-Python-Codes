# Q19)String operations:
    

#to find length of a string

def find_length(str) :
    length=len(str)
    return length

# To find maximum of three strings
def maximum(str1,str2,str3) :
    maximum_string=max(str1,str2,str3)                             #built in function max
    return maximum_string

#To replace every consecutive character with # except " "
def replace_char(str) :
    str4=""
    i=0
    while i>=0 and i<=(len(str)-1) :
        if str[i]!=" " and str[i+1]!=" " :
            str4=str4+str[i]+"#"                                       #concatenation of strings
            i=i+2
        else :
            str4=str4+str[i]
            i=i+1
    return str4

#To count number of words present in a string
def count_words(str) :
    string1=str.strip()                                                #removing whitespaces from the start and end of string
    count=0
    for i in range(0,len(string1)) :
        if string1[i]==" " :
            count=count+1                                               #counting the number of words
    words=count+1
    return words

def main() :
    ch='y'
    while ch=='y' :
          print()
          print("Enter 1 to find length of a string")                        #menu
          print("Enter 2 to find maximum of three strings")
          print("Enter 3 to replace every consecutive character with #")
          print("Enter 4 to count number of words in it")
          choice=int(input("Enter your choice : "))
          assert choice>=1 and choice<=4
          if choice==1 :
              str=input("Enter a string to find its length : ")
              l=find_length(str)
              print("The length of string is : ",l)
          elif choice==2 :
              print("Enter three strings to find the maximum string")
              str1=input("Enter 1st string : ")
              str2=input("Enter 2nd string : ")
              str3=input("Enter 3rd string : ")
              strng=maximum(str1,str2,str3)
              print("The maximum of three strings is : ",strng)
          elif choice==3 :
              str=input("Enter a string to replace consecutive characters by #")
              strng=replace_char(str)
              print("The string after replacement is :",strng)
          else :
              str=input("Enter a string to count number of words in it :")
              w=count_words(str)
              print("Number of words in string is :",w)
          print()
          print("Do you want to continue : if yes, press 'y' ; otherwise press 'n'")
          ch=input("Do you want to continue : ")
if __name__=="__main__" :
    main()
