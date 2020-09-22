'''
TODO:
main function
board initialization
functions for changing tile status
'''
import random

board = []
dimension = 5

def main():
  global board
  initialize_board()

  print_board(board)

  board = update_board(board)

  print_board(board)

def initialize_board():
  global board
  for row in range(dimension):
    grid_rows = []
    for  column in range(dimension):
      if random.randint(0,2) == 0:
        grid_rows += [1]
      else:
        grid_rows += [0]
    board += [grid_rows]
  return board


def print_board(board):
    print("")
    for i in range(5):
      print(board[i])
    print("")

def update_board(board):
  for row in range(dimension):
    for column in range(dimension):
        ##count alive neighbour cells
        alive_cells = 0
        try:
            for i in range(3):
                if board[row-1][i-1] == 0:
                    alive_cells += 1
        except IndexError:
            pass
        continue
        try:
            if board[row][column-1] == 0:
                alive_cells += 1
        except IndexError:
            pass
        continue
        try:
            if board[row][column+1] == 0:
                alive_cells += 1
        except IndexError:
            pass
        continue
        try:
            for i in range(3):
                if board[row+1][i-1] == 0:
                    alive_cells += 1
        except IndexError:
            pass
        continue
        ## change status
        if alive_cells == 3:
            board[row][column]=1
        else:
            if alive_cells <= 1:
                board[row][column]=  0
            elif alive_cells >= 4:
                board[row][column]= 0
    return(board)



if __name__ == '__main__':
    main()
