# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 15:52:00 2023

@author: Angelina
"""
#The difference is which way of entering information takes up more space on the computer, takes longer to process and takes up more linesThe difference is which way of entering information takes up more space on the computer, takes longer to process and takes up more lines
print ("Hello! \nPlease, enter first numbers after second, and this program will check which one is higher")
var1 = input ()
var1 = int ( var1 )

var2 = int ( input () )

if var1 > var2 :
    print ( " The first input is higher " )
if var1 < var2 :
    print ( " The second input is higher " )
if var1 == var2 :
    print ( " They are equal " )
 
print ("the sum of two numbers is ", var1 + var2) 
print ("the difference of two numbers is ", var1 - var2 )