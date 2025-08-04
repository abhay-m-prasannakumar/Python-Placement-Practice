def purchase(stockdata):
    minsofar=stockdata[0]
    Forward= [0]
    for i in stockdata:
        if(i<minsofar):
            minsofar=i
        Forward.append(max(i-minsofar,Forward[-1]))
    maxprofit=max(Forward)
    print(Forward)
    maxsofar=-float('inf')
    for i in range(len(stockdata)-1,-1,-1):
        maxsofar=max(maxsofar,stockdata[i])
        maxprofit=max(maxprofit,maxsofar-stockdata[i]+Forward[i])
    return(maxprofit)
list1=[310,337,275,260,270,290,230,255,250]
list2=[12,11,13,9,12,8,14,13,15]
x=purchase(list1)
y=purchase(list2)
print(x)
print(y)
        