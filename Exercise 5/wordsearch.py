##################################################
# FILE : wordsearch.py
# WRITER : Omer Ferster , omerferster , 206893653
# EXERCISE : intro2cse ex5 2021
# DESCRIPTION: THE WORDS SEARCH GAME PROGRAM
##################################################

import sys
import os

DIRECTION_DICT = {'up': 'u', 'down': 'd', 'right': 'r', 'left': 'l',
                  'up/right': 'w', 'up/left': 'x', 'down/right': 'y',
                  'down/left': 'z'}
VALID_DIRECTIONS = 'udrlwxyz'
STRAIGHT_DIRECTIONS = 'udlr'
DIAGONAL_DIRECTIONS = 'wxyz'
INVALID_CHARS = ', \n'


def read_wordlist(filename):
    """ The function returns a list with all the words appears inside the file
        param filename: The file with all the words """
    words_file = open(filename, 'r')  # open words file
    words_list = [word[:-1] for word in words_file.readlines()]  # extract lst
    words_file.close()
    return words_list


def read_matrix(filename):
    """ The function returns a List with matrix pattern, every element in
        the returned list represent a single row, which contains letters.
        param filename: The matrix file name """
    matrix = []
    matrix_file = open(filename, 'r')  # open matrix file
    for row in matrix_file.readlines():
        spec_row = [char for char in row if char not in INVALID_CHARS]
        matrix.append(spec_row)
    matrix_file.close()
    return matrix


def check_direction(directions):
    """ The function check if the directions input is valid, returns True if
        valid, False and msg otherwise. VALID DIRECTIONS - 'u/d/r/l/w/x/y/z'
        param directions: The given directions input """
    for direction in set(directions):
        if direction not in VALID_DIRECTIONS:
            msg = 'You entered Invalid direction -> ' + direction
            return False, msg  # invalid direction
    msg = ''
    return True, msg  # all directions are valid


def check_files(words_file, matrix_file):
    """ The function checks the existence of words / matrix files,
        returns True if both exist, False and a fitting msg otherwise.
        param words_file: The words file name
        param matrix_file: The matrix file name """
    if not os.path.isfile(words_file):
        msg = 'The words file not found'
        return False, msg
    if not os.path.isfile(matrix_file):
        msg = 'The matrix file not found'
        return False, msg
    msg = ''
    return True, msg  # both file exists


def check_args_num(args):
    """ The function checks if there is 4 arguments from command line
        return True if there is exactly 4 args, False otherwise.
        param args: The list of args from command line """
    if len(args) == 4:
        return True
    return False


def check_input_args(args):
    """ The function checks if all args are valid, if valid it will returns
        None, else returns a fitting msg that describes the args error.
        param args: The list of args from command line """
    if not check_args_num(args):
        msg = 'You must enter exactly 4 args'
        return msg
    words_file = args[0]
    matrix_file = args[1]
    directions = args[3]
    valid, msg = check_files(words_file, matrix_file)
    if not valid:
        return msg
    valid, msg = check_direction(directions)
    if not valid:
        return msg
    return None  # all args are valid


def optional_index(matrix, word):
    """ The function returned a list of optionals indexes in matrix that might
        be the searching word, when the first letter in the word fits matrix
        param matrix: The nested list matrix
        param word: The specific word we are searching """
    return [[i, j] for i in range(len(matrix)) for j in
            range(len(matrix[0])) if matrix[i][j] == word[0]]


def straight_direct_word(matrix, row_num, column_num, word_length, direction):
    """ The function returns an optional single word within given args
        works only if the direction belongs to STRAIGHT_DIRECTIONS (u,d,l,r)
        param matrix: The nested list matrix
        params row_num, column_num: The start searching index from matrix
        param word_length: The length of the word
        param direction: The specific direction to search for """
    spec_word = ''
    for i in range(word_length):
        if direction == DIRECTION_DICT['up']:  # 'u' direction
            if row_num != -1:
                spec_word += matrix[row_num][column_num]
                row_num -= 1
        elif direction == DIRECTION_DICT['down']:  # 'd' direction
            if row_num != len(matrix):
                spec_word += matrix[row_num][column_num]
                row_num += 1
        elif direction == DIRECTION_DICT['right']:  # 'r' direction
            if column_num != len(matrix[0]):
                spec_word += matrix[row_num][column_num]
                column_num += 1
        elif direction == DIRECTION_DICT['left']:  # 'l' direction
            if column_num != -1:
                spec_word += matrix[row_num][column_num]
                column_num -= 1
    return spec_word


def diagonal_direct_word(matrix, row_num, column_num, word_length, direction):
    """ The function returns an optional single word within given args
        works only if the direction belongs to DIAGONAL_DIRECTIONS (w,x,y,z)
        param matrix: The nested list matrix
        params row_num, column_num: The start searching index from matrix
        param word_length: The length of the word
        param direction: The specific direction to search for """
    spec_word = ''
    for i in range(word_length):
        if direction == DIRECTION_DICT['up/right']:  # 'w' direction
            if column_num != len(matrix[0]) and row_num != -1:
                spec_word += matrix[row_num][column_num]
                row_num -= 1
                column_num += 1
        elif direction == DIRECTION_DICT['up/left']:  # 'x' direction
            if column_num != -1 and row_num != -1:
                spec_word += matrix[row_num][column_num]
                row_num -= 1
                column_num -= 1
        elif direction == DIRECTION_DICT['down/right']:  # 'y' direction
            if column_num != len(matrix[0]) and row_num != len(matrix):
                spec_word += matrix[row_num][column_num]
                row_num += 1
                column_num += 1
        elif direction == DIRECTION_DICT['down/left']:  # 'z' direction
            if column_num != -1 and row_num != len(matrix):
                spec_word += matrix[row_num][column_num]
                row_num += 1
                column_num -= 1
    return spec_word


def try_word(matrix, word_length, start_index, direction):
    """ The function returns an optional single word within given args
        param matrix: The nested list matrix
        param word_length: The length of the word
        param start_index: The start searching index from matrix
        param direction: The specific direction to search for """
    row, column = start_index[0], start_index[1]  # extract start index
    optional_word = ''
    if direction in STRAIGHT_DIRECTIONS:
        optional_word = straight_direct_word(matrix, row, column,
                                             word_length, direction)
    elif direction in DIAGONAL_DIRECTIONS:
        optional_word = diagonal_direct_word(matrix, row, column,
                                             word_length, direction)
    return optional_word


def find_words(word_list, matrix, directions):
    """ The function returns a list of tuples, each element contains a tuple
        with this form (word, counts), word and amount of appearances.
        param word_list: The list of words
        param matrix: The nested list matrix
        param directions: The directions to look for in matrix """
    result_list = []  # initial returned list of tuples as empty
    for word in word_list:
        count_index = 0  # index for counting word's appearances in matrix
        for optional in optional_index(matrix, word):
            for direction in set(directions):
                check_word = try_word(matrix, len(word), optional, direction)
                if check_word == word:
                    count_index += 1  # we found the word in the matrix
        if count_index > 0:
            result_list.append((word, count_index))  # appends a tuple
    return result_list


def write_output(results, filename):
    """ The function write the searches output in an output file,
        only words with at least 1 count will be writen in the returned file
        if file already exist, the content will be replaced, else creates new.
        param results: The result list of tuples search
        param filename: The output file name """
    output_file = open(filename, 'w')
    for elem in results:  # write tuples content
        output_file.write(elem[0] + ',' + str(elem[1]) + "\n")
    output_file.close()


def main():
    """ The main function that runs the whole searching game """
    msg = check_input_args(sys.argv[1:])
    if msg is None:  # all arguments are valid
        words_file = sys.argv[1]  # extracting all args from command line
        matrix_file = sys.argv[2]
        output_file = sys.argv[3]
        directions = sys.argv[4]
        words_list = read_wordlist(words_file)
        matrix = read_matrix(matrix_file)
        search_results = find_words(words_list, matrix, set(directions))
        write_output(search_results, output_file)
    else:
        print(msg)  # there is an error with the arguments


if __name__ == "__main__":
    main()
