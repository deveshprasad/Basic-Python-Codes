counts=dict()
line=input("Enter a line ")
words=line.split()
print('WORD=',words)
for word in words:
    counts[word]=counts.get(word,0)+1
print("COUNTS=",counts)    


