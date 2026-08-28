import numpy as np


def move_max_rec(arr: np.ndarray[int]) -> np.ndarray[int]:
    """
Sorts an array of integers in ascending order using the Bubble Sort algorithm.

Parameters
----------
arr : numpy.ndarray[int]
    Input array.

Returns
-------
numpy.ndarray[int]
    Sorted array.

"""
    # Base case: empty array or single element
    if len(arr) <= 1:
        return arr

    # Compare adjacent elements and swap if necessary
    if arr[0] > arr[1]:
        arr[0], arr[1] = arr[1], arr[0]

    # Recursively call the function with the remaining array (excluding the first element)
    return np.concatenate([[arr[0]], move_max_rec(arr[1:])])



def is_substring(big_string: str, sub_string: str) -> bool:
    """
    Checks if sub_string is a sub-string of big_string using head-tail recursion.

    Parameters
    ----------
    big_string : str
        The larger string.
    sub_string : str
        The potential sub-string.

    Returns
    -------
    bool
        True if sub_string is a sub-string of big_string, False otherwise.

    """
    # Base case: if the sub_string is an empty string, it is always a sub-string
    if not sub_string:
        return True

    # Base case: if the big_string is empty and sub_string is not, it's not a sub-string
    if not big_string:
        return False

    # Check if the current head of big_string matches the start of sub_string
    if big_string.startswith(sub_string):
        return True

    # Recursively call the function with the tail of big_string
    return is_substring(big_string[1:], sub_string)

def find_combinations(input: list, target: int) -> int:
    """
    Finds the number of different ways to reach the target by summing a set of numbers in the list.

    Parameters
    ----------
    input_list : list
        The list of numbers.
    target : int
        The target sum.

    Returns
    -------
    int
        The number of different ways to reach the target.

    """
    # Base case: if the target is 0, there is one valid combination (empty set)
    if target == 0:
        return 1

    # Base case: if the target is negative or the list is empty, no valid combinations
    if target < 0 or not input:
        return 0

    # Recursive case: consider the current number in the list or skip it
    with_current = find_combinations(input[1:], target - input[0])
    without_current = find_combinations(input[1:], target)

    # Sum the results of the two recursive calls
    return with_current + without_current

def insert_into_sorted(sorted_arr: np.ndarray[int], new_value: int, index: int) -> np.ndarray[int]:
    """
    Inserts a new value into a sorted array at the specified index.

    Parameters
    ----------
    sorted_arr : np.ndarray[int]
        The sorted array.
    new_value : int
        The value to insert.
    index : int
        The index at which to insert the new value.

    Returns
    -------
    np.ndarray[int]
        The sorted array with the new value inserted.

    """
    return np.concatenate((sorted_arr[:index], np.array([new_value]), sorted_arr[index:]))

def sort_array(arr: np.ndarray[int]) -> np.ndarray[int]:
    """
    Sorts an array in ascending order using recursion.

    Parameters
    ----------
    arr : np.ndarray[int]
        The array to be sorted.

    Returns
    -------
    np.ndarray[int]
        The sorted array.

    """
    # Base case: if the array has 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr

    # Recursive case: sort the tail of the array
    sorted_tail = sort_array(arr[1:])

    # Find the index to insert the head into the sorted tail
    i = 0
    while arr[0] > sorted_tail[i]:
        i += 1
        if i == sorted_tail.shape[0]:
            break

    # Insert the head into the sorted tail and return the result
    return insert_into_sorted(sorted_tail, arr[0], i)
