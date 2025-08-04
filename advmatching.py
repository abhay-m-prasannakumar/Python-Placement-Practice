inpStr=input()
stack=[]
flag=True
for i in inpStr:
    if i=='{':
        stack.append(i)
    elif i=='[':
        stack.append(i)
    elif i=='(':
        stack.append(i)
    elif i==')' and len(stack)!=0 and stack[-1]=='(':
        stack.pop()
    elif i=='}' and len(stack)!=0 and stack[-1]=='{':
        stack.pop()
    elif i==']' and len(stack)!=0 and stack[-1]=='[':
        stack.pop()
    else:
        flag=False
        break
if len(stack)==0 and flag:
    print("Matching")
else:
    print("Not Matching")

