#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Artificial Intelligence Lab Skills
Assignment 6 Code Testing

Author(s):Angelina Podolako s1125886 
Group: 119
Contributor(s): 
Average hours spent per person: more than 15h
"""
from Cipher import CaesarCipher, SubstitutionCipher

# First verse of your favorite song
txt = """
Hey you, what do you see?
Something beautiful or something free?
Hey, you, are you trying to be mean?
If you live with apes man, it's hard to be clean """

# Creating a CaesarCipher object with txt as input
caesar_cipher = CaesarCipher(txt)

# Creating and saving the ciphertext in message.txt
caesar_cipher.write_message(3)  # Choose any shift value Ūser prefer

""" I can no do it since I do not have a partner
Let your group partner (if you still have one) pull the most recent version of your remote
repository. And let them decode the message by reading the message (code), creating
a CaesarCipher object with the encrypted message and using thedecrypt_message
method to create the plaintext.
• Switch roles for the SubstitutionCipher object (i.e. student two creates the ciphertext
and student one decrypts is). Now, the commit message on git should contain the key
"""