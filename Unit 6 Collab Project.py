# Tic Tac Toe

# Imported so that later on the starting player can be chosen randomly
import random

# Makes the class Board
class Board:

    # Initializes the object
    def __init__(self):
        self.positions = [' '] * 10

    # Creates the visual game board
    def printBoard(self):
        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + self.positions[7] + ' | ' + self.positions[8] + ' | ' + self.positions[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.positions[4] + ' | ' + self.positions[5] + ' | ' + self.positions[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.positions[1] + ' | ' + self.positions[2] + ' | ' + self.positions[3])
        print('   |   |')

     # Checks if there is open spot
    def checkOpenPos(self, i):
        return self.positions[i] == ' '

    # Checks if any 3 in a row have the same symbol
    # In order, we check from
    # Top 3, Middle 3, Bottom 3
    # Left 3, Middle 3, Right 3
    # Left Diagonal, Right Diagonal
    def isWon(self, sym):
        # Checks if the given symbol won
        return ((self.positions[7] == sym and self.positions[8] == sym and self.positions[9] == sym) or
        (self.positions[4] == sym and self.positions[5] == sym and self.positions[6] == sym) or
        (self.positions[1] == sym and self.positions[2] == sym and self.positions[3] == sym) or
        (self.positions[7] == sym and self.positions[4] == sym and self.positions[1] == sym) or
        (self.positions[8] == sym and self.positions[5] == sym and self.positions[2] == sym) or
        (self.positions[9] == sym and self.positions[6] == sym and self.positions[3] == sym) or
        (self.positions[7] == sym and self.positions[5] == sym and self.positions[3] == sym) or
        (self.positions[9] == sym and self.positions[5] == sym and self.positions[1] == sym))

    # Checks if the board is filled
    def fullBoard(self):
        for i in range(1,10):
            if self.checkOpenPos(i):
                return False
        return True

    # Checks if there is a final tie or if the game should keep playing
    def tie(self, sym1, sym2):
        return self.fullBoard() and not self.isWon(sym1) and not self.isWon(sym2)

# Makes the class Player
class Player:

    # Initializes the object
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    # Passes position i and Board object b
    def makeMove(self, i, b):
        b.positions[i] = self.symbol

    # Lets the player type in their move
    def getPlayerMove(self, board): 
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not board.checkOpenPos(int(move)):
            print('What is your next move, ' + self.name + '? (1-9)')
            move = input()
        return int(move)

print('Welcome to Tic Tac Toe!')

# Creates the object Player 1 and designates them a symbol
player1 = Player("Player 1", 'X')
# Creates the object Player 2 and designates them a symbol
player2 = Player("Player 2", 'O')

# Creates the object board
board = Board()

# Utilizes the random module to randomly determine which player goes first
def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'player 2'
    else:
        return 'player 1'

# Allows the player to choose if they would like to play again
def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

# The game starts
while True:
    # Randomly selects the first player
    turn = whoGoesFirst()
    print(turn + ' will go first.')
    gameIsPlaying = True
    # Game loop as the players are playing the game
    while gameIsPlaying:
        if turn == 'player 1':
            # Player 1's turn
            board.printBoard()
            # Player inputs their move
            move = player1.getPlayerMove(board)
            # Executes Player 1's move
            player1.makeMove(move,board)
            # Checks if Player 1 has won.
            if board.isWon(player1.symbol):
                # Prints board.
                board.printBoard()
                print('Hooray! Player 1 has won the game!')
                gameIsPlaying = False
            else: # Game is a tie.
                if board.fullBoard():
                    board.printBoard()
                    print('The game is a tie!')
                    break
                else: # Game goes to Player 2's turn
                    turn = 'player 2'

        else:
            # Player 2's turn.
            board.printBoard()
            # Player inputs their move
            move = player2.getPlayerMove(board)
            # Executes Player 2's move
            player2.makeMove(move, board)
            # Checks if Player 2 has won
            if board.isWon(player2.symbol):
                # Prints board
                board.printBoard()
                print('Hooray! Player 2 has won the game!')
                gameIsPlaying = False
            else: # Game is a tie
                if board.fullBoard():
                    board.printBoard()
                    print('The game is a tie!')
                    break
                else: # Game goes to Player 1's turn
                    turn = 'player 1'
     # Clears the board if the game is over
    board = Board()
    # Checks if players want to play again
    if not playAgain():
        break
