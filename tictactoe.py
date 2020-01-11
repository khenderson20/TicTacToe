"""TIC TAC TOE GAME
    using only functions.
"""
import random


def display_board(board):
    """ Displays the board game by taking in a list Object
        and using print statements to display the board game.

        TEST: a list of all the 'X's and 'O's to make sure the board
        gets displayed correctly to the user.

    :param board: list Object of the game board, index 0 is never used.
    :return: nothing, just displays the board
    """
    print(board[7] + "  | " + board[8] + " | " + board[9])
    print("---|---|---")
    print(board[4] + "  | " + board[5] + " | " + board[6])
    print("---|---|---")
    print(board[1] + "  | " + board[2] + " | " + board[3])


# TEST: display_board
# test_board = ['#', 'X', 'O', 'X', 'O', ' ', 'O', 'X', 'O', 'X']
# display_board(test_board)


def player_input():
    """ takes in a player input and assigns their marker as either 'X' or 'O'.
        uses a while loop to continually ask the user until a correct answer is given.

        TEST: makes sure the desired return values are given.
    :return: a tuple to use the player1_marker and player2_marker in another function.
    """
    marker = ''
    # KEEP ASKING PLAYER 1 to choose X or O

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')

    # ASSIGN PLAYER 2, the opposite marker
    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = "X"

    return (player1, player2)


# TEST: player_input
# player1_marker, player2_marker = player_input()
# print(player1_marker, player2_marker)


def place_marker(board, marker, position):
    """ Assigns the marker to the board, at specified position.

    :param board: list of all available spaces on board.
    :param marker:  the marker the player chooses to use.
    :param position:  the position which the player wishes their marker to be placed at.
    :return: none, only marks the board.
    """
    board[position] = marker


# TEST: player_marker, then display board to make sure, marker was placed.
# place_marker(test_board, '$', 3)
# display_board(test_board)


def win_check(board, mark):
    """ checks to see if the players (1 or 2) markers have won by getting 3 in a row
        possible ways to win:
        1. across the top
        2. across the middle
        3. across the bottom
        4. down the left column
        5. down thr middle column
        6. down the right column
        7. diagonal right.
        8. diagonal left.

    :param board: list to check whether matching markers for player.
    :param mark: the players chosen marker, 'X' or 'O'
    :return: returns 1 of boolean conditions for a win.
    """
    # returns 1 of 8 boolean conditions for a win.
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down left column
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down middle column
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down right column
            (board[1] == mark and board[5] == mark and board[9] == mark) or  # diagonal right
            (board[3] == mark and board[5] == mark and board[7] == mark))  # diagonal left


def choose_first():
    """ function creates a random number between 1 or 2 a
        returns a string saying which player is going to play first.

    :return: returns a string indicating which player is going first
    """
    player = random.randint(1, 2)
    return "player {} is going.".format(player)


def space_check(board, position):
    """ returns a boolean value if position is blank on the board.
        True if position is free, false otherwise.

    :param board: list with possible open positions, or not.
    :param position: position player wants
    :return: boolean True if space is open ' ', False otherwise.
    """
    return board[position] == ' '


def full_board(board):
    """ method to check if board still has available spaces, if board is full, call a tie.

    :param board: list of all spaces to check if board is full
    :return: boolean True if board is full, False otherwise.
    """
    length = len(board)
    # iterate through the list looking for ' ' spaces.
    for i in range(1, length):
        # if no ' ' keep searching
        if not space_check(board, i):
            continue
        elif space_check(board, i):
            return False
    return True


def player_choice(board):
    """

    :param board: list of all spaces to check if space player chose was available
    :return: integer if the available space is free, returns a string if space is not available
    """
    number = 0
    choice_bool = True
    # get user input and ask until it's within correct range.
    while choice_bool:
        number = int(input("Next position? (1 - 9): "))
        if number in range(1, 10):
            choice_bool = False
            break
        else:
            continue
    # if space is ' ' available
    if space_check(board, number):
        return number
    elif not space_check(board, number):
        return 'Space at {} not available'.format(number)


def replay():
    """ method to ask player if they would like to play again or not.

    :return: True if yes, False, if no.
    """
    replay_choice = ''
    while replay_choice.lower() != 'y' and replay_choice.lower() != 'n':
        replay_choice = input("Do you want to Play Again? (Y/N): ")
    if replay_choice.lower() == 'y':
        return True
    elif replay_choice.lower() == 'n':
        return False


print("Welcome to Tic Tac Toe!")
# make the blank game board!
game_board = [' ' for x in range(10)]
game_on = False
to_play = ''
turn = choose_first()
while True:
    display_board(game_board)
    # ask player one which character (X or O) they would like to be.
    # p1, and p2 hold markers for the players
    player1, player2 = player_input()
    # choose which character is going to move first.
    print(turn)

    to_play = input("Are You Ready To Play?: ")
    if to_play.lower() == 'y' or to_play.lower() == 'yes':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == "player 1 is going.":
            # player 1's turn.

            display_board(game_board)
            position = player_choice(game_board)
            # check to see if string is returned from player_choice.
            if isinstance(position, str):
                print(position + " player 1")
                continue
            place_marker(game_board, player1, position)

            # check to see if player won.
            if win_check(game_board, player1):
                display_board(game_board)
                print("Congratulations Player 1! You won the Game!")
                game_board = [' ' for x in range(10)]
                game_on = False
            else:
                if full_board(game_board):
                    print("The game is a tie!")
                    game_board = [' ' for x in range(10)]
                    break
                else:
                    turn = "player 2 is going."
        else:
            # Player 2's turn.

            display_board(game_board)
            position = player_choice(game_board)
            # check to see if string is returned from player_choice.
            if isinstance(position, str):
                print(position + " player 2")
                continue
            place_marker(game_board, player2, position)
            # check to see if player won.
            if win_check(game_board, player2):
                display_board(game_board)
                print("Player 2 has won!")
                game_on = False
            else:
                if full_board(game_board):
                    display_board(game_board)
                    print("The game is a tie!")
                    break
                else:
                    turn = 'player 1 is going.'

    if not replay():
        break
