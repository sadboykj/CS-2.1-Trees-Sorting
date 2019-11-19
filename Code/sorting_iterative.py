#!python

import os
import time

def is_sorted(items):
    """
    Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) - iterates through all elements in array  worst case
    Memory usage: O(1) - no new memory used
    """
    for i in range(0, len(items) - 1):
        if items[i] > items[i+1]:
            return False
    return True

def bubble_sort(items):
    """
    Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: O(n^2) - for loop within a while loop
    Memory usage: O(logn) - new slice made for every for loop iteration, every slice gets smaller
    """
    size = len(items)
    print(f"size: {size}")

    if is_sorted(items):
        print(f"list already sorted")
        return
    
    while size > 0:
        # i for index
        # e for array[element]
        for i in range(0, size):
            # check if last in list
            if i == size - 1:
                print(f"index {i}: {items[i]} is set!")
                break
            # checks if neighbor is bigger
            print(f"checking index {i+1}, val {items[i+1]}")
            if items[i] > items[i+1]:
                print(f"switching {i}: {items[i]} and {i+1}: {items[i+1]}")
                items[i], items[i+1] = items[i+1], items[i]
                print(items)
        # biggest element has been moved to end
        size -= 1

def selection_sort(items):
    """
    Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: ??? Why and under what conditions?
    Memory usage: ??? Why and under what conditions?
    """
    if is_sorted(items):
        print(f"list already sorted")
        return

    # Repeat until all items are in sorted order
    while size > 0:
        # i for index
        # e for array[element]
        for i in range(0, size):
            # Find minimum item in unsorted items
            print(f"checking index {i+1}, val {items[i+1]}")
            # minimum index
            min_i, min
            min_v = min(min_val, arr[i])
                print(f"switching {i}: {arr[i]} and {i+1}: {arr[i+1]}")
                arr[i], arr[i+1] = arr[i+1], arr[i]
                print(arr)
        # biggest element has been moved to end
        size -= 1
    # TODO: Swap it with first unsorted item


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items

if __name__ == "__main__":

    arr = [1, 6, 7, 3, 5]
    print(f"array: {arr}")
    print(f"is sorted: {is_sorted(arr)}")
    if is_sorted(arr):
        print(f"array is already sorted")
    else:
        print("b for bubble sort")
        print("s for selection sort")
        method = input("method: ")
        if method == "b":
            print(f"Method: Bubble Sort")
            print(f"Sorting...")
            bubble_sort(arr)
            print(f"Done")
            print(f"array: {arr}")
        else:
            print("method not found")

    

