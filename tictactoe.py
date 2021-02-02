"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    # count the number of filled in entries
    # if even, X
    # if odd, O
    count = count_non_empty_elements(board)

    if count % 2 == 0:
        return X
    elif count > 9:
        return EMPTY
    else:
        return O


def count_non_empty_elements(board):
    count = 0
    for line in board:
        if line is not None:
            for element in line:
                if element != EMPTY:
                    count = count + 1
    return count


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = []

    row = -1
    for line in board:
        row = row + 1
        column = -1
        if line is not None:
            for element in line:
                column = column + 1
                if element == EMPTY:
                    possible_moves.add((row, column))

    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board2 = board.deepcopy()
    if board[action[0]][action[1]] == EMPTY:
        board2[action[0]][action[1]] = player(board)
    else:
        raise Exception
    return board2


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    top_left_corner = board[0][0]
    top_center = board[0][1]
    if top_left_corner == EMPTY:
        check_top_center(top_center)
    else:
        if (top_left_corner == board[1][0] and top_left_corner == board[2][0]) or \
                (top_left_corner == board[1][1] and top_left_corner == board[2][2]) or \
                (top_left_corner == board[0][1] and top_left_corner == board[0][2]):
            return top_left_corner
        else:
            check_top_center(top_center)


def check_top_center(board, top_center):
    top_right = board[0][2]
    if top_center == EMPTY:
        check_top_right(board, top_right)
    else:
        if top_center == board[1][1] and top_center == board[2][1]:
            return top_center
        check_top_right(board, top_right)


def check_top_right(board, top_right):
    center_left = board[1][0]
    if top_right == EMPTY:
        check_center_left(board, center_left)
    else:
        if (top_right == board[2][1] and top_right == board[2][2]) or \
                (top_right == board[1][1] and top_right == board[0][2]):
            return top_right
        else:
            check_center_left(board, center_left)


def check_center_left(board, center_left):
    bottom_left = board[2][0]
    if center_left == EMPTY:
        check_bottom_left(board, bottom_left)
        return None
    else:
        if center_left == board[1][1] and center_left == board[1][2]:
            return center_left


def check_bottom_left(board, bottom_left):
    if bottom_left == EMPTY:
        return None
    else:
        if bottom_left == board[2][1] and bottom_left == board[2][2]:
            return bottom_left


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    else:
        count = count_non_empty_elements(board)
        if count >= 8:
            return True
        else:
            return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winning_player = winner(board)
    if winning_player == X:
        return 1
    elif winning_player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
