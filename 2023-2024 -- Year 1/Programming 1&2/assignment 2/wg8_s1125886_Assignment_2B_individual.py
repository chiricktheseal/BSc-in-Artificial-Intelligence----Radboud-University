#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#%%
"ANGELINA PODOLAKO S1125886      +I also added exercises 13, 14a, 14 b here"

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

answer = input(question1)
if answer == "yes"
    answer = input(question2)
    if answer = "no":
         print(answer1)
     elif answer == "yes":
        print(answer2)
Else:
    print("All praise the error message! :)")
print(final_message)

error_message = 'Invalid answer"


#%% Problem 14 - Part B (individual)
# Your code goes here

question1 = "Do you know about the pedagogical tools of this course? [yes/no]"
question2 = "Have you ever heard of the term 'banking education'? [yes/no]"
answer1 = "It's the idea that teachers detain the static knowledge and fill it onto the students, mere repositories."
answer2 = "In this class we try to avoid the idea that teachers narrate the reality. Instead, students are invited to dialogue."
final_message = "If you wanna know more about that, have a look at the extra material of the course"
error_message = "Invalid answer" # two different type of quotes

answer = input(question1)
if answer == "yes": # expected :
    answer = input(question2)
elif answer == "no": # meant ==, not = #i think it can be better to use elif here 
    print(answer1)
elif answer == "yes": #excess space before elif
    print(answer2)
else: # else, not Else
    print(error_message)
print(final_message)


#%% Problem 18 (individual)

"""
NEW ONE


Write your answer below, using ',' to separate the columns 
and ';' to separate the lines. Complete the missing lines.

Ex.: 
Loop number, Code line, i, sum;
 -, 1, -, -;
 -, 2, -, 0;
 1, 3, 0, 0;
 1, 4, 0, 0;
 1, 5, 0, 0;
 1, 6, 0, 0;
 2, 3, 1, 0;
 2, 4, 1, 1;
 2, 5, 1, 1;
 2, 6, 1, 1;
 3, 3, 2, 1;
 3, 4, 2, 3;
 
 [MISSING LINES]
\/\/\/\/\/\/\/\/\
 3, 5, 2, 3;
 3, 6, 2, 3;
 4, 3, 3, 3;
 4, 4, 3, 6;
 4, 5, 3, 6;
 4, 6, 3, 6;
 5, 3, 4, 6;
 5, 4, 4, 10;
 5, 5, 4, 10;
 5, 6, 4, 10;
 6, 3, 5, 10;
 6, 4, 5, 15;
 6, 5, 5, 15;
 6, 6, 5, 15;
 7, 3, 6, 15;
 7, 4, 6, 21;
 7, 5, 6, 21;
 7, 6, 6, 21;
 8, 3, 7, 15;
 8, 4, 7, 28;
 8, 5, 7, 28;
 8, 6, 7, 28;
 /\/\/\/\/\/\/\/\/\
 [MISSING LINES]
 -, 7, 7, 0;
 
"""


