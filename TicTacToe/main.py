# Displaying game board
def displayBoard(board):
    print("\n" * 100)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


# Taking player input
def playerInput():
    playerChoice = ''
    # Asking player to choose X or 0
    while playerChoice != 'X' and playerChoice != '0':
        playerChoice = input('Player 1, Choose X or 0: ').upper()
    if playerChoice == 'X':
        return ('X', '0')
    return ('0', 'X')


# Placing player choices on board
def playerChoiceOnBoard(board, playerChoice, poistion):
    board[poistion] = playerChoice


# Checking winning statuses
def checkWinStatus(board, playerChoice):
    return ((board[7] == playerChoice and board[8] == playerChoice and board[9] == playerChoice) or
            (board[4] == playerChoice and board[5] == playerChoice and board[6] == playerChoice) or
            (board[1] == playerChoice and board[2] == playerChoice and board[3] == playerChoice) or
            (board[7] == playerChoice and board[4] == playerChoice and board[1] == playerChoice) or
            (board[8] == playerChoice and board[5] == playerChoice and board[2] == playerChoice) or
            (board[9] == playerChoice and board[6] == playerChoice and board[3] == playerChoice) or
            (board[7] == playerChoice and board[5] == playerChoice and board[3] == playerChoice) or
            (board[9] == playerChoice and board[5] == playerChoice and board[1] == playerChoice))


# Choosing first
import random

def chooseFirst():
    flipChoice = random.randint(0, 1)
    if flipChoice == 0:
        return 'Player 1'
    return 'Player 2'


# Checking space in board
def checkSpace(board, position):
    return board[position] == ' '


# Checking full board
def fullBoardCheck(board):
    for i in range(1, 10):
        if(checkSpace(board, i)):
            return False
    return True


# Player choice position
def playerChoicePosition(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not checkSpace(board, position):
        position = int(input('Choose a postion: (1 - 9)' ))
    return position


# Replay game
def replayGame():
    choice = input("Play Again? Enter Yes or No").upper()
    return choice == "YES"


# Game loop starts - Game starts
print('Welcome to TicTacToe')

while True:
    board = [' '] * 10;
    playerOne, playerTwo = playerInput()
    turn = chooseFirst()
    print(turn + ' Will be playing First!')
    play = input('Ready to Play? Y or N').upper()
    if play == 'Y':
        game = True
    else:
        game = False
    while game:
        if turn == 'Player 1':
            displayBoard(board)
            position = playerChoicePosition(board)
            playerChoiceOnBoard(board, playerOne, position)
            if checkWinStatus(board, playerOne):
                displayBoard(board)
                print('Yo!! Player 1 has won the game')
                game = False
            else:
                if fullBoardCheck(board):
                    displayBoard(board)
                    print('Game is Tied')
                    game = False
                else:
                    turn = 'Player 2'
        else:
            displayBoard(board)
            position = playerChoicePosition(board)
            playerChoiceOnBoard(board, playerTwo, position)
            if checkWinStatus(board, playerTwo):
                displayBoard(board)
                print('Yo!! Player 2 has won the game')
                game = False
            else:
                if fullBoardCheck(board):
                    displayBoard(board)
                    print('Game is Tied')
                    game = False
                else:
                    turn = 'Player 1'
    if not replayGame():
        break