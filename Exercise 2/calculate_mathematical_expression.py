###################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : Omer Ferster , omerferster , 206893653
# EXERCISE : intro2cse ex2 2021
# DESCRIPTION: A calculations of math expressions in different ways
###################################################################


def calculate_mathematical_expression(first_num, second_num, chosen_operator):
    """ The function returns the result of a mathematical expression.
        param first_num: The first number in expression
        param second_num: The second number in expression
        param chosen_operator: The operator in the expression (+/-/*/:) """
    if chosen_operator == '+':
        return first_num + second_num  # returns the Sum
    elif chosen_operator == '-':
        return first_num - second_num  # returns the Subtraction
    elif chosen_operator == '*':
        return first_num * second_num  # returns the Multiplication
    elif chosen_operator == ':':
        if second_num != 0:
            return first_num / second_num  # returns the Division
        elif second_num == 0:
            return None  # Illegal division by zero
    else:
        return None  # chosen operator is not legal


def calculate_from_string(math_expression):
    """ The function returns the result of a string mathematical expression.
        param math_expression: The string type expression """
    first_num, chosen_operator, second_num = math_expression.split()
    return calculate_mathematical_expression(float(first_num),
                                             float(second_num),
                                             chosen_operator)
