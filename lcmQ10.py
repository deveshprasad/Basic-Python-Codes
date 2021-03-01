#lcm
a = int(input(" Please Enter the First Value a: "))
b = int(input(" Please Enter the Second Value b: "))

if(a > b):
    maximum = a
else:
    maximum = b

while(True):
    if(maximum % a == 0 and maximum % b == 0):
        print("LCM=",maximum)
        break;
    maximum = maximum + 1
    
print('CODE2')

def lcm(a,b):
    
    if(a > b):
        maximum = a
    else:
        maximum = b

    while(True):
        if(maximum % a == 0 and maximum % b == 0):
            
            break;
        maximum = maximum + 1
    return maximum
a = int(input(" Please Enter the First Value a: "))
b = int(input(" Please Enter the Second Value b: "))
LCM=lcm(a,b)
print("LCM=",LCM)


    