def heapSort(arr):
    heap = heapify(arr)
    arr = heap.toArr()
    srted = []
    while (heap.size > 0):
        largest = heap.removeLargest()
        srted.insert(0, largest)
        arr = heap.toArr()
        arr = arr + srted

def heapify(arr):
    mh = MaxHeap()
    for val in arr:
        mh.add(val)
    return mh

class MaxHeap:
    def __init__(self):
        self.size = 0
        self.values = ['x']
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
        
    def swap(self, i1, i2):
        temp = self.values[i1]
        self.values[i1] = self.values[i2]
        self.values[i2] = temp
        
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

