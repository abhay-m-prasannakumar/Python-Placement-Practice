inputstr=input("Enter string:")
k=int(input("Enetr k:"))
result=0
i,j=0,0
while i<=j and i<len(inputstr) and j<len(inputstr):
    if len(set(inputstr[i:j+1])) ==k:
        result=max(result,len(inputstr[i:j+1]))
        j +=1
    elif (len(set(inputstr[i:j+1]))<k):
         j+=1
    else:
        i+=1
print(result)