# -*- coding:utf-8 -*-
import sys


def partition(array, start, end):
    part_key = array[start]
    low = start
    high = end
    while low<high:
        while low<high and part_key <= array[high]:
            high -=1
        array[low] = array[high]
        while low < high and part_key >= array[low]:
            low += 1
        array[high] = array[low]
    array[low] = part_key
    return low


def quick_sort(array, low, high):
    if low < high:
        part_id = partition(array, low, high)
        quick_sort(array, low, part_id-1)
        quick_sort(array, part_id+1, high)


def new_partition(array, start, end):
    key = array[start]
    low = start
    high = end
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        array[low] = array[high]
        while low < high and array[low] <= key:
            low += 1
        array[high] = array[low]
    array[low] = key
    return low


def new_quick_sort(array, start, end):
    if start < end:
        pos = new_partition(array, start, end)
        new_quick_sort(array, start, pos-1)
        new_partition(array, pos+1, end)
    else:
        return


if __name__ == "__main__":
    test_array = [2, 5, 1, 7, 9, 4]
    # print partition(test_array, 0, len(test_array)-1)
    # print test_array

    new_quick_sort(test_array, 0, len(test_array)-1)
    print test_array
