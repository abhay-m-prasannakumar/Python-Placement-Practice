def getways(amt,coins):
    dp=[0]*(amt+1)
    dp[0]=1
    for coin in coins:
        for x in range(coin,amt+1):
            dp[x]+=dp[x-coin]
    print(dp[amt])
getways(10,[1,2,3,4,5])