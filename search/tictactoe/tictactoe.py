"""
Tic Tac Toe Player
"""

import math
import random

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
    x = sum([line.count("X") for line in board])
    o = sum([line.count("O") for line in board])

    if x == o:
        return "X"
    else:
        return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    sign = player(board)

    result = [line.copy() for line in board]

    # Checking if action isn't out of board
    for coordinate in action:
        if coordinate < 0 or coordinate > 2:
            raise Exception("Unauthorized Action")

    # Checking if action isn't already taken
    if not board[action[0]][action[1]]:
        result[action[0]][action[1]] = sign
    else:
        raise Exception("Unauthorized Action")

    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[1][1] and board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        return board[1][1]

    for n in range(3):
        if board[n][0] and board[n][0] == board[n][1] == board[n][2] or board[0][n] == board[1][n] == board[2][n]:
            return board[n][n]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or not actions(board):
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    player = winner(board)

    if player:
        return 1 if player == "X" else -1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current = player(board)
    possibilities = actions(board)

    choices = [possibility for possibility in possibilities]
    random.shuffle(choices)

    elements = [{"value": None, "action": action} for action in choices]

    # Computing optimal value for each action
    for element in elements:
        state = result(board, element["action"])
        while not terminal(state):
            state = result(state, minimax(state))
        element["value"] = utility(state)

    # Returning best move according to player
    if current == "X":
        best = max([element["value"] for element in elements])
        # Checking first for a winning move
        for element in elements:
            if element["value"] == best and terminal(result(board, element["action"])):
                return element["action"]
        # Finding best move otherwise
        for element in elements:
            if element["value"] == best:
                return element["action"]
    else:
        best = min([element["value"] for element in elements])
        # Checking first for a winning move
        for element in elements:
            if element["value"] == best and terminal(result(board, element["action"])):
                return element["action"]
        # Finding best move otherwise
        for element in elements:
            if element["value"] == best:
                return element["action"]
