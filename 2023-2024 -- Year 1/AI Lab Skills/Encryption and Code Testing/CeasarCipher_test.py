# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 17:40:22 2024

@author: Angelina
"""
import pytest
from Cipher import CaesarCipher

def test_apply_cipher(): 
    """
    Test whether the method apply_cipher accepts and includes capitals, punctuation, and sentences correctly.
    """
    caesar_cipher = CaesarCipher("Hello, World!")
    encrypted_text = caesar_cipher.apply_cipher(3)
    assert encrypted_text == "Khoor, Zruog!"
    
def test_build_cipher_zero(): 
    """
    Test whether a shift 0 results in the same letter for at least one example letter.
    """
    caesar_cipher = CaesarCipher("A")
    cipher = caesar_cipher.build_cipher(0)
    assert cipher["A"] == "A"

def test_build_cipher_n(): 
    """
    Test whether a shift n results in the correct letter for at least one example letter.
    """
    caesar_cipher = CaesarCipher("A")
    cipher = caesar_cipher.build_cipher(5)
    assert cipher["A"] == "F"
    
def test_build_unique():
    """
    Test whether a shift n results in the correct letter for at least one example letter.
    """
    caesar_cipher = CaesarCipher("A")
    cipher = caesar_cipher.build_cipher(3)
    values = list(cipher.values())
    assert len(values) == len(set(values))

def test_decrypt_message(): 
    """
    Test whether the shift and message of an encryption indeed match the returned output of the decrypt_message method.
    """
    caesar_cipher = CaesarCipher("Khoor")
    decryption_key, decrypted_text = caesar_cipher.decrypt_message()
    assert decryption_key == 23  # Expected decryption key for shift of 3
    assert decrypted_text == "Hello"  # Expected decrypted text to be the same as original text


def test_negative_shift():
    """
    Test for negative shift processing.
    """
    caesar_cipher = CaesarCipher("Hello")
    encrypted_text = caesar_cipher.apply_cipher(-3)
    assert encrypted_text == "Ebiil"
    
def test_special_characters():
    """
    Test for processing different types of input data.
    """
    caesar_cipher = CaesarCipher("Hello, World!")
    encrypted_text = caesar_cipher.apply_cipher(5)
    assert encrypted_text == "Mjqqt, Btwqi!"
    
def test_shift_equal_alphabet_length():
    """
    A shift test equal to the length of the alphabet.
    """
    caesar_cipher = CaesarCipher("Hello")
    encrypted_text = caesar_cipher.apply_cipher(26)
    assert encrypted_text == "Hello"
    
# Run the tests
if __name__ == "__main__":
    pytest.main()  
    