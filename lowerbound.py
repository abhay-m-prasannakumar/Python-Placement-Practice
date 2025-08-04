def lower_bound(nums, x):
    low = 0
    high = len(nums)
    
    while low < high:
        mid = (low + high) // 2
        if nums[mid] <x:
            low = mid + 1
        else:
            high = mid  # nums[mid] >= x, possible answer
    return low  # Index of first element >= x, or len(nums) if not found

# Example usage
nums = list(map(int, input("Enter sorted array: ").split()))
x = int(input("Enter value to find lower bound: "))

index = lower_bound(nums, x)
print(f"Lower bound index: {index}")
