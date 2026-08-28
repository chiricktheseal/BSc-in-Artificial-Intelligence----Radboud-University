#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import random as rnd

# maybe you need to install matplotlib
# pip install matplotlib
import matplotlib.pyplot as plt 


def random_array(a: int, b: int, n: int):
    """
    Generate a one-dimensional NumPy array with 'n' random integers between 'a' and 'b'.

    Parameters
    ----------
    a : int
        Lower bound for random integers.
    b : int
        Upper bound for random integers.
    n : int
        Number of elements in the array.

    Returns
    -------
    random_array : numpy.ndarray
        One-dimensional array containing random integers.

    """
    #This line of Python code uses multiple assignment to exchange the values of variables a and b. 
    #This technique prevents the problem when a is greater than b by ensuring that a will always contain the smaller of the two values
    if a > b:
        a, b = b, a
      
    one_dimen_array = np.random.randint(a, b + 1, n, dtype='int32')
    return one_dimen_array


def element_mult(x: np.ndarray, y: np.ndarray):
    """
    Perform element-wise multiplication of two NumPy arrays.

    Parameters
    ----------
    x : numpy.ndarray
        First input array.
    y : numpy.ndarray
        Second input array.

    Returns
    -------
    result : numpy.ndarray or None
        Element-wise product of input arrays if they have the same length, otherwise None.

    """
    if  len(x) == len(y) :
      z = np.multiply(x,y)
      z = z.astype(x.dtype)
      return z
    else:
      return None

def find_max(x: np.ndarray):
    """
    Find the index of the maximum value in a one-dimensional NumPy array.

    Parameters
    ----------
    x : numpy.ndarray
        One-dimensional array.

    Returns
    -------
    max_index : int or None
        Index of the maximum value in the array or None if there are negative values.

    """
    # check for negative values
    if np.any(x < 0):
        return None
    
    # Index of max value
    last_max_index = 0
    
    # go through the elements of the array and find the index of the last maximum value
    for i in range(1, len(x)):
        if x[i] >= x[last_max_index]:
            last_max_index = i
    
    return last_max_index
  
def transpose(x: np.ndarray):
    """
    Transpose a two-dimensional NumPy array.

    Parameters
    ----------
    x : numpy.ndarray
        Two-dimensional array.

    Returns
    -------
    transposed_array : numpy.ndarray
        Transposed array.

    """
    # get shape of array x
    m, n = x.shape
    # Make new array of shape (n,m) with same type as array x 
    y = np.zeros((n, m), dtype=x.dtype)
        
    for i in range(m):
        for j in range(n):
            y[j,i] =x[i,j]
            
    return y

def is_square(x: np.ndarray):
    """
   Check if a NumPy array is a square matrix.

   Parameters
   ----------
   x : numpy.ndarray
       Input array.

   Returns
   -------
   is_square : bool
       True if the array is a square matrix, False otherwise.

   """

    shape = x.shape
    #1D check
    if len(shape) == 1 and shape[0] == 1:
            return True
    elif len(shape) < 2:
        return False
       
    # check that dimen. are equal
    for dim in shape:
        if dim != shape[0]:
            return False
    
    return True

def is_magic(x: np.ndarray):
    """
    Check if a NumPy array is a magic square.

    Parameters
    ----------
    x : numpy.ndarray
        Input array.

    Returns
    -------
    is_magic : bool or None
        True if the array is a magic square, False otherwise. None if the array has more or less than 2 dimensions or is not a square matrix.

    """
    shape = x.shape
    
    if len(shape) != 2 or shape[0] != shape[1]:
        return None
    
    # Counting the sums of rows and columns
    row_sums = np.sum(x, axis=1)
    col_sums = np.sum(x, axis=0)
    
    # Counting sums of diagonals
    diag1_sum = np.sum(np.diag(x))
    diag2_sum = np.sum(np.diag(np.fliplr(x)))
    
    # Checking the equality of all sums
    if not np.all(row_sums == row_sums[0]) or not np.all(col_sums == col_sums[0]):
        return False
    
    # Checking the equality of diagonal sums
    if not (diag1_sum == diag2_sum == row_sums[0]):
        return False

    return True
    
def main():
    """
    Main function
    """
    x = np.arange(10)
    
    try:
        # if your functions are working properly, you can implement changes in 
        # main() here
        
        y = random_array(0, 100, 10)
        
        #the np.mean(y) to find the average value of the array y
        mean_value = np.mean(y)
        #determine the points that are above the average value
        above_mean = y > mean_value
        
        # Plotting a graph with black dots and lines
        #plotting using the plot.plot function. In this case, these are black dots with lines connecting them. x is an array of values along the X axis, y is an array of values along the Y axis, 'ko-' is the formatting of the graph: 'k' means black, 'o' means that the points will be displayed in circles, and '-' means that a line will be drawn between the points.
        plt.plot(x, y, 'ko-')
        
        # highlight in red the points that are above the average value
        #the dots will be red ('ro').  x[above_mean] and y[above_mean] to pass only those points that match the above_mean condition
        plt.plot(x[above_mean], y[above_mean], 'ro')
   
    except:
        
        # if your functions are not working properly, you can implement changes
        # in main() here:
            
        y = np.arange(100).reshape((4,25)).T.flatten()[0:10]
        imax = 7
        
        mean_value = np.mean(y)
        above_mean = y > mean_value

        plt.plot(x, y, 'ko-')
        
        plt.plot(x[above_mean], y[above_mean], 'ro')
            
    
    # Example of magic matrix
    x = np.array([[2,7,6],[9,5,1],[4,3,8]])        
    print(x)
    
    return None
    

# The main body of your program should only call the main() function like this:
if __name__=="__main__":    
    main()
    
    
