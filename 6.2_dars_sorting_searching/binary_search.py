# Python3 code to implement iterative Binary
# Search.
from random import randint

# It returns location of x in given array arr
def binarySearch(arr, l, r, x):
    while l <= r:

        mid = l + (r - l) // 2
        print(f'{l=},\t{mid=}, \t{r=}')   # l, r -> index raqami, mid= l ga qoshiladi r-l va 2 ga bolinadi va butun qism olinadi

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element
    # was not present
    return -1


# Driver Code
if __name__ == '__main__':
    arr = [randint(10, 100) for i in range(int(input('n = ')))]
    arr.sort()
    print(arr)
    x = int(input('Search: '))
    print(arr.index(x))


    # Function call
    result = binarySearch(arr, 0, len(arr) - 1, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")