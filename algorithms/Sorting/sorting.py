# question path
# Algorithms/Sorting/Big Sorting
def bigSorting(arr):
    # Complete this function
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    arr.sort()

    return num

def bigSorting(arr):
	tmp = map(int, arr)
	tmp.sort()
	return tmp

def bigSorting(arr):
	tmp = [int(num) for num in arr]
	tmp.sort()
	return tmp

# Insertion sort 1
def insertionSort1(n, arr):
    # Complete this function
    i = n - 2
    tmp = arr[-1]
    while i>=0 and arr[i]> tmp:
        arr[i + 1] = arr[i]
        i-=1
        print " ".join(map(str, arr))

    arr[i+1] = tmp
    print " ".join(map(str, arr))

# Insertion sort 2
def insertionSort2(n, arr):
    # Complete this function
    if n < 2:
        return arr
    for i in range(1, len(arr)):
        j = i - 1
        tmp = arr[i]
        while j >= 0 and arr[j] > tmp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = tmp
        print " ".join(map(str, arr))
    return arr # after switch

# Running Time of Algorithms
def runningTime(arr):
    # Complete this function
    if len(arr) < 2:
        return arr
    res = 0
    for i in range(1, len(arr)):
        j = i - 1
        tmp = arr[i]
        while j >= 0 and arr[j] > tmp:
            arr[j + 1] = arr[j]
            j -= 1
            res += 1
        arr[j + 1] = tmp
    return res

# Quick Sort 1- Partition
def quickSort(arr):
    # Complete this function
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return left + [pivot] + right

# Quick Sort 2 - Sorting
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    left, right = [], []
    pivot = arr[0]
    for num in arr[1:]:
        if num < arr[0]:
            left.append(num)
        else:
            right.append(num)
    res = quick_sort(left) + [pivot] + quick_sort(right)
    print ' '.join(map(str, res))
    return res