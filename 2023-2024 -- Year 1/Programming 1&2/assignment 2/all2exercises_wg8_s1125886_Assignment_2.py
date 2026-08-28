#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This assignment was done by Student Angelina Podolako s1125886
I also added here exercises from previous lessons
"""


#%% Problem 15
# Your code goes here

#%% Problem 15
# Your code goes here
#1
nameq1= " First one. Write your name, please. "
print (nameq1)
namea1 = input ()
print ( "Your name is "+ namea1 )

ageq= " What is your year of birth? "
print (ageq)
agea1 = input ()
print ( "You born in "+ agea1 )

#2
nameq2= " Second one. Write your name, please. "
print (nameq2)
namea2 = input ()
print ( "Your name is "+ namea2 )

print (ageq)
agea2 = input ()
print ( "You born in "+ agea2 )

#3
nameq3= " Third one. Write your name, please. "
print (nameq3)
namea3 = input ()
print ( "Your name is "+ namea3 )

print (ageq)
agea3 = input ()
print ( "You born in "+ agea3 )

#age str to int and age calculations
agea1 = int(agea1)
agea2 = int(agea2)
agea3 = int(agea3)
agei1= 2023 - agea1
agei2= 2023 - agea2
agei3= 2023 - agea3

average= (agea1+agea2+agea3)/3

#ANSWERS
print (" \n \n The name of the historical women are: " +namea1 + ", " + namea2 + ", " + namea3)
print (namea1+ " todays age is " ,agei1 , ". ")
print (namea2+ " todays age is " ,agei2 , ". ")
print (namea3+ " todays age is " , agei3 , ". ")
print ("The average of your birth year is" , average)

#NEW! task 11 
#NEW TASK 15
if agei1>agei2 and agei1>agei3:
    print (namea1, " is the oldest women in that datasaet.")
elif agei1<agei2 and agei2>agei3:
    print (namea2, " is the oldest women in that datasaet.")
elif agei1<agei3 and agei2<agei3:
    print (namea3, " is the oldest women in that datasaet.")
else:
    print ("ERROR")





#%% Problem 16
# Your code goes here
# Your code goes here
print("\n\n\n NEW TASK")
a = int(input("Give the first number "))
b = int(input("Give the second number "))

modular_diva = a % b
floor_diva = a // b
powera = b ** a

modular_divb = b % a
floor_divb = b // a
powerb = a ** b


if a>b:
    print ( "Modular division is ", modular_diva )
    print ("Floor divicion is " , floor_diva )
    if a<5 :    
        print ("Power is ", powera)
    if  b<5:
        print ("Power is ", powerb)
    
elif a<b:
    print ( "Modular division is ", modular_divb )
    print ("Floor divicion is " , floor_divb )
    if a<5 :    
        print ("Power is ", powera)
    if  b<5:
        print ("Power is ", powerb)
        
else:
    print("Error, they are equal")







#%% Problem 17
# Write the description of your code in the comment below
"""
Your description goes here...


"""

# Your code goes here

# Write the description of your code in the comment below
"""
Your description goes here...
-User chooses a "Harry Potter" character among 1-Harry Potter 2- Hermione Granger 3- Ron Weasley
-Program asks about which property of the chosen character that they want to know.
-1 is for personality. 2 is for magic ability. 3 is for the pet.

"""

# Your code goes here

msg1 = " Welcome User ! This is a compiled version of the Harry Potter’s adventures. "
print(msg1)
character = int(input("\n Which of the three main characters do you want to know about? \n 1- Harry Potter \n 2- Hermione Granger \n 3- Ron Weasley \n"))
personality_harry = "Harry is a really brave wizard. And at the same time, he wants to do the right thing for everyone.. "
magic_ability_harry = "Harry is a complete warrior in the wizard world. During a combat, he can perform the most unique magics. "
the_pet_harry = "Harry has an owl! "

personality_hermione = "Hermione is really good at solving problems. As well as she is a nerd, she also doesn't hesitate to express her feelings to the Professor Snape. (You wouldn't want to mess with Snape!)"
magic_ability_hermione = "Hermione is a master at preparing magic potions, especially the herbal ones. "
the_pet_hermione = "She has a cat :) "

personality_ron = "Ron is just a clumsy. "
magic_ability_ron = "Ron is just a clumsy. "
the_pet_ron = "He has a mouse. Weirdo. "

if character == 1:
    msg2 = int(input("What do you want to know about Harry? \n 1- Personality \n 2- Magic Ability \n 3- The Pet "))
    if msg2 == 1:
        print(personality_harry)
    elif msg2 == 2:
        print(magic_ability_harry)
    elif msg2 == 3:
        print(the_pet_harry)
    else:
        print("Opps.. Invalid number")

if character == 2:
    msg2 = int(input("What do you want to know about Hermione? \n 1- Personality \n 2- Magic Ability \n 3- The Pet "))
    if msg2 == 1:
        print(personality_hermione)
    elif msg2 == 2:
        print(magic_ability_hermione)
    elif msg2 == 3:
        print(the_pet_hermione)
    else:
        print("Opps.. Invalid number")
    
if character == 3:
    msg2 = int(input("What do you want to know about Ron? \n 1- Personality \n 2- Magic Ability \n 3- The Pet "))
    if msg2 == 1:
        print(personality_ron)
    elif msg2 == 2:
        print(magic_ability_ron)
    elif msg2 == 3:
        print(the_pet_ron)
    else:
        print("Opps.. Invalid number")
        
else:
    print("You had only one task to do. Are you alright?")




#%% Problem 19
# Your code goes here
# Your code goes here
intro1 = " We were good , we were gold \n " +\
" Kinda dream that can ’t be sold \n " +\
" We were right ’ til we weren ’t \n " +\
" Built a home and watched it burn \n "
intro2 = " Paint my nails cherry red \n " +\
" Match the roses that you left \n " +\
" No remorse , no regret \n " +\
" I forgive every word you said \n "
prechorus = " I didn ’t wanna leave you \n " +\
" I didn ’t wanna lie/fight \n " +\
" Started to cry , but then remembered I \n "
chorus1 = " I can buy myself flowers \n " +\
" Write my name in the sand \n " +\
" Talk to myself for hours \n " +\
" Say things you don ’t understand \n " +\
" I can take myself dancing \n " +\
" And I can hold my own hand \n " +\
" Yeah , I can love me better than you can \n "
chorus2 = " Can love me better \n " +\
" I can love me better , baby \n"
chorus2_ending = " Can love me better \n " +\
" I \n "
# if bl1 then intro 1; if bl2 then intro 2; if bl 3 then nothing
for iblock in range (3) :
    if iblock == 0:
        print ( intro1 )
    elif iblock == 1:
        print(intro2) 
    #print that in any block
    print (prechorus)
    print(chorus1)
    # print it twice in bl1, and three times in bl2 and bl3
    if iblock == 0:
        for ichorus2 in range (2):
            print (chorus2)
    else:
        for ichorus2 in range (3):
            print (chorus2)
    #print it in any block        
    print (chorus2_ending)



# that was pretty hard and let me to think a lot)))))









#%% Problem 20
# Your code goes here
# Your code goes here
days = [ " Mon " , " Tue " , " Wed " , " Thu " , " Fri " ]
daytasks = []

for day in days:
    tasks = []
    n_tasks = int ( input ( " \nHow many tasks do you have for " +day+ "?  -->  " ) )
    for i in range ( n_tasks ) :
        task_name = input ( " Task number " + str ( i +1) + ": " )
        tasks.append ( task_name )
    daytasks.append(tasks)

today= int(input("\n\n\n Which day is today? " + str(days) +"?  -->  "))
s = daytasks[today]
for item in s:
    print( item)



#that one made me cry BUT our the best on the planet TA helped me and know I know much more, as well as I am not crying now





#%% Problem 21 
# Your code goes here
peoplecount=int(input("How much people at all there are?  --> "))
allinfo=[]


for i in range(1, peoplecount+1):
    print(f"\n\n\nPerson {i}:")
    name=[]
    name= str (input("What is your name?  -->  ")) 
    intervcount= int(input("How many interviews did you have?  -->  "))
    
    for eachinterv in range(intervcount):
        questions=int(input(f"How many questions you had on {eachinterv+1} interview?  --> "))
        whatquestionlist=[]
        whatanswerlist=[]
        
        for j in range (1, questions+1):
            whatquestion= str (input(f"\nWhat {j} question you was asked?  -->  ")) 
            whatquestionlist.append ( whatquestion )
            whatanswer= str (input(f"What {j} answer you gave ?  -->  ")) 
            whatanswerlist.append ( whatquestion )

    print(f"Summary for Interview {i}:")
    print(f"Name: {name}")
    for q in range(intervcount):
        print(f"Question {q+1}: {whatquestionlist[q]}; Answer {q+1}: {whatanswerlist[q]}")



#If you want to modify the code to keep the information about each interviewee for later use,
# you can use data structures like lists or dictionaries to store the information. 
#If you want to keep the information about each interviewee for later use, 
#you can modify the code to store the information in a more persistent data structure like a list or a dictionary outside of the loop.



#%% Problem 22 

""""
# Your answers go here

    1. What’s the difference between the keywords continue and break?
    
Continue - used to skip the rest of the loop
Break - used to stop the loop

-->The break operator exits the loop. And the continue statement jumps to the next iteration of the loop.



    2. Exemplify when would you use each one of them (continue/break) in a loop.
    
---> Break - when a certain condition is met, and I don't want to continue iterating. 
    Example: In a loop that iterates through a list of numbers, Imight use break to exit the loop when I find a specific number I'm looking for.
    Is used to exit a loop prematurely based on a condition.
    
    Continue - when I want to skip the current iteration of the loop and move to the next one.
    Example: In a loop that iterates through a list of numbers, I might use continue to skip even numbers and only process odd numbers.
    Is used to skip the current iteration and move to the next one in a loop based on a condition.

    3. How do you identify the structure of a for loop from a problem? 
    Describe your thought process using one of the problems in the 
    lesson/assignment as an example.
   
--->We use the for loop to perform the tasks we need for several variables at once.
    For example, task 20. We had to ask the same question for all days of the week and get answers.
    First you need to understand exactly what needs to be done, then decide whether to use a loop.
    Next, give the values from which to which variable we will implement further code.
    Later in this assignment, we asked a question and asked to enter an answer. The final action was to add (save) the answer to the list by entering each new value at the end of the list.
    There may be other conditions in the cycle.

""""


#%% Problem 23 - Part A
# Modify the code below

n = int(input("Give me an integer N: "))
sum = 0 
i = 0

while (i <= n):
    sum += i
    i+=1
    
print (f"Sum from 0 to N is {sum}")


#%% Problem 23 - Part B
# Your code goes here

while True:
    n = int(input("Give me an integer N: "))
    if n<0:
        break
    
    sum = 0 
    i = 0
    
    while (i <= n):
        sum += i
        i+=1
    
print (f"Sum from 0 to N is {sum}")










#%% Problem 24 

# Sample code 

def check_balance(amount, balance):    
    if amount<=balance:
        valid = True
    else:
        print(warning_msg)
        valid = False
    # checkpoint 1
    return valid

def transfer_x(x,sender,receiver):
    valid_transaction = check_balance(x, sender)
    if valid_transaction:
        sender = sender-x
        receiver = receiver+x
    # checkpoint 2
    return sender,receiver
    
warning_msg = "Insuficient balance"
a = 40
b = 0
for i in range(10):
    a,b = transfer_x(i,a,b)
    print(a)
# checkpoint 3


"""
# Your answer goes here:

Global namespace: warning_msg ; a ; b ;
Local namespace (check_balance): amount ; balance ; valid
Local namespace (transfer_x):  x ; sender ; reciever ; valid_transaction

Checkpoint 1: amount ; balance ;valid ;warning_msg;
Checkpoint 2: sender ; reciever ; valid_transaction ;x; warning_msg
Checkpoint 3: a ; b; warning_msg

"""

#%% Problem 25
# Your code goes here


n = int(input("Enter a number : "))

def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

factors_of_n = find_factors(n)
print(f"Factors of {n}: {factors_of_n}")

def prime (number):
    if number < 2:
        return False  
    factors = find_factors(number)
    return len(factors) == 2 

result = prime(n)
if result:
    print(f"{n} is prime.")
else:
    print(f"{n} is not prime.")








#%% Problem 26

"""
# Your answers go here

1. What is the main difference between a for loop and a while loop? In which situations you
can not use a for loop, but can use a while loop?

We use the for loop to perform an operation (cycle) from 0 (or another set value) to a value selected by us or entered by the user. 
We will execute the same code for all these variables. The while loop will be executed until the statement is TRUE, and I do not know. 
the exact number of iterations.

I can use a while loop when the number of iterations depends on the execution conditions,
 which may change while the program is running. For example, when you need to repeatedly perform an action until a certain
 condition is met, the while loop will be better and more convenient.


2. When your program access a variable inside of a function, in which namespaceS it looks
for that variable?

When a program accesses a variable inside a function, 
the program first searches for this variable in the local namespace of the function. 
If the variable is not found locally, then it should be searched in the global namespace.
 If the variable is still not found in any of these namespaces, a name error occurs, indicating that the variable is not defined.


3. If there are two variables with the same name in different accessible namespaces, how
does a program select which one to use?

The program selects the variable it sees.
A variable in the local scope itself has priority.
If a variable is found in the local scope, it will be used; otherwise, the program will search in the global scope.
If there are several variables with the same name in different forms, the one that is in the local scope itself will be used.
"""



