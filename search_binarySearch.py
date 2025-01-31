#array must be already sorted.

def binary_search(arr,ele):
    # First and last index values
    first = 0
    last = len(arr) - 1
    found = False
    while first <= last and not found:
        mid = (first+last)/2 # or // for Python 3
        
        # Match found
        if arr[mid] == ele:
            found = True
        
        # Set new midpoints up or down depending on comparison
        else:
            # Set down
            if ele < arr[mid]:
                last = mid -1
            # Set up 
            else:
                first = mid + 1
                
    return found

def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) -1)


def binarySearchHelper(array, target, left, right):
    while left <= right:
        middle = (left + right)//2
        potentialMatch = array[middle]
        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            right = middle - 1
        else:
            left = middle + 1
    return -1