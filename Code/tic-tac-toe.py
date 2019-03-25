import random


board = [ [" " for cnt in range(0,3)] for cnt in range(0,3) ]

def print_board(board):
    for i in range(0,3):
        print(board[i])

def get_coord_usr():
    row = int(input("enter row"))
    col = int(input("enter col"))
    return (row,col)

def get_coord_comp(board):
    row = 0
    col = 0
    while board[row][col] != " ":
        row = random.randint(1,2)
        col = random.randint(1,2)
    return (row, col)

def check_full(board):
    for row in board:
        if " " in row:
            return False
    return True

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
    u_row, u_col = get_coord_usr()
    board[u_row][u_col] = "x"
    print_board(board)
    print()
    if CheckVictory(board,u_row, u_col):
        stop = True
        winner = "user"
        break
    if check_full(board):
        full = True
        winner = "tie"
        break
    c_row, c_col = get_coord_comp(board)
    board[c_row][c_col] = "o"
    print_board(board)
    print()
    if CheckVictory(board,u_row, u_col):
        stop = True
        winner = "comp"
    if check_full(board):
        full = True
        winner = "tie"
        break
print("Winner:", winner)

