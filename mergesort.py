
def merge(arr, start, mid, end):
    numL = mid - start + 1
    numR = end - mid
    leftArr = arr[start:mid+1]
    rightArr = arr[mid+1:end+1]
    
    iterOnarr = start
    i, j = 0, 0
    
    # Merging the two halves
    while i < numL and j < numR:
        if leftArr[i] < rightArr[j]:
            arr[iterOnarr] = leftArr[i]
            i += 1
        else:
            arr[iterOnarr] = rightArr[j]
            j += 1
        iterOnarr += 1
    
    # Copy remaining elements of leftArr if any
    while i < numL:
        arr[iterOnarr] = leftArr[i]
        i += 1
        iterOnarr += 1
    
    # Copy remaining elements of rightArr if any
    while j < numR:
        arr[iterOnarr] = rightArr[j]
        j += 1
        iterOnarr += 1


def mergeSort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        mergeSort(arr, start, mid)
        mergeSort(arr, mid + 1, end)
        merge(arr, start, mid, end)


# Input and execution
inputlist = list(map(int, input().rstrip().split()))
mergeSort(inputlist, 0, len(inputlist) - 1)
print(inputlist)
