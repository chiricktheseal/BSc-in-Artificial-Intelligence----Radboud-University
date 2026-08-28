#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#%% Problem 13 (individual)
"""
Write your answer for problem 13 here in this comment section:
    
#1
If we put number 5 we get in first print out :
    The first number was 5
#2.1
 The number is bigger than 0 ( as well it can be any other number which is bigger than 0), so we need to give other one number
If second number is bigger than 0 ( for example 3), we get in second output number 3, that is sum of previous 2 numbers:
    The sum is 8
#2.2 
If second number is less than o (for example -2), we get 3rd number, that is differnce of 1st and 2nd numbers:
    The absolute sum is 7
#2.3
If second number waas something else (it can be only 0), we get:
    The second number was 0
#1.2 
If first number is smaller than 0 (negative numbers and 0), then we get:
    The first number has to be positive
#3
The last one output is (after one of #2.1,2,3,or after #1.2):
    Program terminated
    
#error
error is there if we put float not int
"""


#%% Problem 14 - Part A (individual)
# Fix the code below

question1 = "Do you know about the pedagogical tools of this course? [yes/no]"
question2 = "Have you ever heard of the term 'banking education'? [yes/no]"
answer1 = "It's the idea that teachers detain the static knowledge and fill it onto the students, mere repositories."
answer2 = "In this class we try to avoid the idea that teachers narrate the reality. Instead, students are invited to dialogue."
final_message = "If you wanna know more about that, have a look at the extra material of the course"
error_message = "Invalid answer" # two different type of quotes # put that line before w are gping to use that

answer = input(question1)
if answer == "yes": # expected :
    answer = input(question2)
    if answer == "yes": #excess space before elif
        print(answer2)
    elif answer == "no": # meant ==, not = #i think it can be better to use elif here #unnecessary to use space from line 47 to line 52
        print(answer1)
    else: # else, not Else
        print(error_message)
            
elif answer == "no": # meant ==, not = #i think it can be better to use elif here #unnecessary to use space from line 47 to line 52
    print(answer1)
else: # else, not Else
    print(error_message)
print(final_message)




#%% Problem 14 - Part B (individual)
# Your code goes here





