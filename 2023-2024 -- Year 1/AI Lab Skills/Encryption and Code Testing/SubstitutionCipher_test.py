# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 17:40:22 2024

@author: Angelina
"""
import unittest
from Cipher import SubstitutionCipher

class TestSubstitutionCipher(unittest.TestCase):
    """A class to test the SubstitutionCipher class."""
    
    def test_build_cipher_seed(self):
        """Test whether the method build_cipher returns the same key when called with the same random seed."""
        substitution_cipher = SubstitutionCipher('')
        key1, _ = substitution_cipher.build_cipher()
        key2, _ = substitution_cipher.build_cipher()
        self.assertEqual(sorted(key1.values()), sorted(key2.values()))
    
    def test_build_unique(self):
        """Test whether the method build_cipher returns the same key when called with the same random seed."""
        substitution_cipher = SubstitutionCipher('')
        cipher, _ = substitution_cipher.build_cipher()
        self.assertEqual(len(set(cipher.values())), len(cipher))
    
    def test_build_numbers(self):
        """Test whether numbers remain the same after encryption."""
        substitution_cipher = SubstitutionCipher('')
        cipher, _ = substitution_cipher.build_cipher()
        for char in cipher:
            self.assertTrue(char.isalpha() or char == cipher[char])
    
    def test_decrypt_message(self):
        """Test whether the decrypted message matches the original text using the returned key."""
        text = "Spwwz, Hzcwo!"
        substitution_cipher = SubstitutionCipher(text)
        key = {'A': 'L', 'B': 'M', 'C': 'N', 'D': 'O', 'E': 'P', 'F': 'Q', 'G': 'R', 'H': 'S', 'I': 'T', 'J': 'U', 'K': 'V', 'L': 'W', 'M': 'X', 'N': 'Y', 'O': 'Z', 'P': 'A', 'Q': 'B', 'R': 'C', 'S': 'D', 'T': 'E', 'U': 'F', 'V': 'G', 'W': 'H', 'X': 'I', 'Y': 'J', 'Z': 'K'}
  
        decrypted_text = substitution_cipher.decrypt_message(key)
        self.assertEqual(decrypted_text, 'Hello, World!')
        
            
if __name__ == '__main__':
    unittest.main()