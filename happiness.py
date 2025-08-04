n, m = map(int, input().split())
arr=[]
for i in range(n):
    arr.append(int(input()))
A=[],B=[]
for _ in range(m):
    A.append(int(input()))
for _ in range(m):
    B.append(int(input()))
sum=0
for i in arr:
    if i in A:
        sum +=1
    elif i in B:
        sum -=1
print(sum)