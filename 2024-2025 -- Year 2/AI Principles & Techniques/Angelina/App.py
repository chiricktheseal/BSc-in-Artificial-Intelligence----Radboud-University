import os
from Game import Game
from Sudoku import Sudoku

sudoku_folder = os.path.join(os.path.dirname(__file__), "Sudokus")  #путь к папке, где хранятся файлы с задачами судоку

class App:


    @staticmethod
    def solve_sudoku(sudoku_file):
        game = Game(Sudoku(sudoku_file)) #объект судоку из файла передается в гейм, создавая объект гейм
        game.show_sudoku()
        if (game.solve() and game.valid_solution()): #солве - пытается решить . валид -проверка правильности
            print("Solved!") # если оба тру
        else:
            print("Could not solve this sudoku :(")

    @staticmethod
    def start(): # запуск основного интерфейса - можно выбрать файл судоку и управляет циклом выполнения программы.
        while True:
            file_num = input("Enter Sudoku file (1-5): ")
            print("\n")

            file = None
            for filename in os.listdir(sudoku_folder):  # ищет файл в папке Sudokus, в названии которого содержится введенный номер
                if file_num in filename:
                    file = filename
            if file is not None:
                App.solve_sudoku(os.path.join(sudoku_folder, file)) #метод solve_sudoku с полным путем к файлу
            else:
                print("Invalid choice")

            continue_input = input("Continue? (yes/no): ") # В конце программы
            if continue_input.lower() != 'yes':
                break


if __name__ == "__main__":
    App.start()

