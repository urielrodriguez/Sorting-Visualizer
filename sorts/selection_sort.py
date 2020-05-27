def selectionSort(arr):
    start = 0
    while (start < len(arr)):
        smallest = start
        for i in range(start, len(arr)):
            if (arr[i] < arr[smallest]):
                smallest = i
        swap(arr, start, smallest)
        start += 1
    return arr
        
def swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp