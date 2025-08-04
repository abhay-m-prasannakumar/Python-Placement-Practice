inputstr=input("Enter string:")
valley=0
x=0
for i in inputstr:
    if i=="U":
        x +=1
        if x==0:
            valley +=1
    elif i == "D": 
        x -=1
print((valley))    
