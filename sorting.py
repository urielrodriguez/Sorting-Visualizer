import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation
import random
from random import randrange

#######################################
# SORTING FUNCTIONS
#######################################

def selectionSort(arr, comparisons, swaps):
    start = 0
    while (start < len(arr)):
        smallest = start
        for i in range(start, len(arr)):
            if (arr[i] < arr[smallest]):
                smallest = i
            yield arr
            comparisons[0] += 1
        swap(arr, start, smallest, swaps)
        start += 1
        yield arr

def mergeSort(arr, start, end, comparisons):
    if start < end:
        mid = start + ((end - start + 1) // 2) - 1
        yield from mergeSort(arr, start, mid, comparisons)
        yield from mergeSort(arr, mid+1, end, comparisons)
        yield from merge(arr, start, mid, end, comparisons)
        yield arr

def insertionSort(arr, comparisons, swaps):
    for i in range(len(arr)):
        index = i
        while (index > 0 and (arr[index] < arr[index-1])):
            comparisons[0] += 1
            swap(arr, index, index-1, swaps)
            index -= 1
            yield arr

def heapSort(arr, comparisons, swaps):
    heap = heapify(arr)
    arr = heap.toArr()
    srted = []
    while (heap.size > 0):
        largest = heap.removeLargest()
        comparisons[0] = heap.comparisons
        swaps[0] = heap.swaps
        srted.insert(0, largest)
        arr = heap.toArr()
        arr = arr + srted
        yield arr
    yield arr

def quickSort(arr, start, end, comparisons, swaps):
    if start >= end:
        return
    
    tStart = start
    tEnd = end
    pivot = start
    tStart += 1
    while tStart <= tEnd:
        if arr[tStart] > arr[pivot] and arr[tEnd] < arr[pivot]:
            swap(arr, tStart, tEnd, swaps)
        if arr[tStart] < arr[pivot]:
            tStart += 1
        if arr[tEnd] > arr[pivot]:
            tEnd -= 1
        yield arr
        comparisons[0] += 3
    swap(arr, pivot, tEnd, swaps)
    pivot = tEnd
    yield arr
    
    yield from quickSort(arr, start, pivot-1, comparisons, swaps)
    yield from quickSort(arr, pivot+1, end, comparisons, swaps)
    yield arr

def countingSort(arr, last):
    sort = [0] * len(arr)
    i = indexList(last, arr)
    for a in arr:
        sort[i[a]] = a
        i[a] += 1
        yield sort
    yield sort

#######################################
# HELPER FUNCTIONS
#######################################

# Used in Selection Sort, Insertion Sort, & Quick Sort
def swap(arr, x, y, swaps):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp 
    swaps[0] += 1

# Used in Merge Sort
def merge(arr, start, mid, end, comparisons):
    tempArr = []
    left = start
    right = mid + 1
    while left <= mid and right <= end:
        if arr[left] <= arr[right]:
            tempArr.append(arr[left])
            left += 1
        else:
            tempArr.append(arr[right])
            right += 1
        comparisons[0] += 1
    while left <= mid:
        tempArr.append(arr[left])
        left += 1
    while right <= end:
        tempArr.append(arr[right])
        right += 1
    for i in range(start, end+1):
        arr[i] = tempArr[i-start]
        yield arr

# Used in Heap Sort
def heapify(arr):
    mh = MaxHeap()
    for val in arr:
        mh.add(val)
    return mh

# Used in Counting Sort
def indexList(last, n):
    indices = [0] * (last + 1)
    for num in n:
        indices[num] += 1
    sum = 0
    for i in range(last + 1):
        sum += indices[i]
        indices[i] = sum
    temp = indices[0]
    for i in range(last, 0, -1):
        indices[i] = indices[i-1]
    indices[0] = 0
    return indices

# Used for Counting Sort number generation
def numbers(last, length):
    nums = []
    count = 0
    while count < length:
        num = randrange(1, last)
        nums.append(num)
        count += 1
    return nums

#######################################
# MAX HEAP IMPLEMENTATION
#######################################

class MaxHeap:
    def __init__(self):
        self.size = 0
        self.values = ['x']
        self.comparisons = 0
        self.swaps = 0
    def add(self, value):
        self.values.append(value)
        self.size += 1
        self.swim(self.size)
        
    def removeLargest(self):
        largest = self.getLargest()
        self.swap(1, self.size)
        del self.values[-1]
        self.size -= 1
        self.sink(1)
        return largest
        
    def getLargest(self):
        return self.values[1]
    
    def swim(self, i):
        if i == 1:
            return
        if self.values[self.parent(i)] < self.values[i]:
            self.swap(i, self.parent(i))
            self.swim(self.parent(i))
        self.comparisons += 1
            
    def sink(self, i):
        if self.leftChild(i) > self.size:
            return
        if self.rightChild(i) > self.size:
            return
        if (self.values[self.leftChild(i)] > self.values[i] or self.values[self.rightChild(i)] > self.values[i]):
            if self.rightChild(i) > self.size or self.values[self.leftChild(i)] > self.values[self.rightChild(i)]:
                self.swap(i, self.leftChild(i))
                self.sink(self.leftChild(i))
            else:
                self.swap(i, self.rightChild(i))
                self.sink(self.rightChild(i))
            self.comparisons += 1
        
    def swap(self, i1, i2):
        temp = self.values[i1]
        self.values[i1] = self.values[i2]
        self.values[i2] = temp
        self.swaps += 1
        
    def parent(self, i):
        return i // 2
        
    def leftChild(self, i):
        return i * 2
        
    def rightChild(self, i):
        return i * 2 + 1

    def toArr(self):
        arr = []
        for val in self.values:
            arr.append(val)
        del arr[0]
        return arr

#######################################
# DATA
####################################### 

comparisons = [0]
swaps = [0]
operations = [0]

#######################################
# USER INPUT HANDLER
#######################################  
     
sort = int(input('Select Sorting Algorithm\n(1)Selection Sort\n(2)Merge Sort\n(3)Insertion Sort\n(4)Heap Sort\n(5)Quick Sort\n(6)Counting Sort\n'))
units = int(input('Number of Data Points to Sort: '))

if sort == 6:
    maxRange = units//2
    rang = int(input('Specify the Range of the Data Points (<={}): '.format(maxRange)))
    valsCountSort = numbers(rang, units)

values = [x + 1 for x in range(units)]
random.shuffle(values)

if sort == 1:
    generator = selectionSort(values, comparisons, swaps)
    title = 'Selection Sort'
elif sort == 2: 
    generator = mergeSort(values, 0, units-1, comparisons) 
    title = 'Merge Sort'
elif sort == 3:
    generator = insertionSort(values, comparisons, swaps)
    title = 'Insertion Sort'
elif sort == 4:
    generator = heapSort(values, comparisons, swaps)
    title = 'Heap Sort'
elif sort == 5:
    generator = quickSort(values, 0, units-1, comparisons, swaps)
    title = 'Quick Sort'
elif sort == 6:
    generator = countingSort(valsCountSort, rang)
    title = 'Counting Sort'


#######################################
# VISUALIZER
#######################################

fig, ax = plt.subplots()
bars = ax.bar(range(len(values)), values, color='c', edgecolor='k')
ax.set_title(title)
ax.set_xlim(0, units)
ax.set_ylim(0, 1.1*units)
ax.set_xlabel('Data Points: {} - Comparisons: {} - Swaps: {} - Operations: {}'.format(units, comparisons[0], swaps[0], operations[0]))

def update(vals, rects, operations):
    for val, rect in zip(vals, rects):
        rect.set_height(val)
    operations[0] += 1
    ax.set_xlabel('Data Points: {} - Comparisons: {} - Swaps: {} - Operations: {}'.format(units, comparisons[0], swaps[0], operations[0]))
    
animation = FuncAnimation(fig, func=update, frames=generator, fargs=(bars, operations), interval=200, repeat=False)
        
plt.show()


