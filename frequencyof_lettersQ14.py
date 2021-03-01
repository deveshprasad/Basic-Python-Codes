# To find out the frequency of each letter in string and using a dictionary

def frequency(str) :
    dct={}                                         
    str1=str.split(" ")
    for i in str1 :                          
        str2=i
        for j in str2 :                                 
            dct[j]=dct.get(j,0) +1
str=input("Enter a string to find frequency of each letter : ")
dct1=frequency(str)
print("The frequency of each letter is :",dct1)



