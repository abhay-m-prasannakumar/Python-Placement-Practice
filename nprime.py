n=int(input("ENter:"))
count=0
for i in range(2,n+1):
    for j in range(1,n+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i)
    count=0

    # OR
#def isprime(i):
#for j in range(2,int(i**0.5)+1):
  #  if i%j ==0:
 #      return (False)
#return (True)
#for i in range(2,n+1):
#if isprime(i):
#print(i,end= ' ')
