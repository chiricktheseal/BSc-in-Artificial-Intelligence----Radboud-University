#functions_part1.py
from array import array

# Function to add a movie to the database
def add_movie(movie_dict:dict, name: str ,rating :float, duration: int, year: int , genre: str , gross_income:int):
    """
    Add a movie to the database.

    Args:
    - movie_dict (dict): The dictionary representing the movie database.
    - name (str): The name of the movie.
    - rating (float): The rating of the movie.
    - duration (int): The duration of the movie.
    - year (int): The year of the movie.
    - genre (str): The genre of the movie.
    - gross_income (int): The gross income of the movie.

    Returns:
    - dict: The updated movie database.
    """
    # Check if the movie already exists in the database
    if name in movie_dict:
        return movie_dict

    # Add the new movie information to the dictionary
    movie_dict[name] = (rating, duration, year, genre, gross_income)
    return movie_dict


# Function to find information about a specific movie in the database
def find_movie_by_name(movie_dict: dict, name: str):
    """
Find information about a specific movie in the database.

Args:
- movie_dict (dict): The dictionary representing the movie database.
- name (str): The name of the movie to search for.

Returns:
- dict or None: A dictionary with movie information if found, otherwise None.
"""
    movie_info = movie_dict.get(name)
    
    if movie_info is not None:
        # Extract information from the tuple and return as a dictionary
        rating, duration, year, genre, gross_income = movie_info
        return {'name': name, 'rating': rating, 'duration': duration, 'year': year, 'genre': genre, 'gross_income': gross_income}
    else:
        return None
 
    
# Function to find movies based on rating and year range
def find_movies_by_rating_and_year(movie_dict, min_rating, max_rating, start_year, end_year): 
    """
Find movies based on rating and year range.

Args:
- movie_dict (dict): The dictionary representing the movie database.
- min_rating (float): The minimum rating of the movies to find.
- max_rating (float): The maximum rating of the movies to find.
- start_year (int): The start year of the range.
- end_year (int): The end year of the range.

Returns:
- list: A list of dictionaries containing information about matching movies.
"""
    matching_movies = []
    # Iterate through each movie in the database
    for name, (rating, duration, year, genre, gross_income) in movie_dict.items():
        # Check if the movie's rating and year fall within the specified range
        if min_rating <= rating <= max_rating and start_year <= year <= end_year:
            matching_movies.append({"name": name, "rating": rating, 'duration': duration, 'year': year, 'genre': genre, 'gross_income': gross_income})

    return matching_movies


# Function to find movies by genre
def find_movies_by_genre(movie_dict, user_genre):
    """
  Find movies based on a specified genre.

  Args:
  - movie_dict (dict): The dictionary representing the movie database.
  - user_genre (str): The genre to search for.

  Returns:
  - dict: A dictionary where keys are genres and values are lists of movies in that genre.
  """
    matching_movies = {}

      # Iterate through each movie in the database
    for name, (rating, duration, year, genre, gross_income) in movie_dict.items():
        # Check if the specified genre is present in the movie's genre
        if user_genre.lower() in genre.lower():
            movie_info = (name, rating, duration, year)
            # Add the movie information to the matching_movies dictionary
            if genre not in matching_movies:
                matching_movies[genre] = [movie_info]
            else:
                matching_movies[genre].append(movie_info)

    return matching_movies


# Function to get sorted years and associated movies
def get_sorted_years_and_movies(movie_dict):
    """
    Get a dictionary with years as keys and lists of movies for each year as values.

    Args:
    - movie_dict (dict): The dictionary representing the movie database.

    Returns:
    - dict: A dictionary where keys are years and values are lists of dictionaries containing movie information.
    """
    years_array = array('i', [])  # Create an array to store unique years
    years_movies_dict = {}  # Create a dictionary to store movies grouped by year

    # Iterate through each movie in the database
    for name, (_, _, year, _, _) in movie_dict.items():
        # Check if the year is not already in the array
        if year not in years_array:
            years_array.append(year)

    years_array = sorted(years_array)  # Sort the years in ascending order

    # Iterate through each unique year
    for year in years_array:
        movies_for_year = []
        # Iterate through each movie in the database
        for name, (rating, _, movie_year, genre, _) in movie_dict.items():
            # Check if the movie's year matches the current year
            if movie_year == year:
                movies_for_year.append({'name': name, 'rating': rating})

        # Add the list of movies for the current year to the dictionary
        years_movies_dict[year] = movies_for_year

    return years_movies_dict

