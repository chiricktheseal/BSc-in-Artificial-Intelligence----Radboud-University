"""
authors: Angelina and Maria (group 53)
"""
from __future__ import annotations
from abc import abstractmethod
import numpy as np
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from heuristics import Heuristic
    from board import Board


class PlayerController:
    """Abstract class defining a player
    """
    def __init__(self, player_id: int, game_n: int, heuristic: Heuristic) -> None:
        """
        Args:
            player_id (int): id of a player, can take values 1 or 2 (0 = empty)
            game_n (int): n in a row required to win
            heuristic (Heuristic): heuristic used by the player
        """
        self.player_id = player_id
        self.game_n = game_n
        self.heuristic = heuristic


    def get_eval_count(self) -> int:
        """
        Returns:
            int: The amount of times the heuristic was used to evaluate a board state
        """
        return self.heuristic.eval_count
    

    def __str__(self) -> str:
        """
        Returns:
            str: representation for representing the player on the board
        """
        if self.player_id == 1:
            return 'X'
        return 'O'
        

    @abstractmethod
    def make_move(self, board: Board) -> int:
        """Gets the column for the player to play in

        Args:
            board (Board): the current board

        Returns:
            int: column to play in
        """
        pass

class MinMaxPlayer(PlayerController):
    """Class for the minmax player using the minmax algorithm
    Inherits from Playercontroller
    """
    def __init__(self, player_id: int, game_n: int, depth: int, heuristic: Heuristic) -> None:
        """
        Args:
            player_id (int): id of a player, can take values 1 or 2 (0 = empty)
            game_n (int): n in a row required to win
            depth (int): the max search depth
            heuristic (Heuristic): heuristic used by the player
        """
        super().__init__(player_id, game_n, heuristic)
        self.depth: int = depth


    def make_move(self, board: Board) -> int:
        """Gets the column for the player to play in using the Minmax algorithm.

        Args:
            board (Board): the current board

        Returns:
            int: column to play in
        """

        # Use minimax to get the best move
        _, best_column = self.minmax(board, self.depth, self.player_id)

        # Return the best move
        return best_column

    
    def minmax(self, board: Board, depth: int, player: int):
        """Minmax recursive algorithm for evaluating game states.

        Args:
            board (Board): Current board state.
            depth (int): Depth of search.
            player (int): The current player (either 1 or 2).

        Returns:
            tuple: (score, best_column)
        """
        # Determining the ID of the opponent based on the current player
        if player == 1:
            opponent = 2
        else:
            opponent = 1

        # Base case
        if depth == 0 or board.is_valid == False or self.heuristic.winning(board.board_state, self.game_n) != 0:
            return self.heuristic.evaluate_board(player, board), None

        # Recursive Call
        
        # Player is Maximizing player
        if player == self.player_id:
            max_eval = -np.inf
            
            for col in range(board.width):
                if board.is_valid(col):
                    new_board = board.get_new_board(col, player)
                    
                    evaluation, _ = self.minmax(new_board, depth - 1, opponent)
                    
                    # updating the max score
                    if evaluation > max_eval:
                        max_eval = evaluation
                        best_column = col
                    
            return max_eval, best_column

        # Player is Minimizing Player
        else:  
            min_eval = np.inf
            
            for col in range(board.width):
                if board.is_valid(col):
                    new_board = board.get_new_board(col, player)
                    
                    evaluation, _ = self.minmax(new_board, depth - 1, opponent)
                    
                    # updating the min score
                    if evaluation < min_eval:
                        min_eval = evaluation
                        best_column = col
                    
            return min_eval, best_column
    

class AlphaBetaPlayer(PlayerController):
    """Class for the minmax player using the minmax algorithm with alpha-beta pruning
    Inherits from Playercontroller
    """
    def __init__(self, player_id: int, game_n: int, depth: int, heuristic: Heuristic) -> None:
        """
        Args:
            player_id (int): id of a player, can take values 1 or 2 (0 = empty)
            game_n (int): n in a row required to win
            depth (int): the max search depth
            heuristic (Heuristic): heuristic used by the player
        """
        super().__init__(player_id, game_n, heuristic)
        self.depth: int = depth
        
        
    def minmax_abp(self, board: Board, depth: int, alpha: float, beta: float, player: int):
        """Minimax algorithm with alpha-beta pruning to evaluate the best move
        
        Args:
            board (Board): the current board
            depth (int): current depth in tree
            alpha (float): the best score that the maximizing player can guarantee
            beta (float): the best score that the minimizing player can guarantee
            player (int): The current player (either 1 or 2).
        
        Returns:
            tuple: (score, best_column)
        """
        if player == 1:
            opponent = 2
        else:
            opponent = 1

        # Base case
        if depth == 0 or board.is_valid == False or self.heuristic.winning(board.board_state, self.game_n) != 0:
            return self.heuristic.evaluate_board(player, board), None

        # Recursive Call
        
        # Player is Maximizing player
        if player == self.player_id:
            max_eval = -np.inf
            
            for col in range(board.width):
                if board.is_valid(col):
                    new_board = board.get_new_board(col, player)
                    
                    evaluation, _ = self.minmax_abp(new_board, depth - 1, alpha, beta, opponent)
                    
                    # updating the max score
                    if evaluation > max_eval:
                        max_eval = evaluation
                        best_column = col
                    
                    # updating alpha
                    alpha = max(alpha, evaluation)
                    # Pruning
                    if beta <= alpha: # Beta cut-off
                        break  
                    
            return max_eval, best_column

        # Player is Minimizing Player
        else:  
            min_eval = np.inf
            
            for col in range(board.width):
                if board.is_valid(col):
                    new_board = board.get_new_board(col, player)
                    
                    evaluation, _ = self.minmax_abp(new_board, depth - 1, alpha, beta, opponent)
                    
                    # updating the min score
                    if evaluation < min_eval:
                        min_eval = evaluation
                        best_column = col
                    
                    # updating beta
                    beta = min(beta, evaluation)
                    # Pruning
                    if beta <= alpha: # Alpha cut-off
                        break  
                    
            return min_eval, best_column

    def make_move(self, board: Board) -> int:
        """Gets the column for the player to play in

        Args:
            board (Board): the current board

        Returns:
            int: column to play in
        """

        # TODO: implement minmax algorithm with alpha beta pruning!
        alpha = -np.inf
        beta = np.inf
        
        _, best_column = self.minmax_abp(board, self.depth, alpha, beta, self.player_id)

        return best_column


class HumanPlayer(PlayerController):
    """Class for the human player
    Inherits from Playercontroller
    """
    def __init__(self, player_id: int, game_n: int, heuristic: Heuristic) -> None:
        """
        Args:
            player_id (int): id of a player, can take values 1 or 2 (0 = empty)
            game_n (int): n in a row required to win
            heuristic (Heuristic): heuristic used by the player
        """
        super().__init__(player_id, game_n, heuristic)

    
    def make_move(self, board: Board) -> int:
        """Gets the column for the player to play in

        Args:
            board (Board): the current board

        Returns:
            int: column to play in
        """
        print(board)

        if self.heuristic is not None:
            print(f'Heuristic {self.heuristic} calculated the best move is:', end=' ')
            print(self.heuristic.get_best_action(self.player_id, board) + 1, end='\n\n')

        col: int = self.ask_input(board)

        print(f'Selected column: {col}')
        return col - 1
    

    def ask_input(self, board: Board) -> int:
        """Gets the input from the user

        Args:
            board (Board): the current board

        Returns:
            int: column to play in
        """
        try:
            col: int = int(input(f'Player {self}\nWhich column would you like to play in?\n'))
            assert 0 < col <= board.width
            assert board.is_valid(col - 1)
            return col
        except ValueError: # If the input can't be converted to an integer
            print('Please enter a number that corresponds to a column.', end='\n\n')
            return self.ask_input(board)
        except AssertionError: # If the input matches a full or non-existing column
            print('Please enter a valid column.\nThis column is either full or doesn\'t exist!', end='\n\n')
            return self.ask_input(board)
        