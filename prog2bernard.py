#Zane Bernard
#CSC 131 - 005
#Dr. Ebrahimi

'''Purpose: to display an updated board whenever it is called for
Input: the list 'board' will be input each time the function is called for
Return: a side effect is given (printing out the board) but no value is returned'''
def displayBoard(board):
    
    #group the board into sections of 3
    X = 3
    f_board = [board[x:x+X] for x in range(0, len(board), X)]

    #go through each group, print, and then go to next line
    for k in f_board:
       for l in k:
         print(l, end = "  ")
       print()
       print()

'''Purpose: to take handle invalid input from the user and return a string that
            represents the move the user means to make.
Input:the board, the corresponding locations, and the correct player are passed through
        this function. A move is input by the user.
Return: a string is returned that represents the placement of the move.'''
def getMove(board, locations, player):
    #flag to handle invalid input
    invalid = True

    #while invalid input is not confirmed
    while invalid == True:

        #takes input
        move = str(input(player + ', enter your move: '))

        #check if move is in locations
        if move in locations:
            check_index = (int(move) - 1)

            #if so, has it been taken?
            if board[check_index] == 'X' or board[check_index] == 'O':
                print('That place has already been taken.')
                
            #if all is good, flip the flag
            else:
                invalid = False

    #returns a string that represents the move the user wants to make
    return move

'''Purpose: iterates through the combinations of wins and checks if the board matches.
Input: the current board and current symbol are passed though the function.
Return: returns a boolean value True or False that determines a win or not, respectively.'''
def win(board, symbol):

    #define all vertical, horizontal, and diagonal possibilities
    vertical = [[board[0], board[3], board[6]], [board[1], board[4], board[7]], \
                [board[2], board[5], board[8]]]
    horizontal = [[board[0], board[1], board[2]], [board[3], board[4], board[5]], \
                  [board[6], board[7], board[8]]]
    diagonal = [[board[0], board[4], board[8]], [board[2], board[4], board[6]]]

    #combine those possibilities into a list that can be interated through
    combinations = [vertical, horizontal, diagonal]

    #an empty list that will store a winning combination
    win_combo = []

    #acts as a placeholder for either 'X' or 'O'
    x = symbol
    
    #check if combinations are filled
    for k in combinations:

            #interate through each group within each subsection
            for l in k:
                
                #check if there is a winning combo
                if l == [x, x, x]:
                
                    #append l to the winning combination
                    #this acts as a way to store the win while the loop still iterates
                    win_combo.append(l)

    #sees if a value was stored from the for loop                
    if win_combo == [[x, x, x]]:

        #if so, game is won
        player_win = True
    else:

        #if not, continue game
        player_win = False

    #boolean value (True or False)
    return player_win

'''Purpose: to check if the board is filled once a win has not been determined.
Input: the current board is passed.
Return: returns a boolean value True or False that determines a tie game.'''
def tieGame(board):

    #check if board is filled
    if '-' not in board:

        #tie is true
        tie_game = True

    else:
        tie_game = False


    #boolean value (True or False)
    return tie_game
    
def main():
    #initilize the display board and the corresponding locations
    board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    locations = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    #welcome screen
    print('This program will allow two players to play the game of tic-tac-toe')
    print("Player 1 has 'X', and player 2 has 'O'")

    #get user input to keep track of each player
    player1 = str(input('Enter the name of player 1: '))
    player2 = str(input('Enter the name of player 2: '))

    #stores a list that will go back and forth between players
    players = [player1, player2]

    print('Enter your mark using the board positions shown below')

    #call displayBoard and pass locations
    displayBoard(locations)

    #counts turns
    counter = 0
    #create flag for terminating the game
    game_over = False

    #while loop that keeps the game goig
    while not game_over:

        #if an even number, its player 1
        if counter % 2 == 0:
            player = players[0]
            counter = counter + 1
            symbol = 'X'

        #odd number = player 2
        else:
            player = players[1]
            counter = counter + 1
            symbol = 'O'

        #blank line for formatting
        print()
        
        #assigns the players selection to a variable
        move = getMove(board, locations, player)
        print()
        
        #finds the index of that move
        board_index = locations.index(move)
        
        #replaces the index with the appropriate symbol
        board[board_index] = symbol

        #display updated board
        displayBoard(board)

        #blank line for formatting
        print()
        
        #if the win() returns true, game is over and the current player wins
        if win(board, symbol) == True:
            print(player + ', you win!')
            game_over = True

        #if win() returns false, but tieGame() returns true, then its a tie
        elif tieGame(board) == True:
            print('Tie game!')
            game_over = True
    
main()

