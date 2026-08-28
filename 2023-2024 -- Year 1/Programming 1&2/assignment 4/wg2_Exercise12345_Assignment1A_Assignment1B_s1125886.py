#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# all this work was done by s1125886 A.Podolako. Maybe you can also give me feedback about the exercise please?
#%%  Exercise 1
# The code below creates a dictionary that contains integers as key, and their double as its values
# Write a code to ask for a key to the user, check if that key exists, and print its value if so.

double = {}

for i in range (100) :
    double [ i ] = 2*i
    
#asks user for key
key = int(input("Please, enter a key: "))

# check if this key exist or no
if key in double:
    #if exist, then prints value
    print ("Exist, and value is" ,(double[key])  )
else:
    #not existind
    print ("Does not exist")

#%%  Exercise 2
# Write a function that receive a dictionary as input and invert the its keys and values. In other words, your function should creates
# another dictionary in which the keys of the input dictionary are now the values, and the values of the input dictionary are now the keys.
# Use the dictionary defined in exercise 1 to test your function.

#creates a dictionary
def dict_convert () :
    #we use double dictionary to check if it works
    user_dict  = double
    
    #create new dict.
    new_dict ={}
    #change values for keys and values
    for k, v in user_dict.items () :
        new_key = v
        new_value = k
        new_dict [new_key] =new_value
    #recieve new dictionary    
    return new_dict
# start of function work
print( dict_convert())

#%%  Exercise 3
#The program below ask the user for the metadata of multiple songs and accumulate them in a list of tuples.
add_song = True
song_list = []
while add_song :

    song_name = input ( " Song name :\ n " )
    song_dur = input ( " Song duration ( min ) :\ n " )
    song_composer = input ( " Song composer :\ n " )
    
    song = ( song_name , song_composer , int ( song_dur ) )
    song_list . append ( song )

    option = input ( " Add another song ? [ yes / no ] " )
    if option != "yes" :
        add_song = False
#Modify that program to print the composer of all the songs in the list after the user finishes adding the songs.
print ("Composer of all songs: ")
# loop allows to print all composers
for song in song_list:
    # song[0]=songname ; song[1]=songcomposer ; song[2]=songduration
    print(song[1])
    
#%%  Exercise 4
#Using the song list defined in the previous exercise, write a program that asks for the name of a song and prints all the information about it,
# if the song is present in the list. If the song is not in the list your program should not crash. 
#Try to handle this error without using a try/except statement.

# The program below ask the user for the metadata of multiple songs and accumulate them in a list of tuples.
add_song = True
song_list = []
while add_song :

    song_name = input ( " Song name :\ n " )
    song_dur = input ( " Song duration ( min ) :\ n " )
    song_composer = input ( " Song composer :\ n " )
    
    song = ( song_name , song_composer , int ( song_dur ) )
    song_list . append ( song )

    option = input ( " Add another song ? [ yes / no ] " )
    if option != "yes" :
        add_song = False
# Modify that program to print the composer of all the songs in the list after the user finishes adding the songs.
print ("Composer of all songs: ")
for song in song_list:
    print(song[1])

# Please to input user for a song
ask_song_name = input("Please, enter the song name: ")

#found sonng is none at the mopment 
found=None
#check if it is existing or no
for song in song_list:
    # if typed name in lowe (to have no problems and errors ) is the same as in the list, then found is that song
    if song[0].lower()==ask_song_name.lower():
        found=song
        
        #if exist, then print info
        if found :
            print ("This song is in the list.")
            print ("The song name is " +found[0] +". The song composer is " +found[1] +". The duration is "+str(found[2]))
        # if not , then print this message
        else:
            print ("This song is NOT in the list.")
            
#%%  Exercise 5
#Transform the list of tuple from exercise 3 into a dictionary in which the keys are the song names and the values are tuples with the rest
# of the information. Then write a code to ask for a song name and print the duration of that given song.
add_song = True
song_list = []
while add_song :

    song_name = input ( " Song name :\ n " )
    song_dur = input ( " Song duration ( min ) :\ n " )
    song_composer = input ( " Song composer :\ n " )
    
    song = ( song_name , song_composer , int ( song_dur ) )
    song_list . append ( song )

    option = input ( " Add another song ? [ yes / no ] " )
    if option != "yes" :
        add_song = False
        
#creates a dictionary
song_dict={}
#define info for keys and values in dictionary
for song in song_list:
    song_name = song[0]
    song_info = (song[1],song[2])
    song_dict [song_name]= song_info
    
print(song_dict)
#asks to type the name of somg
user_ask_song_name =input("Please, enter songs name: ")
#checks if it exists or no, if yes, then we can get info about that song
if user_ask_song_name in song_dict.keys():
    #if exist, then prints value
    print ("Exist, there is info " + (str(song_dict[user_ask_song_name])) )
else:
    #not existind
    print ("Does not exist")
#%% Problem 1 Assignment1A
def add_entry(contacts: dict, name: str, phone: str, birthdate: tuple):
    """
    Add a new contact to the dictionary

    Parameters
    ----------
    contacts : dict
        Dictionary containing of the known contacts. The keys of the dictionary
        are str containing the name of the contact. The values are a list with
        a str containing the contact's phone number as the first element, and a tuple 
        containing the contact's birth date in the format (dd, mm) as second element.
    name : str
        Name of the new contact.
    phone : str
        Phone of the new contact.
    birthdate : tuple
        Birthdate of the new contact.

    Returns
    -------
    contacts : dict
        The updated dictionary after adding the new contact.

    """
    
    if name in contacts or not (1 <= birthdate[0] <= 31 and 1 <= birthdate[1] <= 12) or len(phone) != 9:
        return contacts

    contacts[name] = [phone, birthdate]
    return contacts


def change_entry(contacts: dict, name: str, new_phone: str):
    """
    Change the phone number of an existing entry in the contact dictionary.

    Parameters
    ----------
    contacts : dict
        Dictionary containing known contacts.
    name : str
        Name of the contact to change.
    new_phone : str
        New phone number.

    Returns
    -------
    contacts : dict
        The updated dictionary.

    """
    
    if name not in contacts or( len(new_phone) != 9):
        return contacts
    
    if name in contacts:
        contacts[name][0] = new_phone
        return contacts



def delete_entry(contacts: dict, name: str):
    """
    Delete the specified entry if it exists in the contact dictionary.

    Parameters
    ----------
    contacts : dict
        Dictionary containing known contacts.
    name : str
        Name of the contact to delete.

    Returns
    -------
    contacts : dict
        The updated dictionary.
    """
  
    if name in contacts:
        del contacts[name] 
    return contacts
    
def find_phone(contacts: dict, name: str):
    """
    Return the phone number of the contact specified by name, if it exists.

    Parameters
    ----------
    contacts : dict
        Dictionary containing known contacts.
    name : str
        Name of the contact.

    Returns
    -------
    str or None
        The phone number if the contact exists, None otherwise.
    """
    return contacts.get(name, [None])[0]
    

def list_all_names(contacts: dict):
    """
    Return a list of strings containing all the names in the contact dictionary.

    Parameters
    ----------
    contacts : dict
        Dictionary containing known contacts.

    Returns
    -------
    list
        List of strings containing all the names in the contact dictionary.
    """
    return list(contacts.keys())
 

def month_birthdays(contacts: dict, date: tuple):
    """
    Return a list of tuples containing the names and days of contacts with birthdays in the current month.

    Parameters
    ----------
    contacts : dict
        Dictionary containing known contacts.
    date : tuple
        Current day and month.

    Returns
    -------
    list
        List of tuples containing names and days of contacts with birthdays.
    """
    
    return  [(name, contacts[name][1][0]) for name in contacts if contacts[name][1][1] == date[1]]

def ask_input(text, options):
    """
    Display the input options and ask the user for input.

    Parameters
    ----------
    text : str
        The text to display.
    options : dict
        Dictionary containing the options.

    Returns
    -------
    str
        The user's input.
    """
    print(text)
    for key, value in options.items():
        print(f"{key} - {value}")
    return input("Choose an option: ")
   
def parse_input(usr_opt):
    """
    Parse user input into integer.

    Parameters
    ----------
    usr_opt : str
        User input.

    Returns
    -------
    int
        Parsed integer or None if parsing fails.
    """
    try:
        return int(usr_opt)
    except ValueError:
        return None
   
    
def main():
   contacts = {}
   while True:
    options = {1: "Add entry", 
               2: "Change entry", 
               3: "Delete entry", 
               4: "Find phone",
               5: "Month birthdays", 
               6: "List names", 
               7: "Exit"}
    
    choose_option = ask_input("Choose an option: ", options)
    parsed_choice = parse_input(choose_option)
    
    if parsed_choice is None or parsed_choice < 1 or parsed_choice > 7:
        print("Please enter a number from 1 to 7")
        continue
    
    if parsed_choice == 1 :
        name = input("Enter name: ")
        phone = input("Enter phone (9 digits): ")
        day = int(input("Enter birth day: "))
        month = int(input("Enter birth month: "))
        birthdate = (day, month)

        contacts = add_entry(contacts, name, phone, birthdate)
        
    elif parsed_choice == 2 :
        name = input("Enter name: ")
        phone = input("Enter new phone (9 digits): ")

        contacts = change_entry(contacts, name, phone)
        
    elif parsed_choice == 3 :
       name = input("Enter name: ")
      
       contacts = delete_entry(contacts, name)
        
    elif parsed_choice == 4 :
       name = input("Enter name: ")
      
       phone =  find_phone(contacts, name)
     
       if phone is not None:
           print(f"The phone number for {name} is {phone}")
       else:
           print(f"Contact with name {name} not found.")
            
    elif parsed_choice == 5 :         
       day = int(input("Enter current day: "))
       month = int(input("Enter current month: "))
       date = (day, month)

       birthdays = month_birthdays(contacts, date)
       print("Birthdays this month:")
       for name, day in birthdays:
           print(f"{name}:{day}")
           
    elif parsed_choice == 6 :
        names = list_all_names(contacts)
        if not names:
            print("Contact dictionary is empty.")
        else:
            print("All names in the contact dictionary:")
            for name in names:
                print(name)

            
    elif parsed_choice == 7 :
        print("Exit")
        break
        
# The main body of your program should only call the main() function like this:
if __name__=="__main__":    
    main()
    
    
#%% Problem 2 Assignment1A
def read_database(filename='movie_dataset.txt'):
    """Reading from a text file and creating a database using a dictionary.

    This function reads a text file with movies, each entry on a new line with the following format:
    "_title_of_the_movie_" _rating_ _duration_in_minutes_
    The title of the movie might be several words long.
    The rating is a float, and the duration is an integer representing minutes.
    The function creates a dictionary with keys as movie titles and values as tuples of
    the respective rating and duration. If two movie entries have the same title,
    the movie with the longer duration should be kept. If the filename is invalid
    (the file does not exist), the program returns None.

    Parameters:
        filename (str): The name of the file to be read, default = "movie_dataset.txt"

    Returns:
        dict: A dictionary with movie names as keys and a tuple containing the movie
        rating and duration of each movie as a value.
    """
    movies = {}  # Create an empty dictionary to store movie information

    open_file = open(filename, 'r') 
    
    for line in open_file:
        parts = line.rsplit(' ', 2) #rsplit- splits the line into three parts, ensuring that we only split the rating and duration at the last space in case the movie title contains spaces 
        title = parts[0][1:-1]  # [1:-1] means without quotes
        rating = float(parts[1])
        duration = int(parts[2])
            
        movies[title] = (rating, duration)

    
    return movies


def movie_title_list(movies: dict):
    """Get a list of movie titles from the provided dictionary.

    Parameters:
        movies (dict): A dictionary with movie names as keys and values as tuples
        containing the movie rating and duration.

    Returns:
        list: A list of strings containing all the movie titles.
    """
    return list(movies.keys())


def avg_duration(movies: dict, rating: float):
    """Compute and return the average duration of movies with ratings above the given parameter rating.

    If no movies have the above rating, the function returns None.
    If a movie has a duration of 0 minutes, that movie should not be included when computing the average duration.

    Parameters:
        movies (dict): A dictionary with movies and their respective rating and duration.
        rating (float): The minimum rating for filtering movies.

    Returns:
        float or None: The average duration of movies with ratings above the given parameter rating,
        or None if no such movies are found.
    """
    filtered_onrating_movies = [] 

    for (rat, dur) in movies.values(): 
        if rat > rating and dur > 0:  
            filtered_onrating_movies.append((dur, rat))  
    
    if not filtered_onrating_movies:  
        return None
    
    sum=0
    for (dur, _) in filtered_onrating_movies: #(dur, _) = _ means that we do not use the rat( we do not need that here)
        sum += dur 
    avg_dur= sum/ len(filtered_onrating_movies)
    return avg_dur


def best_rated_movie(movies: dict, min_dur: int, max_dur: int,choose_shortest: bool ):#
    """Return the movie title with the highest rating within the given duration range.

    The optional parameter choose_shorter is a boolean that indicates what to do in case of a tie.
    If choose_shortest is True, the shortest movie is returned in case of a tie in the ratings.
    Otherwise, the longest one is returned.
    In case no movies in the dictionary fulfill the requirements, the function should return None.

    Parameters:
        movies (dict): A dictionary with movies and their respective rating and duration.
        min_dur (int): The minimum duration for filtering movies.
        max_dur (int): The maximum duration for filtering movies.
        choose_shortest (bool): If True, choose the shortest movie in case of a tie; otherwise, choose the longest.

    Returns:
        str or None: The title of the best-rated movie within the given duration range,
        or None if no such movies are found.
    """
    filtered_onduration_movies = []
     
    for (title, (rat, dur)) in movies.items():
        if min_dur <= dur and dur <= max_dur:
            filtered_onduration_movies.append((title, (rat, dur)))

    if not filtered_onduration_movies:
        return None

    
    movies_best_rating_fromall = []
     
    rating=0
    for (title, (rat, dur)) in filtered_onduration_movies:
        if rat >= rating:
            movies_best_rating_fromall.append((title, (rat, dur)))
            rating=rat
            for (title, (rat, dur)) in movies_best_rating_fromall:
                if rat < rating:
                    movies_best_rating_fromall.remove((title, (rat, dur)))

    duration = float('inf')  
    shortest_movie=  []
    length_movie=[]
    for (title, (rat, dur)) in movies_best_rating_fromall:
        if dur < duration:
            shortest_movie.append((title, (rat, dur)))
            duration = dur
            if dur > duration:
                length_movie.append((title, (rat, dur)))
                duration = dur
    print(movies_best_rating_fromall)        
    print(shortest_movie)
    print(length_movie)     
    if choose_shortest:
        return shortest_movie[0][0]
    
    else:
        return length_movie[0][0]


def main():
    """Main function to interact with the user and execute chosen options."""
    movie_dict = read_database("movie_dataset.txt")

    print("Choose one of the below options",
          "1: print all the movie titles in our dataset",
          "2: compute average duration above a rating (e.g. '2 8.8')",
          "3: find the rating of a movie (e.g. '3 Coco')",
          "4: find the best-rated movie within a given duration range (e.g. '4 60 120 True')",
          sep='\n ')
    
    user_input = input()
    user_input = user_input.split()
    
    if len(user_input) == 1 and user_input[0] == '1':
        movie_names = movie_title_list(movie_dict)
        for name in movie_names:
            print(name)
        return
    
    elif len(user_input) == 2 and user_input[0] == '2':
        print(avg_duration(movie_dict, float(user_input[1])))
        return
    
    elif len(user_input) >= 2 and user_input[0] == '3':
        movie_name = " ".join(user_input[1:])
        print(movie_name)
        if movie_name in movie_dict:
            print(movie_dict[movie_name][0])
        else:
            print("Movie not found.")
        return
    
    elif len(user_input) == 4 and user_input[0] == '4':
        min_duration = int(user_input[1])
        max_duration = int(user_input[2])
        flag = bool(user_input[3])
        result = best_rated_movie(movie_dict, min_duration, max_duration,flag )
        if result:
            print(result)
        else:
            print("No movie found within the specified duration range.")
    
    else:
        print("Wrong input")
        return


if __name__ == '__main__':
    main()
