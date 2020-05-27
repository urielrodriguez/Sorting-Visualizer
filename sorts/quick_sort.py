def partition(arr, start, end):
    pivot = start
    start += 1
    while start <= end:
        if arr[start] > arr[pivot] and arr[end] < arr[pivot]:
            swap(arr, start, end)
        if arr[start] < arr[pivot]:
            start += 1
        if arr[end] > arr[pivot]:
            end -= 1
    swap(arr, pivot, end)
    return end

def quickSort(arr, start, end):
    if start >= end:
        return
    pivot = partition(arr, start, end)
    quickSort(arr, start, pivot-1)
    quickSort(arr, pivot+1, end)