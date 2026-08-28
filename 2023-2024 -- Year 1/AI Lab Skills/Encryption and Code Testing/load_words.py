#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:52:39 2024

@author: judithrudolph
"""

def load_words(file_name="words.txt"):
    """
    Returns a list of lowercase words loaded from a file. 
    
    Args:
        file_name (str): the file containing the word list. Default: "words.txt".
        
    Returns:
        (list): the list of candidate words.
    """
    # Load the file
    print("Loading word list from file.")
    in_file = open(file_name, 'r')
    
    # Parse the words
    line = in_file.readline()
    word_list = line.split()
    
    # Print the number of words
    print("A total of", len(word_list), "words were loaded.")
    return word_list