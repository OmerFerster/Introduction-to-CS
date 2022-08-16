##################################################
# FILE : nonogram.py
# EXERCISE : intro2cse ex8 2021
# DESCRIPTION: THE NONOGRAM GAME WITH BACKTRACKING
# AUTHORS: omerferster, meshi.maman
##################################################

"""
PART B, SECTION 3:
we chose to present the option with the undecided box (-1) because
there isn't an agreement on the specific value of the box, in later parts
it will be clearer to understand that there was a disagreement, and will
prevent us from assigning wrong values in these boxes
"""

from copy import deepcopy


WHITE_BOX = 0
BLACK_BOX = 1
UNDECIDED_BOX = -1


def ones_row(possible_perm, blocks, block_ind):
    """
    The function finds whether a sequence answers it constrains blocks or not
    :param possible_perm: The possible sequence of boxes
    :param blocks: The constrains the sequence must stand for
    :param block_ind: The index pointing elements in constrains blocks
    :return: True if sequence is valid according blocks, False otherwise
    """
    count = 0  # counter of '1's boxes in a row
    for i in range(len(possible_perm)):
        if possible_perm[i] == BLACK_BOX:
            count += 1
        elif possible_perm[i] == WHITE_BOX:
            if count > 0 and count != blocks[block_ind]:
                return False  # found an wrong constraint
            elif count > 0 and count == blocks[block_ind]:
                if block_ind < len(blocks)-1:
                    block_ind += 1
                    count = 0  # restart counter, new constraint up next
    if count == blocks[block_ind] and block_ind == len(blocks) - 1:
        return True
    return False


def _const_helper(n, blocks, seq, result, block_ind, one_ind, seq_ind):
    """
     An helper function, finds all legal placings permutes due constrains
    :param n, blocks: The line length & The constrains list
    :param seq, result: The seq to check & The returned list
    :param block_ind: The index pointing specific constrain
    :param one_ind, seq_ind: The '1' counter & The sequence index
    :return: A list of lists with all legal solutions
    """
    if not blocks:
        return [[WHITE_BOX] * n]  # constrain is empty as []
    if one_ind == sum(blocks) and ones_row(seq, blocks, 0) and len(seq) == n:
        result.append(seq[:])  # base case, seq is a possible solution
        return
    if block_ind < len(blocks) and seq_ind + blocks[block_ind] <= len(seq):
        seq[seq_ind:seq_ind + blocks[block_ind]] = \
            [BLACK_BOX] * blocks[block_ind]  # placing '1's boxes
        _const_helper(n, blocks, seq, result, block_ind + 1,
                      one_ind + blocks[block_ind],
                      seq_ind + 1 + blocks[block_ind])
        seq[seq_ind:seq_ind + blocks[block_ind]] =\
            [WHITE_BOX] * blocks[block_ind]  # backtrack by placing '0's boxes
        if seq_ind < n - blocks[block_ind]:
            _const_helper(n, blocks, seq, result, block_ind,
                          one_ind, seq_ind + 1)
    return result


def constraint_satisfactions(n, blocks):
    """
    The function finds all legal permutes according the constrains
    :param n: The line length
    :param blocks: The constrains list
    :return: A list of lists with all possible legal placings
    """
    return _const_helper(n, blocks, [WHITE_BOX] * n, [], 0, 0, 0)


def _row_variations_helper(row, blocks, seq, result, row_ind, n, sum_blocks):
    """
    An helper function, finds all row legal solutions due constrains
    :param row, blocks: The row sequence & The constrains list
    :param seq, result: The sequence to check & The returned list
    :param row_ind: The index pointing the given row
    :param n, sum_blocks: The row length & The blocks constrains sum
    :return: A list of list, with all possible painting rows
    """
    if ones_row(seq, blocks, 0):
        result.append(seq[:])  # base case, seq answers a possible solution
        return
    if row_ind < n and row[row_ind] != UNDECIDED_BOX:
        seq[row_ind] = row[row_ind]
        _row_variations_helper(row, blocks, seq, result,
                               row_ind + 1, n, sum_blocks)
    if row_ind < n and row[row_ind] == UNDECIDED_BOX:
        if row.count(BLACK_BOX) < sum_blocks:
            seq[row_ind] = BLACK_BOX
            _row_variations_helper(row, blocks, seq, result,
                                   row_ind + 1, n, sum_blocks)
        if row.count(WHITE_BOX) < n - sum_blocks:
            seq[row_ind] = WHITE_BOX
            _row_variations_helper(row, blocks, seq, result,
                                   row_ind + 1, n, sum_blocks)
    return result


def row_variations(row, blocks):
    """
    The function finds all row legal solutions according the constrains
    :param row: The row sequence
    :param blocks: The constrains list
    :return: A list of list, with all possible painting rows
    """
    if not row and not blocks:
        return [[]]
    if row and not blocks:
        return [[WHITE_BOX] * len(row)]
    if row.count(BLACK_BOX) > sum(blocks) or (not row and blocks):
        return []
    return _row_variations_helper(row, blocks,
                                  [WHITE_BOX] * len(row),
                                  [], 0, len(row), sum(blocks))


def is_agreed(rows, ind):
    """
    An helper function, finds if there is a common solution agreed upon
    all rows in specific coordinate
    :param rows: The list of rows sequences
    :param ind: The specific coordinate to check in the rows
    :return: True & value, otherwise False & -1 as value
    """
    agreed = True  # initial check agreements flag
    agreed_num = UNDECIDED_BOX
    for i in range(len(rows)):
        if i != len(rows) - 1 and rows[i][ind] != rows[i + 1][ind]:
            agreed = False
            agreed_num = UNDECIDED_BOX  # there is no agreement
    if agreed:
        agreed_num = rows[0][ind]  # there is an agreement
    return agreed, agreed_num


def intersection_row(rows):
    """
    The function finds a row sequence that will be agreed by all rows
    :param rows: The list of rows with there boxes info
    :return: A list that represent an optional intersection solution
    """
    result = []  # initial intersection list as empty
    for i in range(len(rows[0])):
        if is_agreed(rows, i)[0]:
            result.append(is_agreed(rows, i)[1])  # appending agreeable box
        else:
            result.append(UNDECIDED_BOX)  # appending undecided box
    return result


def empty_board(row_len, column_len):
    """
    The function creates an empty board full with UNDECIDED_BOX boxes
    :param row_len: The rows number
    :param column_len: The columns number
    :return: A list of lists represent the empty board
    """
    board = []  # returned board list initial as empty
    for i in range(row_len):
        row = []  # new row every iteration inside loop
        for j in range(column_len):
            row.append(UNDECIDED_BOX)
        board.append(row)
    return board


def count_undecided(board):
    """
    The function find how many UNDECIDED_BOX (-1) there is in the board
    :param board: The list of lists represent the board game
    :return: A counter of how many (-1) boxes found in the board
    """
    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == UNDECIDED_BOX:
                count += 1  # founded an undecided box
    return count


def spec_col(board, col_ind):
    """
    The function find the column list presentation
    :param board: The board game as list of lists
    :param col_ind: The specific column index
    :return: A list represent the column boxes
    """
    col_lst = []
    for i in range(len(board)):
        col_lst.append(board[i][col_ind])
    return col_lst


def optional_rows_board(constraints, board):
    """
    The function finds an optional solution board only for rows constrains
    :param constraints: The whole board row constrains
    :param board: The board game
    :return: An optional board answering the rows constrains in the game
    """
    if board is None:
        return None
    for i in range(len(constraints[0])):
        if sum(constraints[0][i]) <= len(board[i]):
            if board[i].count(UNDECIDED_BOX) != 0:
                option = row_variations(board[i], constraints[0][i])
                if len(option) == 1:
                    board[i] = option[0]  # there is only one option possible
                elif len(option) > 1:
                    board[i] = intersection_row(option)  # intersect options
        else:
            return None  # The constraint is illegal
    return board


def optional_column_board(constraints, board):
    """
    The function finds an optional solution board only for column constrains
    :param constraints: The whole board column constrains
    :param board: The board game
    :return: An optional board answering the column constrains in the game
    """
    if board is None:
        return None
    for i in range(len(constraints[1])):
        col = spec_col(board, i)
        if sum(constraints[1][i]) <= len(col):
            if col.count(UNDECIDED_BOX) != 0:
                option = row_variations(col, constraints[1][i])
                if len(option) == 1:
                    for j in range(len(board)):
                        board[j][i] = option[0][j]  # only one option
                elif len(option) > 1:
                    option = intersection_row(option)  # intersect all options
                    for j in range(len(board)):
                        board[j][i] = option[j]
        else:
            return None  # The constraint is illegal
    return board


def solve_easy_helper(constrains, board):
    """
    An helper function, finds A possible solution if there is one,
    The function is running until it cannot be solved anymore
    :param constrains: The list of constrains
    :param board: The board game
    :return: A possible board solution, or A partial solution it gets to
    """
    if board is None:
        return None
    while True:
        new_board =\
            optional_column_board(constrains,
                                  optional_rows_board(constrains, board))
        if new_board is None:
            return None
        count_minus = count_undecided(new_board)
        if not count_minus:
            break  # found a solution
        if count_minus ==\
                count_undecided(optional_rows_board(constrains, new_board)):
            return new_board  # return partial solution
    if valid_solution(constrains, new_board):
        return new_board  # valid solution
    return None  # illegal solution


def valid_solution(constrains, board):
    """
    The function finds if the board is a legal solution or not due constrains
    :param constrains: The whole constrains list
    :param board: The solved board game
    :return: True if board is valid, False otherwise
    """
    for i in range(len(constrains[0])):
        option = row_variations(board[i], constrains[0][i])
        if len(option) != 1 or board[i] != option[0]:
            return False  # found an exception
    for j in range(len(constrains[1])):
        col = spec_col(board, j)
        option = row_variations(col, constrains[1][j])
        if len(option) != 1 or col != option[0]:
            return False  # found an exception
    return True


def solve_easy_nonogram(constrains):
    """
    The function solves The nonogram game according constrains given
    :param constrains: The constrains list
    :return: The whole / partial solved board, or None if illegal constrains
    """
    board = empty_board(len(constrains[0]), len(constrains[1]))  # init board
    return solve_easy_helper(constrains, board)


def all_board_index(board):
    """
    The function finds all indexes of the board list of lists
    :param board: The lists of lists board game
    :return: A list of tuples, each tuple represent a of row, column indexes
    """
    final_lst = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            final_lst.append((i, j))  # appends indexes from board
    return final_lst


def ones_needed(constrains):
    """
    The function finds how many BLACK BOXES '1' must have in a solved board
    :param constrains: The list of constrains
    :return: A number represent the count of how many '1's must have in board
    """
    count = 0
    for const in constrains[0]:
        count += sum(const)  # adding each constrains '1' requirement
    return count


def count_value_in_board(board, val):
    """
    The function finds how many appearances value has in our board game
    :param board: The game board list of lists
    :param val: The specific value to count in the board
    :return: A counter represent the number of appearances of val in board
    """
    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == val:
                count += 1  # found an appearance
    return count


def solve_nonogram_helper(constrains, result, board, all_inds, ind):
    """
    An helper function, finds all possible solutions for the nonogram game
    :param constrains: The list of constraints
    :param result: The result list that will be returned with all solutions
    :param board: The list of lists representing the board game
    :param all_inds: A list of tuples, represent a row, column index in board
    :param ind: The board boxes index
    :return: A list of all possible and legal solutions if there are any
    """
    if valid_solution(constrains, board) and board not in result:
        result.append(deepcopy(board))  # base case, found a valid solution
        return
    if ind < len(all_inds):
        if board[all_inds[ind][0]][all_inds[ind][1]] != UNDECIDED_BOX:
            solve_nonogram_helper(constrains, result, board, all_inds, ind+1)
        if board[all_inds[ind][0]][all_inds[ind][1]] == UNDECIDED_BOX and\
                count_value_in_board(board, BLACK_BOX)\
                < ones_needed(constrains):
            board[all_inds[ind][0]][all_inds[ind][1]] = BLACK_BOX
            solve_nonogram_helper(constrains, result, board, all_inds, ind+1)
            board[all_inds[ind][0]][all_inds[ind][1]] = UNDECIDED_BOX
        if board[all_inds[ind][0]][all_inds[ind][1]] == UNDECIDED_BOX and\
                count_value_in_board(board, WHITE_BOX)\
                < len(all_inds) - ones_needed(constrains):
            board[all_inds[ind][0]][all_inds[ind][1]] = WHITE_BOX
            solve_nonogram_helper(constrains, result, board, all_inds, ind+1)
            board[all_inds[ind][0]][all_inds[ind][1]] = UNDECIDED_BOX
    return result


def solve_nonogram(constrains):
    """
    The function solves A whole nonogram game according to given constrains
    :param constrains: The list of constrains
    :return: A list with all possible game solutions
    """
    board = solve_easy_nonogram(constrains)
    if board is None:
        return []
    if valid_solution(constrains, board):
        return [board]  # returns only one solution
    return solve_nonogram_helper(constrains, [], board,
                                 all_board_index(board), 0)
