"""
Fill in the required methods to get this tic tac toe program working
"""

def initializeBoard():
        """Returns blank 3 x 3 grid"""
        newBoard = []
        for row in range(3):
                row = []
                for col in range(3):
                        row.append("_")
                newBoard.append(row)
        return newBoard

def showBoard(board):
        """Display board"""
        for row in board:
                for col in row:
                        print (col, end = " ")
                print()

def updateBoard(board, row, col, character):
        """Upadates board with at given row and column with given character"""
        board[row][col] = character

def checkVictory(board, x, y):
        """Pass in board and coord for previous move"""

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


def getMove():
        """Gets, validates, and returns row and column choice"""
        while True:
                try:
                        y = int(input("Input row: "))
                        x = int(input("Input column: "))
                        if not(0 <= x <= 2) or not(0 <= y <= 2):
                                raise ValueError
                        return x,y
                except:
                        print("Bad input")

def isFull(board):
        """Checks if board is full"""
        for row in board:
                for col in row:
                        if col == "_":
                                return False
        return True

def play():

        b = initializeBoard()
        winner = False
        player1 = False
        characters = ["X","O"]

        #iterates until not winner or full
        while not winner and not isFull(b):
                
                #Changes player each turn
                player1 = not player1
                if player1:
                        char = characters[0]
                else:
                        char = characters[1]
                        
                print()
                showBoard(b)
                col_move, row_move = getMove()
                
                updateBoard(b, row_move, col_move, char)
                winner = checkVictory(b, row_move, col_move)
        
        showBoard(b)
        
        if winner:
                
                if player1:
                        print("The winner is player 1")
                else:
                        print("The winner is player 2")
                        
        else:
                print("DRAW!")

play()
