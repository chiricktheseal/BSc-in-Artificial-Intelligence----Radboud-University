#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Artificial Intelligence Lab Skills
Assignment 2 Hangman

Author(s): Angelina Podolako s1125886
Group: 57
Contributor(s): i did all in my own
Average hours spent per person: 10h - Angelina
"""


import random
import string


WORD_LIST_FILENAME = "words.txt"  # the file with all candidate secret words.


def load_words(file_name="words.txt"):
    """
    Returns a list of words loaded from a file. Words are strings of lowercase 
    letters.
    
    Args:
        file_name (str): the file to read words from. Default: "words.txt".
        
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

def get_secret_word(word_list):
    secret_word = random.choice(word_list)
#######################
    print ("\nDELE THIS   "+ secret_word+"\n")
######################
    hidden_word = '_' * len(secret_word)
    print ("Secrete word is: " + hidden_word) #prints the initial hidden word.
    
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True #all letters in the secret word are in the guessed letters

def format_guessed_word(secret_word, letters_guessed):
    formatted_word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            formatted_word += letter + " "
        else:
            formatted_word += "_ "
    return formatted_word.strip()

def get_available_letters(letters_guessed):
    alphabet = string.ascii_lowercase #abcdef...
    available_letters = alphabet #abcdef... at the initial state
    for ask_letter in alphabet:
        if ask_letter in letters_guessed:
            available_letters = available_letters.replace(ask_letter, "-")
    return available_letters 

def  get_unique_letters_in_word(secret_word):
    unique_letters = []
    for letter in secret_word:
        if letter not in unique_letters:
            unique_letters.append(letter)
    return ''.join(unique_letters) 



def is_word_match(word, formatted_word):
    formatted_word = formatted_word.replace(" ", "")
    if len(formatted_word) == len(word):
        for i in range(len(word)):
            if word[i] == formatted_word[i]:
                continue
            elif formatted_word[i] == "_":
                continue
            else:
                return False
        return True
    else:
        return False
      

def show_matches(word_list, formatted_word) :
    matching_list=[]
    for word in word_list:
        if is_word_match(word, formatted_word):
            matching_list.append(word)

    if len(matching_list) <= 100 and len(matching_list)>0:
        print("Found " + str(len(matching_list))+ " matches: " , ' '.join(matching_list))
    elif len(matching_list) > 100:
        print("Found too many (" + str(len(matching_list))+ ") matches. Here are a few: " , ' '.join(matching_list[:100]))
    elif len(matching_list) == 0:
            print("No matches found!")
    return matching_list



def hangman_game():
    """
        Loads word_list. Saying hello+ warnings ang guesses count+ rules of functions (*,#). Example:
        Loading word list from file.
        A total of 55900 words were loaded.
        Welcome to the game Hangman!
        Secrete word is: _ _ _ _ _ _
        I am thinking of a word that is 6 letters long.
        You have an initial 6 guesses and 3 warnings at the start of the game
    """
    word_list = load_words() # Load all candidate words
    
    print("Welcome to the game Hangman! \n    For hint input -> * after -> Try to guess letter: \n    To quit input -> # after -> Try to guess letter: ")
    
    play_again_flag = True

    while play_again_flag:

        secret_word = get_secret_word(word_list) # Takes a list of candidate words and returns one word chosen at random
        print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")

        letters_guessed = []
        warnings=3
        guesses=6

        print("You have an initial 6 guesses and 3 warnings at the start of the game")


        while True:
            """
                separates first round from greetings. Starting counting warnings and guesses. Available letters, guessed so far and input is here. Example:
                ===================================================
                You have 6 guesses left and 3 warnings left!
                Available Letters: abcdefghijklmnopqrstuvwxyz
                Guessed so far: _ _ _ _ _ _
                Try to guess letter: 
                each round it differs
            """       
            print("===================================================") # a) Print some dashes to separate rounds;

            if warnings == 0:
                guesses -= 1
                warnings = 3

            print("You have "+ str(guesses) + " guesses left and " + str(warnings) + " warnings left!")
            
            available_letters=get_available_letters(letters_guessed) #returns a string containing all English letters that are not already in the list of guessed letters
            print("Available Letters:", available_letters , end=' ') #c)Print the available letters; #end=' ' -ensuring that there is a space instead of a newline character at the end.

            formatted_word = format_guessed_word(secret_word, letters_guessed)  #formats a guessed word such that the letters in the secret word that are also in the guessed letters are visible, and those that are not yet guessed are masked with an underscore
            print("\nGuessed so far:", formatted_word) #d) Print the word as guessed so far; 
            
            """
                Asking for input  -> Try to guess letter: 
                if letter is in word-> appears in guesssed so far:
                if not in ---> and word vowel -> -2 guesses ---> and word constant -> -1 guesses
                if not alphabet or repeats(except * and #) -> -1 warning
                if * -> hint
                if # -> quit
            """       

            ask_letter = str.lower(input("Try to guess letter: ")) #e) Ask the user to guess one letter;
            
            if ask_letter =="*":
                hint = show_matches(word_list, formatted_word)
            elif ask_letter =="#":
                print("You have quit the game.")
                play_again_flag = False  # Set the flag to False to exit the outer loop
                break


            if not (ask_letter.isalpha() or ask_letter == '*'or ask_letter == '#'):
                warnings -= 1
                print("Warning! This letter is invalid. You have " + str(warnings) + " warnings left.")
            elif ask_letter in letters_guessed and not ( ask_letter == '*'or ask_letter == '#'):
                warnings -= 1
                print("Warning! You already guessed this letter. You have " + str(warnings) + " warnings left.") #f) Immediately tell the user whether the guessed letter was in the word or not.
                continue
            
            if ask_letter in secret_word:
                print("Good guess!")  # Print "Good guess" if the guessed letter is in the word. # f) Immediately tell the user whether the guessed letter was in the word or not.у
            else:
                if ask_letter in "aeiouy":
                    guesses -=2
                    print("That letter is not in the word. You have " + str(guesses) + " guesses left.")  # f) Immediately tell the user whether the guessed letter was in the word or not.
                elif ask_letter in "bcdfghjklmnpqrstvwxz":
                    guesses -=1
                    print("That letter is not in the word.You have " + str(guesses) + " guesses left.")
            
            letters_guessed.append(ask_letter)

            """
                Win if word guessed and total score is on the screen
                Loose if 0 guesses left
                Can start new game
            """       
            win = is_word_guessed(secret_word, letters_guessed) #determines whether the secret word has been guessed
            
            if win:
                print("===================================================") # a) Print some dashes to separate rounds;
                total_score = guesses *  len(get_unique_letters_in_word(secret_word)) 
                print("Congratulations, you won! \nYour total score for this game is: ", total_score) #f) Immediately tell the user whether the guessed letter was in the word or not.
                play_again = input("Do you want to play another game? (yes/no): ").lower()# Ask the player if they want to play another game
                if play_again == "yes":
                    break  # Break out of the inner loop to start a new game
                elif play_again == "no":
                    print("Goodbye! Thanks for playing.")
                    play_again_flag = False  # Set the flag to False to exit the outer loop
                    break  # Exit the inner loop if the player doesn't want to play again


            elif guesses == 0 :
                print("===================================================") # a) Print some dashes to separate rounds;
                print("Oops, you ran out of guesses. The word was: ", secret_word) #f) Immediately tell the user whether the guessed letter was in the word or not.
                play_again = input("Do you want to play another game? (yes/no): ").lower()# Ask the player if they want to play another game
                if play_again == "yes":
                    break  # Break out of the inner loop to start a new game
                elif play_again == "no":
                    print("Goodbye! Thanks for playing.")
                    play_again_flag = False  # Set the flag to False to exit the outer loop
                    break  # Exit the inner loop if the player doesn't want to play again


if __name__ == "__main__":
    
    hangman_game()

    #print(is_word_match("traetp", "t r e e _ _"))