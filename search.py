#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if array[index]==item:
        return index
    else:
        return linear_search_recursive(array,item,index+1)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_recursive(array, item,0,len(array)-1)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here

    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    l = 0
    r = len(array)-1

    while l<=r:
        mid_index = (r+l)//2
        if array[mid_index]==item:
            return mid_index

        elif array[mid_index]<item:
            l = mid_index+1
        else:
            r = mid_index-1
    return None



def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here

    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
    mid_index = (right+left)//2
    if left>right:
        return None
    if array[mid_index]==item:
        return mid_index

    elif array[mid_index]<item:
        return binary_search_recursive(array,item,mid_index+1,right)

    else:
        return binary_search_recursive(array,item,left,mid_index-1)



print(binary_search([1,2,3,4,5,6,7,8,9],8))
print(linear_search_recursive([1,2,3,4,5,6,7,8,9],8))
print(binary_search_recursive([1,2,3,4,5,6,7,8,9],8,0,9))
