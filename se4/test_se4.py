import sys
import os

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

import se4

MODULE = "se4"

# # #
#
# HELPER FUNCTIONS
#
# # #

def check_none(actual, recreate_msg=None):
    msg = "The method returned None."
    msg += " Did you forget a return statement?"
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual is not None, msg

def check_expected_none(actual, recreate_msg=None):
    msg = "The method is expected to return None."
    msg += " Your method returns: {}".format(actual)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual is None, msg

def check_type(actual, expected, recreate_msg=None):
    actual_type = type(actual)
    expected_type = type(expected)

    msg = "The method returned a value of the wrong type.\n"
    msg += "  Expected return type: {}.\n".format(expected_type.__name__)
    msg += "  Actual return type: {}.".format(actual_type.__name__)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert isinstance(actual, expected_type), msg

def check_attribute(actual, attribute_name, recreate_msg=None):
    msg = "Your class should have a '{}' attribute.".format(attribute_name)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert hasattr(actual, attribute_name), msg

def check_attribute_type(actual, expected, recreate_msg=None):
    actual_type = type(actual)
    expected_type = type(expected)

    msg = "Your class has an attribute of the wrong type.\n"
    msg += "  Expected type: {}.\n".format(expected_type.__name__)
    msg += "  Actual type: {}.".format(actual_type.__name__)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert isinstance(actual, expected_type), msg

def check_equals(actual, expected, recreate_msg=None):
    msg = "Actual ({}) and expected ({}) values do not match.".format(actual, expected)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual == expected, msg

# # #
#
# TEST HELPERS
#
# # #

def do_test_board_constructor():

    recreate_msg = "To recreate this test in ipython3 run:\n"
    recreate_msg += "    b = {}.Board()".format(MODULE)

    actual = se4.Board()
    expected = boards["empty_board"]

    check_attribute(actual, "board", recreate_msg)

    recreate_msg += "\n    b.board"

    check_attribute_type(actual.board, expected, recreate_msg)
    check_equals(actual.board, expected, recreate_msg)


def do_test_board_str(test_board, expected):

    recreate_msg = "To recreate this test in ipython3 run:\n"
    recreate_msg += "    b = {}.Board()\n".format(MODULE)
    recreate_msg += "    print(b)\n"
    recreate_msg += "With the board b:\n" + board_msg(boards[test_board])

    b = se4.Board()
    b.board = boards[test_board]
    actual = str(b)

    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)


def do_test_board_valid_move(row, col, test_board, expected):

    recreate_msg = "To recreate this test in ipython3 run:\n"
    recreate_msg += "    b.valid_move(({}, {}))\n".format(row, col)
    recreate_msg += "With the board b:\n" + board_msg(boards[test_board])

    b = se4.Board()
    b.board = boards[test_board]
    actual = b.valid_move((row, col))

    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)

def do_test_board_play_move(row, col, player, test_board, expected, expected_board):

    recreate_msg = "To recreate this test in ipython3 run:\n"
    recreate_msg += "    p = {}.Player('{}', '{}')\n".format(MODULE, player.name, player.symbol)
    recreate_msg += "    b.play_move(({}, {}), p)\n".format(row, col)
    recreate_msg += "With the board b:\n" + board_msg(boards[test_board])

    b = se4.Board()
    b.board = boards[test_board]
    actual = b.play_move((row, col), player)

    check_equals(actual, expected, recreate_msg)
    check_type(b.board, boards[expected_board], recreate_msg)
    check_equals(b.board, boards[expected_board], recreate_msg)


def do_test_board_winner(player, expected, test_board):

    recreate_msg = "To recreate this test in ipython3 run:\n"
    recreate_msg += "    p = {}.Player('{}', '{}')\n".format(MODULE, player.name, player.symbol)
    recreate_msg += "    b.winner(p)\n"
    recreate_msg += "With the board b:\n" + board_msg(boards[test_board])

    b = se4.Board()
    b.board = boards[test_board]
    actual = b.winner(player)

    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)

# # #
#
# TESTS
#
# # #

def test_board_constructor():
    do_test_board_constructor()

def test_board_str1():
    do_test_board_str("empty_board", "E E E\nE E E\nE E E\n")

def test_board_str2():
    do_test_board_str("board_1", "E E O\nE X E\nE E E\n")

def test_board_str3():
    do_test_board_str("board_2", "E E O\nE X O\nE E E\n")

def test_board_str4():
    do_test_board_str("board_3", "E E O\nX X O\nE E E\n")

def test_board_str5():
    do_test_board_str("board_4", "E E O\nX X O\nE O E\n")

def test_board_str6():
    do_test_board_str("board_5", "E E O\nX X O\nE O X\n")

def test_board_valid_move_1():
    do_test_board_valid_move(0, 1, "board_1", True)

def test_board_valid_move_2():
    do_test_board_valid_move(2, 2, "board_1", True)

def test_board_valid_move_3():
    do_test_board_valid_move(-1, 0, "board_2", False)

def test_board_valid_move_4():
    do_test_board_valid_move(1, 3, "board_2", False)

def test_board_valid_move_5():
    do_test_board_valid_move(4, 0, "board_2", False)

def test_board_valid_move_6():
    do_test_board_valid_move(3, -2, "board_2", False)

def test_board_valid_move_7():
    do_test_board_valid_move(1, 1, "board_2", False)

def test_board_valid_move_8():
    do_test_board_valid_move(1, 2, "board_2", False)

def test_board_play_move_1():
    player = se4.Player("Orgus", "O")
    do_test_board_play_move(1, 2, player, "board_1", True, "board_2")

def test_board_play_move_2():
    player = se4.Player("Teneniel", "X")
    do_test_board_play_move(1, 0, player, "board_2", True, "board_3")

def test_board_play_move_3():
    player = se4.Player("Durge", "O")
    do_test_board_play_move(2, 1, player, "board_3", True, "board_4")

def test_board_play_move_4():
    player = se4.Player("Elan", "X")
    do_test_board_play_move(2, 2, player, "board_4", True, "board_5")

def test_board_play_move_5():
    player = se4.Player("Elan", "X")
    do_test_board_play_move(0, 2, player, "board_5", False, "board_5")

def test_board_play_move_6():
    player = se4.Player("Elan", "X")
    do_test_board_play_move(1, 0, player, "board_5", False, "board_5")

def test_board_play_move_7():
    player = se4.Player("Elan", "O")
    do_test_board_play_move(3, 1, player, "board_5", False, "board_5")

def test_board_winner_1():
    player = se4.Player("Satele", "X")
    do_test_board_winner(player, True, "X_horiz_win")

def test_board_winner_2():
    player = se4.Player("Luuke", "X")
    do_test_board_winner(player, True, "X_vert_win")

def test_board_winner_3():
    player = se4.Player("Raynar", "O")
    do_test_board_winner(player, True, "O_horiz_win")

def test_board_winner_4():
    player = se4.Player("Tikkes", "O")
    do_test_board_winner(player, True, "O_vert_win")

def test_board_winner_5():
    player = se4.Player("Shado", "X")
    do_test_board_winner(player, False, "tie_1")

def test_board_winner_6():
    player = se4.Player("Shado", "O")
    do_test_board_winner(player, False, "tie_1")

def test_board_winner_6():
    player = se4.Player("Morlish", "X")
    do_test_board_winner(player, False, "tie_2")

def test_board_winner_6():
    player = se4.Player("Morlish", "O")
    do_test_board_winner(player, False, "tie_2")

# # #
#
# TEST BOARDS
#
# # #

boards = {"empty_board": [["E", "E", "E"], ["E", "E", "E"], ["E", "E", "E"]], 
          "board_1":     [["E", "E", "O"], ["E", "X", "E"], ["E", "E", "E"]], 
          "board_2":     [["E", "E", "O"], ["E", "X", "O"], ["E", "E", "E"]], 
          "board_3":     [["E", "E", "O"], ["X", "X", "O"], ["E", "E", "E"]], 
          "board_4":     [["E", "E", "O"], ["X", "X", "O"], ["E", "O", "E"]], 
          "board_5":     [["E", "E", "O"], ["X", "X", "O"], ["E", "O", "X"]],
          "X_horiz_win": [["E", "O", "O"], ["X", "X", "X"], ["O", "E", "E"]],
          "X_vert_win":  [["X", "O", "X"], ["X", "O", "X"], ["O", "X", "X"]],
          "X_diag_win":  [["E", "O", "X"], ["O", "X", "E"], ["X", "E", "O"]],
          "O_horiz_win": [["E", "X", "E"], ["X", "O", "X"], ["O", "O", "O"]],
          "O_vert_win":  [["X", "O", "E"], ["X", "O", "X"], ["X", "O", "E"]],
          "O_diag_win":  [["O", "E", "E"], ["X", "O", "X"], ["E", "E", "O"]],
          "tie_1":       [["O", "E", "O"], ["X", "O", "X"], ["E", "E", "X"]],
          "tie_2":       [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]}

def board_msg(board):
    s = ""
    for row in board:
        s += "    " + str(row) + "\n"
    return s[:-1]



