import os

def read_database(filename='movies_v2.txt'):
    """
    Read data from a text file and store it in a dictionary.

    Args:
    - filename (str): The name of the file to read. Default is 'movies_v2.txt'.

    Returns:
    - dict: A dictionary containing movie information.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, filename)
    
    movies_dict = {}  # Create an empty dictionary to store movie information

    # Open the file in read mode
    open_file = open(filename, 'r') 
    try:
        with open(file_path, 'r') as open_file:
            # Iterate through each line in the file
            for line in open_file:
                # Split the line into parts using ',' as a delimiter
                parts = line.rsplit(',', 5)  

                # Extract information from the parts
                name = parts[0]
                rating = float(parts[1])
                duration = int(parts[2])
                year = int(parts[3])
                genre = parts[4]
                gross_income = int(parts[5])

                # Add the movie information to the dictionary
                movies_dict[name] = (rating, duration, year, genre, gross_income)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        
    # Return the dictionary containing movie information
    return movies_dict
