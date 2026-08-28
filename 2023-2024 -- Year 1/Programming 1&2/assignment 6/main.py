#main.py
import database
import functions_part1
import functions_part2
from array import array
import numpy as np
import matplotlib.pyplot as plt


# Function to display a menu and get user input
def ask_input(text, options):
    """
    Display a menu and prompt the user to choose an option.

    Args:
    - text (str): The prompt to display.
    - options (dict): A dictionary containing menu options.

    Returns:
    - str: The user's choice.
    """
    print(text)
    for key, value in options.items():
        print(f"{key} - {value}")
    return input("\nChoose an option: ")

# Function to parse user input as an integer
def parse_input(usr_opt):
    """
    Parse user input as an integer.

    Args:
    - usr_opt (str): The user's input.

    Returns:
    - int or None: Parsed integer or None if parsing fails.
    """
    try:
        return int(usr_opt)
    except ValueError:
        return None

# Main function to manage the movie database application   
def main():
    
    # Set the filename for the movie database
    filename = 'movies_v2.txt'
    # Read the movie database from the file
    movies_in_dict = database.read_database(filename)
    #print(database.read_database(filename)) #to check if it works
    
    
    while True:
        options = {1: "Add movie", 
                   2: "Find movie by name",
                   3: "Show movies of year and rating ", 
                   4: "Sort by genre", 
                   5: "Sort from old to new films",
                   6: "Random array (rating) - sample_array",
                   7: "Array with rating sorted from min to max - sort_array",
                   8: "Graph with sorted and unsorted ratings - plot_sorting",
                   9: "- time_sorting",
                   10: "Exit"}
        # Get user input for menu choice
        choose_option = ask_input("Choose an option: ", options)
        parsed_choice = parse_input(choose_option)
         # Validate user input
        if parsed_choice is None or parsed_choice < 1 or parsed_choice > 10:
            print("Please enter a number from 1 to 10")
            continue
         # Execute the chosen functionality based on user input
        if parsed_choice == 1 :
            # Add a new movie to the database
            name = input("Enter name: ")
            rating = float(input("Enter rating (can be float): "))
            duration = int(input("Enter duration (in min, e.g. 122): "))
            year = int(input("Enter year: "))
            genre = str(input("Enter genre: "))
            gross_income = int(input("Enter gross income: "))
            # Update the movie database
            movies_in_dict = functions_part1.add_movie(movies_in_dict, name, rating, duration,year,genre, gross_income)

        elif parsed_choice == 2:
            # Find and display information about a movie by name
            name = input("Enter name: ")
            
            movie_info = functions_part1.find_movie_by_name(movies_in_dict, name)
            
            if movie_info is not None:
                print(f"There's info for movie {name}:\n"
                      f"rating is {movie_info['rating']}\n"
                      f"duration is {movie_info['duration']}\n"
                      f"year is {movie_info['year']}\n"
                      f"genre is {movie_info['genre']}\n"
                      f"gross income is {movie_info['gross_income']}\n")
            else:
                print(f"Movie with name {name} not found.")

        elif parsed_choice == 3:
            # Show movies based on specified rating and year range
            min_rating = float(input("Enter minimum rating: "))
            max_rating = float(input("Enter maximum rating: "))
            start_year = int(input("Enter start year: "))
            end_year = int(input("Enter end year: "))
            
            # Find and display matching movies
            matching_movies = functions_part1.find_movies_by_rating_and_year(movies_in_dict, min_rating, max_rating, start_year, end_year)

            if matching_movies:
                print("Matching Movies:")
                for movie in matching_movies:
                    print(movie)
            else:
                print("No matching movies found.")


        elif parsed_choice == 4:
            # Sort movies by specified genre and display
            user_genre = input("Enter a genre to search for: ")
        
            matching_movies = functions_part1.find_movies_by_genre(movies_in_dict, user_genre)
        
            if matching_movies:
                print("Matching Movies:")
                for genre, movies_info in matching_movies.items():
                    print(f"Genre: {genre}")
                    
                    for movie_info in movies_info:
                        name, rating, duration, year = movie_info
                        print(f"  - Movie: {name}")
                        print(f"    Rating: {rating}")
                        print(f"    Duration: {duration}")
                        print(f"    Year: {year}")
            else:
                print("No matching movies found.")


        
        elif parsed_choice == 5:
            # Call the function to get sorted years and associated movies and ratings
            sorted_years_movies_dict = functions_part1.get_sorted_years_and_movies(movies_in_dict)
    
            # Print the result
            for year, movies_for_year in sorted_years_movies_dict.items():
                print(f"Year: {year}")
                for movie_info in movies_for_year:
                    print(f"  - Movie: {movie_info['name']}")
                    print(f"    Rating: {movie_info['rating']}")
        
        
        elif parsed_choice == 6: 
            # Generate a random array of movie ratings
            movie_ratings = np.array(list(movies_in_dict.values()))[:, 0]
            
            # Get the number of samples from the user
            num_samples = int(input("Enter the number of samples: "))
            if num_samples <= 0:
                print("Please enter a positive number for the samples.")
            else:
                # Sample the movie ratings array and display the result
                sampled_ratings = functions_part2.sample_array(movie_ratings, num_samples)
                print("Sampled Ratings:", sampled_ratings)
         
        elif parsed_choice == 7 :
            # Get the movie ratings array
            movie_ratings = np.array(list(movies_in_dict.values()))[:, 0]
            
            # Display the unsorted and sorted movie ratings arrays
            print("There is unsorted array:\n", movie_ratings)
            print("There is sorted array from min to max:\n", functions_part2.sort_array(movie_ratings))
            
        elif parsed_choice == 8 :
            movie_ratings = np.array(list(movies_in_dict.values()))[:, 0]
            # Plot and display the sorted and unsorted ratings
            functions_part2.plot_sorting(movie_ratings)
            
        elif parsed_choice == 9:
            # Sample data for time_sorting
            data_for_timing = np.random.randint(1, 100, 1000)  
            sizes_for_timing = np.arange(10, 101, 10)  
            
            # Call the time_sorting function
            sorting_times = functions_part2.time_sorting(sizes_for_timing, data_for_timing)
            
            # Print and plot the results
            print("Sorting Times for Different Sizes:")
            for size, sorting_time in zip(sizes_for_timing, sorting_times):
                print(f"Size: {size}, Sorting Time: {sorting_time:.6f} seconds")
            
            plt.plot(sizes_for_timing, sorting_times, marker='o')
            plt.title('Sorting Time vs. Subsample Size')
            plt.xlabel('Subsample Size')
            plt.ylabel('Sorting Time (seconds)')
            plt.show()
            
        elif parsed_choice == 10:
            # Exit the application
            print("Exit")
            break


## Entry point of the program
if __name__ == '__main__':
    main()
