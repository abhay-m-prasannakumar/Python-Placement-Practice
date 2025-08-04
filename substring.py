s=input("Enter string:")
k=int(input("Enter K:"))
result=0
for i in range(len(s)):
    for j in range(i,len(s)+1):
        if(len(set(s[i:j]))==k):
            result=max(result,len(s[i:j]))
print(result)
    