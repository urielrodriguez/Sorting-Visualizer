import random
from random import randrange

def numbers(last, length):
    nums = []
    count = 0
    while count < length:
        num = randrange(last)
        nums.append(num)
        count += 1
    return nums

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
    
def countingSort(arr, last):
    sort = [0] * len(arr)
    i = indexList(last, arr)
    for a in arr:
        sort[i[a]] = a
        i[a] += 1
    return sort
    
nums = numbers(5, 10)
countingSort(nums, 5)