################################################################
# FILE : largest_and_smallest.py
# WRITER : Omer Ferster , omerferster , 206893653
# EXERCISE : intro2cse ex2 2021
# DESCRIPTION: Finding max/min numbers from given parameters
################################################################

# check_largest_and_smallest --> my additional tests reasons:
# if largest_and_smallest(-99, -5.3, -6) == (-5.3, -99):
# reason - all numbers are negative, also checking float type
# if largest_and_smallest(0, -2, 0) == (0, -2):
# reason - two numbers are 'largest' not one, also checking 0 value


def largest_and_smallest(first_num, second_num, third_num):
    """ The function returns the Largest number and the Smallest number
        as a Tuple with this form (largest, smallest).
        param first_num: The first number
        param second_num: The second number
        param third_num: The third number """
    largest, smallest = None, None  # Initial values as None
    if first_num >= second_num and first_num >= third_num:
        largest = first_num  # first case (1st num is largest)
        if second_num >= third_num:  # finding smallest between 2 left numbers
            smallest = third_num
        else:
            smallest = second_num
    elif second_num >= first_num and second_num >= third_num:
        largest = second_num  # second case (2nd num is largest)
        if first_num >= third_num:  # finding smallest between 2 left numbers
            smallest = third_num
        else:
            smallest = first_num
    elif third_num >= first_num and third_num >= second_num:
        largest = third_num  # third case (3rd num is largest)
        if first_num >= second_num:  # finding smallest between 2 left numbers
            smallest = second_num
        else:
            smallest = first_num
    return largest, smallest  # returns final largest/smallest that founded


def check_largest_and_smallest():
    """ The function checks if largest_and_smallest function returning
        the predictable values according divers cases.
        returns True if all outputs expected, False otherwise """
    if largest_and_smallest(17, 1, 6) == (17, 1):
        if largest_and_smallest(1, 17, 6) == (17, 1):
            if largest_and_smallest(1, 1, 2) == (2, 1):
                if largest_and_smallest(-99, -5.3, -6) == (-5.3, -99):
                    if largest_and_smallest(0, -2, 0) == (0, -2):
                        return True  # all cases are working
    return False  # not all cases are working
