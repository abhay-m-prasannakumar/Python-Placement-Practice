x=input("Enter a string1:")
y=input("Enter a string2:")
a=[]
b=[]
for i in x:
    a.append(i)
for i in y:
    b.append(i)
a.sort()
b.sort()
if a==b:
    print("Anagram")
else:
    print("Not Anagram")