def raisetopower(basenum,powernum):
    result=1
    for index in range(powernum):
        result=result*basenum
    return result
basenum=int(input("enter base : "))
powernum=int(input("enter power : "))

answer=raisetopower(basenum,powernum)
print(answer)