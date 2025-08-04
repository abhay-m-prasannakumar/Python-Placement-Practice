x=input("Enter string:")
y=0
for char in x:
    if char == '{':
        y=y+1
    elif char =='}':
        y=y-1
    if y<0:
        break
if y==0:
    print("Matching")
else:
    print("Not Matching")
  