import numpy as np

def sum_even_rec(n : int) -> int: 
    """
        Implement the function sum_even_rec to take an integer n as a parameter and return the sum of all the even numbers from 0 to n. 
        Think of the following three question before starting the implementation : 
            - What is the base case?
            The base case is when n becomes 0 because you want to stop the recursion when you reach the lower limit.
            - What argument is passed to the recursive function call?
            The argument passed to the recursive function call is n - 2 because you want to move towards the base case by reducing n for each recursive call.
            - How does this argument become closer to the base case?
            In each recursive call, you reduce n by 2, making the argument closer to the base case of n == 0.
        Modify the base condition, the recursive condition and the returns of the program.
        Rewrite the docstring
    """
    """
    Calculates the sum of all even numbers from 0 to n using recursion.

    Parameters
    ----------
    n : int
        The upper limit for the summation.

    Returns
    -------
    int
        The sum of even numbers from 0 to n.
    """
    # Base case
    if n == 0:
        return 0
    
    # Recursive case
    elif n % 2 == 0:
        return n + sum_even_rec(n - 2)
    
    else:
        return sum_even_rec(n - 1)

def array_product_rec(numbers : np.ndarray[int]) -> int: 
    """
    Calculates the product of all numbers in the array using recursion.

    Parameters
    ----------
    numbers : np.ndarray[int]
        The array of integers.

    Returns
    -------
    int
        The product of all numbers in the array.
    """
    # Base cases:
    if numbers.shape[0]==1:
        return numbers[0]
    # Recursive case:
    else:
        return numbers[0] * array_product_rec(numbers[1:])
    
def concat_rec(words : list[str]) -> str:
    """
    Concatenates a list of words into a single string with spaces in between using recursion.

    Parameters
    ----------
    words : list[str]
        The list of words.

    Returns
    -------
    str
        The concatenated string.
    """
    #Base case
    if len(words) == 0:
        return ""
    #Recursive case
    else:
        if len(words) > 1:
            space = " " 
            return words[0] + space + concat_rec(words[1:])
        else: 
            space =""
            return words[0] + space + concat_rec(words[1:]) 
    
def half_christmas_tree_rec(height : int) -> str:
    """
    Generates a string representing half of a Christmas tree pattern using recursion.

    Parameters
    ----------
    height : int
        The height of the tree.

    Returns
    -------
    str
        The string representing the Christmas tree pattern.
    """
    # Base case:
    if height == 0:
        return ""
    # Recursive case: 
    tree = half_christmas_tree_rec(height - 1) + "*" * height + "\n"
    return tree
    
def find_max(llist : list[int]) -> int:
    """
    Finds the maximum value in a list using iteration.

    Parameters
    ----------
    llist : list[int]
        The list of integers.

    Returns
    -------
    int
        The maximum value in the list.
    """
    max_value = llist.pop()
    for value in llist:
        if value>max_value:
            max_value = value
    return max_value

def find_max_rec(llist : list[int]) -> int:
    """
    Finds the maximum value in a list using recursion.

    Parameters
    ----------
    llist : list[int]
        The list of integers.

    Returns
    -------
    int
        The maximum value in the list.
    """
    # Base case:

    if len(llist) == 1:
        return llist[0]
    # Recursive case: 

    else:
        return max(find_max_rec(llist[:-1]), llist[-1])

