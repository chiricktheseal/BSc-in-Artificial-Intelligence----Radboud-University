from Field import Field


class Sudoku: # загрузка сцдоку из файла, формат вывод, создание соседних ячеек для каждой ячейки, доступ к текущ состоянию доски

    def __init__(self, filename):
        self.board = self.read_sudoku(filename)

    def __str__(self): 
        output = "╔═══════╦═══════╦═══════╗\n" # output — накапливает результат
        # iterate through rows
        for i in range(9):  # i — индекс строки, от 0 до 8
            if i == 3 or i == 6:
                output += "╠═══════╬═══════╬═══════╣\n"  # разделительная линия между блоками строк.
            output += "║ " # левая граница
            # iterate through columns
            for j in range(9): # столбцы от 0 до 8
                if j == 3 or j == 6:
                    output += "║ " #разделяет каждый 3ий квадрат
                output += str(self.board[i][j]) + " " # self.board[i][j] — значение текущей ячейки в сетке судоку
            output += "║\n" # справа граница
        output += "╚═══════╩═══════╩═══════╝\n"
        return output

    @staticmethod
    def read_sudoku(filename):
        """
        Read in a sudoku file
        @param filename: Sudoku filename
        @return: A 9x9 grid of Fields where each field is initialized with all its neighbor fields
        """
        assert filename is not None and filename != "", "Invalid filename"
        # Setup 9x9 grid
        grid = [[Field for _ in range(9)] for _ in range(9)] # пустая сетка 9*9, Каждый элемент сетки инициализируется объектом Field

        try:
            with open(filename, "r") as file: # постросчная обработка файла
                for row, line in enumerate(file):  # енумерате -номер строки и текст
                    for col_index, char in enumerate(line): # внутри строки лайн, для индекса кол_индекс и значение чар каждого символа
                        if char == '\n':
                            continue
                        if int(char) == 0:
                            grid[row][col_index] = Field() # пустая ячейка доски - создается Field() (без значения)
                        else:
                            grid[row][col_index] = Field(int(char)) # Создается Field с этим значением

        except FileNotFoundError:
            print("Error opening file: " + filename)

        Sudoku.add_neighbours(grid) # добавит соседей для каждой ячейки
        return grid # Возвращает заполненную сетку

    @staticmethod
    def add_neighbours(grid):
        """
        Adds a list of neighbors to each field
        @param grid: 9x9 list of Fields
        """
        for row in range(9):
            for col in range(9):
                neighbour_set = set()
                 
                for cols_of_row in range(9):
                    if cols_of_row != col:
                        neighbour_set.add(grid[row][cols_of_row])
                
                for rows_of_row in range(9):
                    if rows_of_row != row:
                        neighbour_set.add(grid[rows_of_row][col])
                
                start_row, start_col = (row // 3) * 3, (col // 3) * 3
                for i in range(3):
                    for j in range(3):
                        square_row =  start_row + i
                        square_col = start_col + j 
                        if square_row != row or square_col != col:
                            neighbour_set.add(grid[square_row][square_col])
                        
                       
                grid[row][col].set_neighbours(list(neighbour_set))  # Устанавливаем список соседей для текущей ячейки

    def board_to_string(self):

        output = ""
        for row in range(len(self.board)): # Проходит по каждой строке row доски
            for col in range(len(self.board[row])): #  и столбцу col каждого столбца доски
                output += self.board[row][col].get_value() # Для каждой ячейки добавляет значение self.bo... в строку output.
            output += "\n" # После каждой строки
        return output

    def get_board(self):
        return self.board
