import random

def display_board_hits(board, hit):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if hit[row][col]:
                print("X", end=" ")
            elif board[row][col] == -1:
                print("O", end=" ")
            else:
                print("_", end=" ")
        print()
        
    
def initialize_board(ships):

    board = [ [0 for i in range(8)] for i in range(8)]
    hits = [ [False for i in range(8)] for i in range(8)]
    
    while ships > 0:
        length = random.randint(2,4)
        start_row = random.randint(0,7)
        start_col = random.randint(0,7)
        vert = random.choice([True, False])
        if vert:
            try:
                for row_increment in range(length):
                    if board[start_row + row_increment][start_col] != 0:
                        raise IndexError
                for row_increment in range(length):
                    board[start_row + row_increment][start_col] = length
            except IndexError:
                continue
        else:
            try:
                for col_increment in range(length):
                    if board[start_row][start_col + col_increment] != 0:
                        raise IndexError
                for col_increment in range(length):
                    board[start_row][start_col + col_increment] = length
            except IndexError:
                continue
        ships -= 1
        
    return board, hits
    
def check_hit_and_update(row, col, board, hit):
    if board[row][col] != 0 and not hit[row][col]:
        hit[row][col] = True
        return True
    else:
        board[row][col] = -1
        return False

def get_move(board, hit):
    while True:
        try:
            row = int(input("Row ==>"))
            print()
            col = int(input("Column ==>"))
            if hit[row][col]:
                raise TypeError
            if board[row][col] == -1:
                raise TypeError
            return row, col
        except ValueError:
            print("It's gotta be an int")
        except IndexError:
            print("Out of range")
        except TypeError:
            print("We've seen that before")

def get_opp_move(board, hit):
    while True:
        try:
            row = random.randint(0,len(board) -1)
            col = random.randint(0, len(board[0]) -1)
            if board[row][col] == -1 or hit[row][col]:
                raise TypeError
            return row, col
        except TypeError:
            continue


def check_win(board, hit):

    hits = 0
    hits_needed = 0

    for row in board:
        for col in row:
            if col != 0:
                hits_needed += 1
                
    for row in hit:
        for col in row:
            if col:
                hits += 1

    if hits == hits_needed:
        return True
    else:
        return False
    
    
def play():

    ship_num = 4
    winner = False
    user_board, user_hits = initialize_board(ship_num)
    opp_board, opp_hits = initialize_board(ship_num)
    user_hits_opp = False
    opp_hits_user = True

    while not winner:

        
        print("Your Turn")
        display_board_hits(opp_board, opp_hits)
        user_row, user_col = get_move(opp_board, opp_hits)
        user_hits_opp = check_hit_and_update(user_row, user_col, opp_board, opp_hits)
        if user_hits_opp:
            print("You got a hit!")
        else:
            print("You missed!")
        winner = check_win(opp_board, opp_hits)
        if winner:
            break

        print()
        print("Computer Turn")
        opp_row, opp_col = get_opp_move(user_board, user_hits)
        opp_hits_user = check_hit_and_update(opp_row, opp_col, user_board, user_hits)
        if opp_hits_user:
            print("You got hit!")
        else:
            print("You're safe this round!")
        display_board_hits(user_board, user_hits)
        winner = check_win(user_board, user_hits)
        print()
        
    

play()
