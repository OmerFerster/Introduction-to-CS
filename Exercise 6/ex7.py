##################################################
# FILE : ex7.py
# WRITER : Omer Ferster , omerferster , 206893653
# EXERCISE : intro2cse ex7 2021
# DESCRIPTION: VARIED FUNCTIONS WITH RECURSION
##################################################

from typing import Any, List, Tuple


def print_to_n(n: int) -> None:
    """ The function prints the numbers between 1 - n in ascending order
        param n: The last number to print """
    if n >= 1:
        print_to_n(n - 1)
        print(n)


def digit_sum(n: int) -> int:
    """ The function returns the digits sum of 'n' (NON-negative number)
        param n: The number whose digit's will be summed """
    if n % 10 == n:
        return n  # base case, last digit occur
    return n % 10 + digit_sum(n // 10)


def has_divisor_smaller_than(n: int, i: int) -> bool:
    """ The function checks if 'n' got a smaller divisor than 'i'
        returns True if has, False otherwise
        param n, i: The main number to check & The upper bound divisor """
    if n < 2 or i < 2:
        return False
    elif n % (i - 1) == 0 and i != 2 and n != i - 1:
        return True  # founded a smaller divisor
    return has_divisor_smaller_than(n, i - 1)


def is_prime(n: int) -> bool:
    """ The function returns True if 'n' is prime, False otherwise
        param n: The number to check """
    if n > 2 and n % 2 == 0:
        return False  # even numbers can't be prime except '2'
    if n > 1 and not has_divisor_smaller_than(n, int(n ** 0.5) + 1):
        return True  # 'n' is prime, checking until the square root of 'n'
    return False


def play_hanoi(hanoi: Any, n: int, src: Any, dst: Any, temp: Any) -> None:
    """ The function plays the hanoi game, moves all discs from starting stick
        to target stick without placing larger disc on top of smaller ones
        param hanoi: The complex hanoi object field
        param n: The number of discs to move
        param src, dst, temp: The starting / target / temporary sticks """
    if n <= 0:
        return
    if n == 1:
        hanoi.move(src, dst)  # base case only 1 disc left to move
    if n > 1:
        play_hanoi(hanoi, n - 1, src, temp, dst)  # assume n-1 move to temp
        hanoi.move(src, dst)  # move largest disc to target stick
        play_hanoi(hanoi, n - 1, temp, dst, src)  # assume n-1 move to target


def _print_sequences_helper(char_lst: List[str], seq: str, n: int) -> None:
    """ The function prints all permutation possible in char list
        with 'n' length for each permute, can include repetition of chars
        param char_list: The char list to permute
        param seq & n: The seq to permute & The length of each permute """
    if n == 0:
        print(seq)  # base case, seq reached length of 'n'
        return
    for i in range(len(char_lst)):
        new_seq = seq + char_lst[i]
        _print_sequences_helper(char_lst, new_seq, n - 1)  # simpler recursion


def print_sequences(char_list: List[str], n: int) -> None:
    """ The function prints all permutations in char_list with length 'n'
        param char_list: The list of chars to permute
        param n: The length of each permutation """
    _print_sequences_helper(char_list, '', n)


def _print_no_repetition_help(char_lst: List[str], seq: str, n: int) -> None:
    """ The function prints all permutation possible in char list
        with 'n' length for each permute, not include repetition of chars
        param char_list: The char list to permute
        param seq & n: The seq to permute & The length of each permute """
    if n == 0:
        print(seq)  # base case, seq reached length of 'n'
        return
    for i in range(len(char_lst)):
        if seq.count(char_lst[i]) == 0:  # prevent duplicates of chars
            new_seq = seq + char_lst[i]
            _print_no_repetition_help(char_lst, new_seq, n - 1)


def print_no_repetition_sequences(char_list: List[str], n: int) -> None:
    """ The function prints all permutations in char_list with length 'n',
        prints only permutes with no repetitions of chars.
        param char_list: The list of chars to permute
        param n: The length of each permutation """
    _print_no_repetition_help(char_list, '', n)


def _paren_helper(n: int, final: List[str],
                  left: int, right: int, seq: str) -> List[str]:
    """ The function returns a list with all possible permutes with 'n' length
        param left, right: The indexes of how many '(' / ')' in each permute
        param seq, final: The sequence & The returned final permutes lst
        param n: The length of how many '()' there is in each permute """
    if right == 0 and left == 0:  # base case, there is equal '(' and ')'
        final.append(seq)
    if left > 0:
        _paren_helper(n, final, left - 1, right, seq + "(")
    if right > left:
        _paren_helper(n, final, left, right - 1, seq + ")")
    return final


def parentheses(n: int) -> List[str]:
    """ The function returns a list with all parentheses permutes length 'n'
        param n: The length of how many '()' there is in each permute """
    return _paren_helper(n, [], n, n, '')


def flood_fill(image: List[List[str]], start: Tuple[int, int]) -> None:
    """ The function changes the matrix according to the flood fill game
        param image: The nested list matrix with '.' and '*'
        param start: A tuple representing the start index in matrix """
    row, column = start[0], start[1]  # extract matrix location
    if image[row][column] == ".":
        image[row][column] = "*"  # base case, filling the index with '*'
        if row > 0:
            new_start = row - 1, column
            flood_fill(image, new_start)  # check up
        if row < len(image) - 1:
            new_start = row + 1, column
            flood_fill(image, new_start)  # check down
        if column > 0:
            new_start = row, column - 1
            flood_fill(image, new_start)  # check left
        if column < len(image[0]) - 1:
            new_start = row, column + 1
            flood_fill(image, new_start)  # check right
