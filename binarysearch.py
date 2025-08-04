def binary_search(arr, target):
    # Define the left and right pointers
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Calculate the middle index
        
        # Check if the target is at the middle
        if arr[mid] == target:
            return mid
        
        # If the target is smaller than mid, search the left half
        elif arr[mid] > target:
            right = mid - 1
        
        # If the target is larger than mid, search the right half
        else:
            left = mid + 1
    
    # Target not found
    return -1

# Example usage:
arr = []
n=int(input("Enter no elements in list:"))
for i in range(n):
    arr.append(int(input())) 
target = int(input("Enter target value:"))
result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
