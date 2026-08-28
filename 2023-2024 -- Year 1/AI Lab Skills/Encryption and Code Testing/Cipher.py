# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 17:40:22 2024

@author: Angelina
"""
from load_words import load_words
import random

class Cipher:
    """
    A class representing a generic cipher.
    """
    
    def __init__(self, text):
        """
        Initializes the Cipher with the given text and loads a list of valid words.

        Args:
            text (str): The text to be encrypted or decrypted.
        """
        self.__text = text
        self.__valid_words = load_words()
        
    def get_text(self): 
        """
        Returns the text of the cipher.

        Returns:
            str: The text of the cipher.
        """
        return self.__text
    
    def get_valid_words(self):
        """
       Returns the list of valid words.

       Returns:
           list: The list of valid words.
       """
        return self.__valid_words
    
    def set_text(self, new_text):
        """
       Sets the text of the cipher.

       Args:
           new_text (str): The text to set.
       """
        self.__text = new_text
        
class CaesarCipher(Cipher):
    """
    A class representing a Caesar cipher.
    """
       
    def build_cipher(self, shift):
        """
        Builds the Caesar cipher mapping.

        Args:
            shift (int): The shift value for the cipher.

        Returns:
            dict: A dictionary mapping each letter to its shifted counterpart.
        """
        alphabet =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        shifted_alphabet = alphabet[shift:] + alphabet[:shift]  
        
        cipher = {}
        for letter in range(len(alphabet)):
            cipher[alphabet[letter]] = shifted_alphabet[letter]
        return cipher
            
    def apply_cipher(self, shift):
        """
        Applies the Caesar cipher to the text.

        Args:
            shift (int): The shift value for the cipher.

        Returns:
            str: The encrypted or decrypted text.
        """
        cipher = self.build_cipher(shift)
        encrypted_text = ""
        
        for letter in self.get_text():
            if letter.upper() in cipher:  
                shifted_letter = cipher[letter.upper()] 
                if letter.islower():
                    shifted_letter = shifted_letter.lower()
                encrypted_text += shifted_letter
            else:
                encrypted_text += letter  
        return encrypted_text
        
    def decrypt_message(self):
        """
        Decrypts the message and returns the decrypted text.

        Returns:
            str: The decrypted text.
        """
        words = self.get_text().split()
        best_shift = 0
        max_count = 0
       
        for shift in range(26):
            count = 0
            for word in words:
                decrypted_word = self.apply_cipher(-shift)  
                if decrypted_word.lower() in self.get_valid_words():  
                    count += 1
            if count > max_count:
                max_count = count
                best_shift = shift
        
        decryption_key = 26 - best_shift
        decrypted_text = self.apply_cipher(-best_shift)

        return (decryption_key, decrypted_text)

    def write_message(self, shift):
        """
        Writes the encrypted message to a file.

        Args:
            shift (int): The shift value for the cipher.
        """
        encrypted_text = self.apply_cipher(shift)
        
        with open("message.txt", "w") as file:
            file.write(encrypted_text)
   
class SubstitutionCipher(Cipher):
    """
    A class representing a substitution cipher.
    """

    def build_cipher(self):
        """
        Builds the substitution cipher mapping.

        Returns:
            dict: A dictionary mapping each letter to its substituted counterpart.
        """
        alphabet =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        shuffled_alphabet = ''.join(random.sample(alphabet, len(alphabet)))    
        cipher = {}
        
        for i in range(26):
            cipher[alphabet[i]] = shuffled_alphabet[i]
        
        key = ''.join(cipher[letter] for letter in alphabet)
        return cipher, key
            
        
    def apply_cipher(self):
        """
        Applies the substitution cipher to the text.

        Returns:
            str: The encrypted or decrypted text.
        """
        cipher = self.build_cipher()
        encrypted_text = ""
        
        for letter in self.get_text():
            if letter.upper() in cipher:  
                shifted_letter = cipher[letter.upper()] 
                if letter.islower():
                    shifted_letter = shifted_letter.lower()
                encrypted_text += shifted_letter
            else:
                encrypted_text += letter  
        return encrypted_text
    
    def write_message(self, shift):
        """
        Writes the encrypted message to a file.
        """
        cipher, key = self.build_cipher()
        encrypted_text = self.apply_cipher()
        
        with open("message_sc.txt", "w") as file:
            file.write(encrypted_text)
        return key
        
    def decrypt_message(self, key):
        """
        Decrypts the message using the given key.

        Args:
            key (dict): The key to decrypt the message.

        Returns:
            str: The decrypted text.
        """
        decryption_cipher = {value: key for key, value in key.items()}
        decrypted_text = ""
    
        for letter in self.get_text():
            # Checking if the letter exists in the decryption cipher
            if letter.upper() in decryption_cipher:
                original_letter = decryption_cipher[letter.upper()]
                if letter.islower():
                    original_letter = original_letter.lower()
                decrypted_text += original_letter
            else:
                decrypted_text += letter
        return decrypted_text