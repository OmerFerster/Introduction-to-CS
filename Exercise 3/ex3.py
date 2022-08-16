#############################################################
# FILE : ex3.py
# WRITER : Omer Ferster , omerferster , 206893653
# EXERCISE : intro2cse ex3 2021
# DESCRIPTION: A program that use Loops/Lists in varied ways
#############################################################


def input_list():
    """ The function returns a list with all numbers from user inputs and
        appends the SUM of them at the last place in list.
        The program gets inputs until the user input: '' (empty string) """
    EXIT = ''  # The exit input, finish the program
    num_list = []
    inputs_sum = 0  # initial value for sum
    user_input = input()
    while user_input != EXIT:
        num_list.append(float(user_input))  # appends num to list
        inputs_sum += float(user_input)  # sums all numbers in list
        user_input = input()  # asking for a new input
    num_list.append(inputs_sum)  # appends sum at last place in list
    return num_list


def inner_product(vec_1, vec_2):
    """ The function returns the inner multiplication between 2 lists
        at this from: x1*y1 + x2*y2 ... + x(n)*y(n)
        param vec_1: The first vector as a list
        param vec_2: The second vector as a list """
    if len(vec_1) != len(vec_2):
        return None  # returns None if vectors length not equal
    if vec_1 == [] and vec_2 == []:
        return 0  # returns 0 if both vectors are empty
    sum_of_vector = 0
    for i in range(len(vec_1)):
        sum_of_vector += vec_1[i] * vec_2[i]  # sums the inner multiplication
    return sum_of_vector


def sequence_monotonicity(sequence):
    """ The function returns a boolean values list with the sequence
        monotonicity at this from: [UP, VERY UP, DOWN, VERY DOWN].
        if the sequence fits the monotonicity it become True, False otherwise.
        param sequence: The a(n) numbers """
    monotonicity_list = [True, True, True, True]  # Initial list value
    for i in range(len(sequence) - 1):
        if sequence[i] < sequence[i + 1]:  # UP monotonicity
            if monotonicity_list[2] or monotonicity_list[3]:
                monotonicity_list[2] = False
                monotonicity_list[3] = False
        elif sequence[i] > sequence[i + 1]:  # DOWN monotonicity
            if monotonicity_list[0] or monotonicity_list[1]:
                monotonicity_list[0] = False
                monotonicity_list[1] = False
        elif sequence[i] == sequence[i + 1]:
            monotonicity_list[1] = False  # can't be 'VERY' UP/DOWN
            monotonicity_list[3] = False
    return monotonicity_list


def monotonicity_inverse(def_bool):
    """ The function returns an example of numbers that fits the monotonicity.
        param def_bool: The monotonicity sequence (True/False)
        at this form: [T/F, T/F, T/F, T/F] """
    UP = [1, 5, 5, 13]  # UP monotonicity
    VERY_UP = [1, 2, 3, 4]  # VERY UP monotonicity
    DOWN = [88, 23.5, 4, 4]  # DOWN monotonicity
    VERY_DOWN = [100, 30, 0, -10]  # VERY DOWN monotonicity
    EQUAL = [2, 2, 2, 2]  # UP & DOWN monotonicity
    NON_VALID = [1, 0, 6, 6]  # NON-VALID sequence
    if sequence_monotonicity(UP) == def_bool:
        return UP
    elif sequence_monotonicity(VERY_UP) == def_bool:
        return VERY_UP
    elif sequence_monotonicity(DOWN) == def_bool:
        return DOWN
    elif sequence_monotonicity(VERY_DOWN) == def_bool:
        return VERY_DOWN
    elif sequence_monotonicity(EQUAL) == def_bool:
        return EQUAL
    elif sequence_monotonicity(NON_VALID) == def_bool:
        return NON_VALID
    else:
        return None  # illegal sequence


def is_prime(num):
    """ The function returns True if num is prime, False otherwise.
        param num: The number we checking """
    if (num % 2 == 0 and num != 2) or num < 2:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False  # num isn't prime
    return True  # num is prime


def primes_for_asafi(n):
    """ The function returns a list with the first 'n' prime numbers
        param n: The amount of prime numbers in returned list """
    if n == 0:
        return []
    elif n > 0:
        prime_index = 1  # index for how many primes we found
        prime_list = [2]  # initial value for prime list
        check_num = 3  # first num to check
        while prime_index != n:
            if check_num % 2 != 0:
                if is_prime(check_num):
                    prime_list.append(check_num)  # appends prime num to list
                    check_num += 1  # continue for next num
                    prime_index += 1
                else:
                    check_num += 1
            else:
                check_num += 1
        return prime_list


def sum_of_coordinate(vec_list, coordinate):
    """ The function returns the sum of a single coordinate vectors
        at this form - [x1+y1+z1]
        param vec_list: The vector list
        param coordinate: The specific coordinate chosen to sum """
    if vec_list:  # checking if coordinate not empty
        coordinate_sum = 0  # initial value for sum
        for i in range(len(vec_list)):
            for j in range(len(vec_list[0])):
                if j == coordinate:  # checks if it at the right coordinate
                    coordinate_sum += vec_list[i][j]
        return coordinate_sum
    elif not vec_list:  # if vector is empty
        return None


def sum_of_vectors(vec_lst):
    """ The function returns a vector as the sum of coordinates in vec_lst
        at this form - [x1+y1+z1, x2+y2+z2... + x(n)+y(n)+z(n)]
        param vec_lst: The list of vectors """
    result_vector = []
    if not vec_lst:  # checks if vec_lst is empty
        return None
    else:
        for k in range(len(vec_lst[0])):
            spec_coordinate_sum = sum_of_coordinate(vec_lst, k)  # finds sum
            result_vector.append(spec_coordinate_sum)
        return result_vector


def num_of_orthogonal(vectors):
    """ The function returns how many orthogonal vectors pears have founded
        at this form - [x1*y1 + x2*y2... + x(n)*y(n)] = 0
        An orthogonal pear means they're inner product equals 0.
        param vectors: The vectors list """
    orthogonal_pears = 0  # index counting orthogonal pears founded
    for i in range(len(vectors)):
        for j in range(len(vectors)):
            if i != j and inner_product(vectors[i], vectors[j]) == 0:
                orthogonal_pears += 1  # found an orthogonal pear
    return int(orthogonal_pears / 2)
