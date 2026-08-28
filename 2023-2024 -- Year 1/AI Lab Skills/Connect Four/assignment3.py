#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Artificial Intelligence Lab Skills
Assignment 3: Connect Four

Author(s): Angelina Podolako
Group: 119
Contributor(s): 
Average hours spent per person: Friday 13:30-17:30 + Mon 12:00-23:59
"""

import random

class Player:
    """
    Represents a player in the Connect Four game.

    Attributes:
    - symbol (str): The symbol ('o' or 'x') associated with the player.
    - name (str): The name of the player.
    """
    def __init__(self, symbol):
        """
        Initializes a player with the given symbol and prompts for a name.

        Parameters:
        - symbol (str): The symbol ('o' or 'x') associated with the player.
        """
        self.symbol = symbol
        self.set_name()

    def set_name(self):
        """Prompts the player to enter their name."""
        pass

    def get_name(self):
        """Returns the name of the player."""
        return self.name
    
    def __str__(self):
        """Returns the symbol representing the player."""
        return self.symbol

    def __eq__(self, other):
        """
        Checks if two Player objects are equal based on their symbols.

        Parameters:
        - other (Player): The other Player object to compare.

        Returns:
        - bool: True if symbols are equal, False otherwise.
        """
        if isinstance(other, Player):
            return self.symbol == other.symbol
        return False

class HumanPlayer(Player):
    """
    Represents a human player in the Connect Four game.

    Inherits from Player.

    Methods:
    - set_name: Prompts the player to enter their name.
    - play: Allows the player to input a column for their move.
    """
    def set_name(self):
        """Prompts the human player to enter their name."""
        self.name = input(f"Player {self.symbol}, what is your name? ")
    
    def play(self):
        """
        Allows the human player to input a column for their move.

        Returns:
        - int: The selected column for the move.
        """
        try:
            user_column = int(input(f"{self.name} ('{self.symbol}'): Which column do you want to play? "))
            return user_column
        except ValueError:
            print("ValueError! -> Invalid input. Please enter a valid integer for the column.")

class RandomComputerPlayer(Player):
    """
    Represents a computer player with random move selection in the Connect Four game.

    Inherits from Player.

    Methods:
    - set_name: Sets the name of the computer player to 'RandomAI'.
    - play: Generates a random column for the computer's move.
    """
    def set_name(self):
        """Sets the name of the computer player to 'RandomAI'."""
        self.name = "RandomAI"
        
    def play(self):
        """
        Generates a random column for the computer's move.

        Returns:
        - int: A randomly selected column for the move.
        """
        random_column = random.randint(1, 7)
        return random_column

class Board:
    """
    Represents the game board in the Connect Four game.

    Attributes:
    - width (int): The number of columns in the board.
    - height (int): The number of rows in the board.
    - board (list): A 2D list representing the game board.

    Methods:
    - reset_board: Resets the game board to an empty state.
    - __str__: Returns a string representation of the game board.
    - get_column_height: Returns the number of occupied rows in a given column.
    - play: Places a player's symbol in a specified column.
    - is_full: Checks if the game board is full.
    - is_winner: Checks if a player has won based on their move in a specific column.
    """
    def __init__(self, width=7, height=6):
        """
        Initializes a game board with the specified width and height.

        Parameters:
        - width (int): The number of columns in the board.
        - height (int): The number of rows in the board.
        """
        self.width = width
        self.height = height
        self.reset_board()
        
    def reset_board(self):
        """Resets the game board to an empty state."""
        self.board = [[None for _ in range(self.width)] for _ in range(self.height)]

    def __str__(self):
        """Returns a string representation of the game board."""
        column_numbers = " ".join(str(col) for col in range(self.width))
        
        rows = []
        for row in self.board:
            row_str = " ".join(str(cell) if cell is not None else "." for cell in row)
            rows.append(row_str)
        
        board_str = column_numbers + "\n" + "\n".join(rows)
        return board_str
    
    def get_column_height(self, column):
        """
        Returns the number of occupied rows in a given column.

        Parameters:
        - column (int): The column number to check.

        Returns:
        - int: The number of occupied rows in the specified column.
        """
        height = 0
        assert 0 <= column <= self.width, "Invalid column number"

        for row in self.board:
            if row[column] is not None:
                height += 1
                
        return height
    
    def play(self, column, player):
        """
        Places a player's symbol in a specified column.

        Parameters:
        - column (int): The column in which the player wants to play.
        - player (Player): The player making the move.
        """
        assert 0 <= column <= self.width, "Invalid column number"
        assert not self.is_full(), "Board is full"
                
        empty = self.height - self.get_column_height(column)
                
        for row in range(empty- 1, -1, -1):
            if self.board[row][column] is None:
                self.board[row][column] = player
                break      
    
    def is_full(self):
        """Checks if the game board is full."""
        return all(row is not None for col in self.board for row in col)
    
    # Inside the Board class
    def is_winner(self, column, player):
        column_height = self.get_column_height(column)

        for i in range(4):  # for different cases: Horizontal, Vertical, Diagonal Top-Left to Bottom-Right, Diagonal Bottom-Left to Top-Right
            counter = 1
            column_index = column
            row_index_last_piece = self.height - column_height

            # Case 1: Horizontal
            if i == 0:
                # First left
                while column_index > 0:
                    column_index -= 1
                    if 0 <= row_index_last_piece < self.height and 0 <= column_index < self.width and player == self.board[row_index_last_piece][column_index]:
                        counter += 1
                    else:
                        break
                    if counter == 4:
                        return True
                # Then right
                column_index = column
                while column_index < self.width - 1:
                    column_index += 1
                    if 0 <= row_index_last_piece < self.height and 0 <= column_index < self.width and player == self.board[row_index_last_piece][column_index]:
                        counter += 1
                    else:
                        break
                    if counter == 4:
                        return True

            # Case 2: Vertical
            elif i == 1 and column_height >= 4:
                for j in range(1, 4):  # because counter starts at 1
                    if 0 <= column_index < self.width and 0 <= row_index_last_piece + j < self.height and player == self.board[row_index_last_piece + j][column_index]:
                        counter += 1  # if consecutive piece is found
                    else:
                        break
                    if counter == 4:
                        return True

            # Case 3: Diagonal Top-Left to Bottom-Right
            elif i == 2:
                # First to the top left
                while column_index > 0 and row_index_last_piece > 0:
                    column_index -= 1
                    row_index_last_piece -= 1
                    if 0 <= column_index < self.width and 0 <= row_index_last_piece < self.height and player == self.board[row_index_last_piece][column_index]:
                        counter += 1  # if consecutive piece is found
                    else:
                        break
                    if counter == 4:
                        return True
                # Then to the bottom right
                column_index = column
                row_index_last_piece = self.height - column_height
                while column_index < self.width - 1 and row_index_last_piece < self.height - 1:
                    column_index += 1
                    row_index_last_piece += 1
                    if 0 <= column_index < self.width and 0 <= row_index_last_piece < self.height and player == self.board[row_index_last_piece][column_index]:
                        counter += 1  # if consecutive piece is found
                    else:
                        break
                    if counter == 4:
                        return True

            # Case 4: Diagonal Bottom-Left to Top-Right
            else:
                # First to the bottom left
                while column_index > 0 and row_index_last_piece < self.height - 1:
                    column_index -= 1
                    row_index_last_piece += 1
                    if 0 <= column_index < self.width and 0 <= row_index_last_piece < self.height and player == self.board[row_index_last_piece][column_index]:
                        counter += 1  # if consecutive piece is found
                    else:
                        break
                    if counter == 4:
                        return True
                # Then to the top right
                column_index = column
                row_index_last_piece = self.height - column_height
                while column_index < self.width - 1 and row_index_last_piece > 0:
                    column_index += 1
                    row_index_last_piece -= 1
                    if 0 <= column_index < self.width and 0 <= row_index_last_piece < self.height and player == self.board[row_index_last_piece][column_index]:
                        counter += 1  # if consecutive piece is found
                    else:
                        break
                    if counter == 4:
                        return True

        return False



class ConnectFour:
    """
    Represents the Connect Four game.

    Attributes:
    - board (Board): The game board.
    - players (dict): A dictionary containing the players ('o' and 'x') and their names.
    - round_number (int): The current round number.
    """
    def __init__(self):
        """Initializes the Connect Four game with an empty board and players."""
        self.board = Board()
        self.players = {}
        self.round_number = 0
        
    def play(self):
        """Starts and manages the Connect Four game."""
        print("Player o, what is your name?")
        player_o_name = input()
        
        print("Player x, what is your name?")
        player_x_name = input()
        
        self.players = {"o": player_o_name, "x": player_x_name}
        
        while True:
            self.round_number += 1
            
            self.board.reset_board()
            
            print(self.board)
            
            while True:
                print("-" * 10)
                
                if self.round_number % 2 != 0:
                    current_player = "o"  
                else:
                    current_player = "x"
                
                print(f"This is round {self.round_number}. {self.players[current_player]} ('{current_player}') it is your turn!")

                try:
                    column = int(input(f"{self.players[current_player]} ('{current_player}'): Which column do you want to play? "))
                    self.board.play(column, current_player)
                    print(self.board)

                    if self.board.is_winner(column, current_player):
                        print(f"Player {self.players[current_player]} ('{current_player}') won the game!")
                        break

                    if self.board.is_full():
                        print("The game resulted in a draw!")
                        break

                    self.round_number += 1

                except (ValueError, AssertionError) as e:
                    print(f"Invalid input! {e}")

            play_again = input("Do you want to play another game? [y/n] ")
            if play_again.lower() != 'y':
                print("Goodbye!")
                break

# Run the game
if __name__ == "__main__":
    game = ConnectFour()
    game.play()
