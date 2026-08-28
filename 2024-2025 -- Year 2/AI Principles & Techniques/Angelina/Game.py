class Game:

    def __init__(self, sudoku):
        self.sudoku = sudoku

    def show_sudoku(self):
        print(self.sudoku)
    
    def solve(self) -> bool:
        """
        Implementation of the AC-3 algorithm
        @return: true if the constraints can be satisfied, false otherwise
        """
        queue = []  # One shared queue for all arcs
        board = self.sudoku.get_board()
        
        for row in range(9):
            for col in range(9): 
                current_field = board[row][col] 
                 
                for neighbour in current_field.get_neighbours():
                    pair = (current_field, neighbour)
                    queue.append(pair)
                    
                    
        def revise(current_field, neighbour):
            D_current = current_field.get_domain()
            D_neighbour = neighbour.get_domain()
            revised = False
    
            if not D_neighbour: # Если домен соседа пуст, проверяем только значения, которые у него есть
                neighbour_value = neighbour.get_value()  # Получаем значение соседа
                if neighbour_value in D_current:  # Если значение соседа есть в домене текущей ячейки
                    current_field.remove_from_domain(neighbour_value)  # Удаляем его
                    
                    revised = True
            else:    
                #print(f"{current_field} and {neighbour}")
                for D_current_i in D_current[:]:  # Создаем копию списка, чтобы изменять оригинальный домен
                    compatible = False
                    for D_neighbour_i in D_neighbour:
                        if D_current_i == D_neighbour_i:  # Если значение совпадает, оно не совместимо
                            compatible = True
                            break
                    if compatible == False:
                        current_field.remove_from_domain(D_current_i)  # Удаляем его
                        revised = True

            return revised
        
        while queue:
            pair = queue.pop(0)  # Get the first pair from the queue
            current_field, neighbour = pair
            
            #print(f"Сравниваем: текущее значение {current_field} и соседнее значение {neighbour}")
            if revise(current_field, neighbour):
                new_domain_size = current_field.get_domain_size()
                if new_domain_size == 0 : # Check if the domain of current_field is empty (no solution)
                    return False
                
                for neighbour_i in current_field.get_neighbours():
                    if neighbour_i != neighbour:
                        queue.append((neighbour_i, current_field))
                            
        return True
    
    def valid_solution(self) -> bool: 
        """
        Checks the validity of a sudoku solution
        @return: true if the sudoku solution is correct
        """
        # TODO: implement valid_solution function
        for row in range(9):
            checked = []
            for col in range(9):
                cell = self.sudoku.board[row][col]
                cell_value = cell.get_value()
                if cell_value == 0 or cell_value in checked:
                    return False
                checked.append(cell_value)
                
        for col in range(9):
            checked = []
            for row in range(9):
                cell = self.sudoku.board[row][col]
                cell_value = cell.get_value()
                if cell_value == 0 or cell_value in checked:
                    return False
                checked.append(cell_value)
        
        for row in range(9):
            for col in range(9):       
                checked = []
                start_row, start_col = (row // 3) * 3, (col // 3) * 3
                for i in range(3):
                    for j in range(3):
                        cell = self.sudoku.board[start_row + i][start_col + j]
                        cell_value = cell.get_value()
                        if cell_value == 0 or cell_value in checked:
                            return False
                        checked.append(cell_value)
                    
        return True

