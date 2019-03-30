#imports
import random

#initialize board


def print_board(board):
    return

#hint return tuple
def get_coord_usr():
    return

#hint return tuple
def get_coord_comp(board):
    return

def check_full(board):
    return

def CheckVictory(board, x, y):

    #check if previous move caused a win on vertical line 
    if board[0][y] == board[1][y] == board [2][y]:
        return True

    #check if previous move caused a win on horizontal line 
    if board[x][0] == board[x][1] == board [x][2]:
        return True

    #check if previous move was on the main diagonal and caused a win
    if x == y and board[0][0] == board[1][1] == board [2][2]:
        return True

    #check if previous move was on the secondary diagonal and caused a win
    if x + y == 2 and board[0][2] == board[1][1] == board [2][0]:
        return True

    return False   

stop = False
winner = ""
full = False

print_board(board)
print()

while not(stop or full):

    #user play
    u_row, u_col = get_coord_usr()
    board[u_row][u_col] = "x"
    
    print_board(board)
    print()

    #check conditions
    if CheckVictory(board,u_row, u_col):
        stop = True
        winner = "user"
        break
    
    if check_full(board):
        full = True
        winner = "tie"
        break

    #comp play
    c_row, c_col = get_coord_comp(board)
    board[c_row][c_col] = "o"
    
    print_board(board)
    print()

    #check conditions
    if CheckVictory(board,u_row, u_col):
        stop = True
        winner = "comp"
        
    if check_full(board):
        full = True
        winner = "tie"
        break
    
#output results
print("Winner:", winner)

