#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests
    if index >= len(array):
        return None # Not found
    elif array[index] is item:
        return index # Found
    else:
        return linear_search_recursive(array, item, index + 1)

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    left = 0
    right = len(array) - 1
    array.sort()
    return binary_search_recursive(array, item, left, right)


def binary_search_iterative(array, item):
    array.sort()
    left = 0
    right = len(array) - 1

    while(left <= right):
        midpoint = (left + right) // 2
        print('midpoint: ', midpoint)

        if item == array[midpoint]:
            return midpoint
        elif item > array[midpoint]:
            left = midpoint + 1
        else:
            right = midpoint - 1
    return None


def binary_search_recursive(array, item, left=None, right=None):
    if left is None and right is None:
        left = 0
        right = len(array) - 1
    midpoint = (left + right) // 2

    if item is array[midpoint]:
        return midpoint #found
    
    if left > right:
        return None

    elif item > array[midpoint]:
        left = midpoint + 1
    
    else: 
        right = midpoint - 1
        return binary_search_recursive(array, item, left, right)
        