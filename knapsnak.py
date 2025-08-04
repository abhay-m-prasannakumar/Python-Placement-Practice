def knapsack(val, wt, W):
    n = len(val)
    # Initialize DP table with 0s
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    # Build table dp[][] in bottom up manner
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i-1] <= w:
                # Include the item or not
                dp[i][w] = max(
                    val[i-1] + dp[i-1][w - wt[i-1]],  # take
                    dp[i-1][w]                        # don't take
                )
            else:
                # Can't include the item
                dp[i][w] = dp[i-1][w]
    
    # Print the DP table
    print("DP Table:")
    for row in dp:
        print(row)
    
    # Return the maximum value achievable
    return dp[n][W]

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value = knapsack(values, weights, capacity)
print("Maximum value in Knapsack:", max_value)
