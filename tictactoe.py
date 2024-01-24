import random
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#global varibles
currentPlayer = 'X'
winner = None
gameRunning = True

#printing the game board
def printBoard(board):
    print(" | " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print("----------------")
    print(" | " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print("----------------")
    print(" | " + board[6] + " | " + board[7] + " | " + board[8] + " | ")
#printBoard(board)

#take Player Input
def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print('Oops, This position already been taken')


#Check who win or tie
def check_horizontal(board): 
    #this function checks if the value horizontally is same then that player will win
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[7] != "-":
        winner = board[6]
        return True
    
def check_row(board):
    global winner
    if board[0] == board [3] == board[6] and board[3]!= "-":
        winner = board[3]
        return True
    if board[1] == board [4] == board[7] and board[4] != "-":
        winner = board[4]
        return True
    if board[2] == board [5] == board[8] and board[5] != "-":
        winner = board[5]
        return True
    
def check_diagonal(board): # check diagonally X
    global winner
    if board[0] == board [4] == board[8] and board[0]!= "-":
        winner = board[0]
        return True
    if board[2] == board [4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    
def check_tie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False

def check_win():
    global gameRunning  # Ensure you have access to modify the global variable
    if check_diagonal(board) or check_horizontal(board) or check_row(board):
        print(f"The winner is {winner}")
        gameRunning = False  # Stop the game loop when a winner is found


#switch the player
        
def switch_player():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

#computer
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)  # Randomly choose a position
        if board[position] == "-":  # Check if the position is empty
            board[position] = "O"  # Place the computer's move
            switch_player()  # Switch back to the human player
            break  # Exit the loop after making a move


# check for win or tie again
        
while gameRunning:
    printBoard(board)
    playerInput(board)
    check_win()
    check_tie(board)
    switch_player() 
    computer(board)
    check_win()
    check_tie(board)