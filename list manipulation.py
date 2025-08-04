n=int(input("Enter n;"))
k=int(input("Enter nno of queries:"))
q=[]
for _ in range(k):
    q.append(list(map(int,input().rstrip().split(' '))))
arr=[0]*(n+1)
for start,end,value in q:
    arr[start] += value
    arr[end+1] -= value
sum=0
result=0
for i in arr:
    sum +=i
    result=max(result,sum)

print(result)