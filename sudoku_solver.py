import math
import random

class Board():
    def __init__(self, dim):
        self.dim = dim

        self.correct_board = self.makeBoard()
        self.display_board = self.remove_elem(self.correct_board)

    def makeBoard(self):
        main_arr = []
        for i in range(0, self.dim):
            main_arr.append([])

            for j in range(0, self.dim):
                main_arr[i].append(' ')

        self.fillBoard(main_arr)
        return main_arr
    
    def colChecker(self, arr, num, index):
        col_vals = [arr[i][index] for i in range(0, len(arr))]
        if num in col_vals:
            return False
        return True
    
    def fillBoard(self, arr):
        for i in range(0, len(arr)):
            index = 0
            while index < self.dim:
                num = random.randint(1, self.dim)
                if num not in arr[i] and self.colChecker(arr, num, index):
                    arr[i][index] = num
                    index += 1

        return arr
    
    def remove_elem(self, arr):
        for i in range(0, len(arr)):
            num_elem = random.randint(0, self.dim - 1)
            while num_elem > 0:
                index = random.randint(0, len(arr[i]) - 1)
                if arr[i][index] != ' ':
                    arr[i][index] = ' '
                    num_elem -= 1

        return arr
    
def sudoku_solver():
    board = Board(5)
    arr = board.display_board
    print('Initial board:')
    print(arr)
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if arr[i][j] == ' ':
                solved = False
                num = 1
                while solved == False:
                    if num not in arr[i] and board.colChecker(arr, num, j):
                        arr[i][j] = num
                        solved = True
                    else:
                        num += 1

    print('Final board:')
    print(arr)
    
                    

sudoku_solver()