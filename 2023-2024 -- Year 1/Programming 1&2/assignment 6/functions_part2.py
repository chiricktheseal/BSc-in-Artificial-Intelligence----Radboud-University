#functions_part2.py

import numpy as np
import random
import time
import matplotlib.pyplot as plt

def sample_array(arr, n):
    # Use numpy's random.choice to sample n elements from the array arr
    random_array = np.random.choice(arr, n)
    return random_array  # Return n random samples from the array arr


def sort_array(arr):
    #quick-sort
    #Quicksort is a divide-and-conquer algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.
    #Base case:
    if len(arr) <= 1:
        return arr
    #Recursive case
    pivot = arr[len(arr) // 2]
    #easy. but long
    left = []
    for x in arr:
        if x < pivot:
            left.append(x)
    #hard. but short
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Combine the sorted subarrays and the pivot
    return sort_array(left) + middle + sort_array(right)

def plot_sorting(arr):
    # Creates a new shape (graph) with the specified size. figsize=(12, 6) means that the width of the figure will be 12 units and the height will be 6 units (in inches)
    plt.figure(figsize=(12, 6))
    
    # Line graph for sorted array (green)
    sorted_array = sort_array(arr)
    plt.plot(range(len(sorted_array)), sorted_array, color='green', label='Sorted')
    # Scatter plot for sorted ratings
    plt.scatter(range(len(sorted_array)), sorted_array, color='green', marker='o', label='Sorted Points')
    
    # Line graph for an unsorted array (red)
    plt.plot(range(len(arr)), arr, color='red', label='Unsorted')
    # Scatter plot for unsorted ratings
    plt.scatter(range(len(arr)), arr, color='red', marker='o', label='Unsorted Points')


    plt.legend()
    
    plt.title('Sorting Comparison')
    plt.xlabel('Index')
    plt.ylabel('Value')

    plt.show()
    
def time_sorting(sizes, data):
    # Measure and record the time taken to sort subsamples of the data array for different sizes
    times = []
    for size in sizes:
        subset = sample_array(data, size)# Sample a subset of the data
        start_time = time.perf_counter()
        sort_array(subset)# Sort the subset using quick-sort
        end_time = time.perf_counter()
        times.append(end_time - start_time)# Record the time taken
    return times