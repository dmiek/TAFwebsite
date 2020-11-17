"""
Module governing if a move is valid or not.
"""

from idioten.application.idioten_input_modifier import input_modifier


def ok_to_move(board, k_b_f, k_b_t):
    """ Method assessing if a move is valid or not. """
    f_r = input_modifier(k_b_f)
    t_o = input_modifier(k_b_t)
    row = board[0]
    last_row = -1

    # assess if next position is different from current
    if f_r == t_o:
        print('next position needs to be different from current')
        return board

    # assess if to-position is occupied
    if board[0][t_o] != "- ":
        print('position not empty, cannot perform move')
        return board

    # assess if the card to be moved exists
    if board[0][f_r] == "- ":
        print('cannot move a non-existing card')
        return board

    # assess size of board
    if len(board) == 1:
        print('board is 1 row')
        board[0][t_o] = board[0][f_r]
        board[0][f_r] = '- '
        print(board)
        return board

    # if board is 2 rows or larger, continue to last row of board
    print('assessing if OK to remove')
    row = board[last_row]
    print(row)

    # determine from-position in board
    # if row is empty, ascend one row until non-empty row is found
    while row_fr[f_r] == '- ':
        pos_fr = pos_fr - 1
        row_fr = board[pos_fr]
        print('ascended one level')
    # when row is no longer empty
    print('row from no longer empty')

    # perform the move
    board[row_to][t_o] = board[pos_fr][f_r]
    board[pos_fr][f_r] = '- '
    print(board)
    return board