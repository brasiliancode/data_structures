import random


#Busca binaria 

def binary_search(array, item, begin=0, end=None):
    if end is None:
        end = len(array)-1
    if begin <= end:
        m = (begin + end)//2
        if array[m] == item:
            return  m 
        if item < array[m]:
            return binary_search(array, item, begin, m-1)
        else:
            return binary_search(array, item, m+1, end)
    return None


def mergesort(array, begin=0, end=None):
    if end is None:
        end = len(array)
    if (end - begin > 1):
        meio = (end + begin)//2
        mergesort(array, begin, meio)
        mergesort(array, meio, end)
        merge(array, begin, meio, end)

def merge(array, begin, meio, end):
    left = array[begin:meio]
    right = array[meio:end]
    top_left, top_right = 0,0
    for k in range(begin, end):
        if top_left >= len(left):
            array[k] = right[top_right]
            top_right = top_right + 1
        elif top_right >= len(right):
            array[k] = left[top_left]
            top_left = top_left + 1
        elif left[top_left] < right[top_right]:
            array[k] = left[top_left]
            top_left = top_left + 1
        else:
            array[k] = right[top_right]
            top_right = top_right + 1
    


