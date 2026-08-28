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