# Q17)To check any element of list is repeated or not

def check_duplicates(lst) :                                        
    for i in range(0,len(lst)) :
        if lst.count(lst[i])>1 :
            cnt=lst.count(lst[i])                                   
            return True,cnt
        else :
            return False,0
def main() :
    lst=eval(input("Enter the elements of list enclosed in [] brackets "))
    f_check,frequency=check_duplicates(lst)
    if f_check == True :
        print("There is duplicate element in lst whose frequency is : ",frequency)

    else :
        print("There are no duplicates elements in list.")
if __name__=="__main__" :
    main()
