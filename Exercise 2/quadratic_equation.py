###################################################
# FILE : quadratic_equation.py
# WRITER : Omer Ferster , omerferster , 206893653
# EXERCISE : intro2cse ex2 2021
# DESCRIPTION: Quadratic equations solutions
###################################################

import math


def quadratic_equation(a, b, c):
    """ The function returns the quadratic equation (ax^2+bx+c=0) solutions
        param a: Ax^2 parameter
        param b: Bx parameter
        param c: C parameter """
    first_solution, second_solution = None, None  # Initial None for solutions
    discriminant = (b ** 2) - (4 * a * c)  # calculate the discriminant (Δ)
    if discriminant < 0:  # No Solutions.
        pass
    elif discriminant == 0:  # 1 Solution
        first_solution = -b / (2 * a)
    elif discriminant > 0:  # 2 Solutions
        first_solution = (-b + math.sqrt(discriminant)) / (2 * a)
        second_solution = (-b - math.sqrt(discriminant)) / (2 * a)
    return first_solution, second_solution  # returns the Solutions


def quadratic_equation_user_input():
    """ The function prints the quadratic equations solutions (ax^2+bx+c=0)
        according user coefficients input """
    coefficients_string = input("Insert coefficients a, b, and c: ")
    a, b, c = coefficients_string.split()  # extracting coefficients from list
    if float(a) == 0:
        print("The parameter 'a' may not equal 0")  # 'a' can't equal 0
    else:
        first_solution, second_solution = quadratic_equation(float(a),
                                                             float(b),
                                                             float(c))
        if first_solution is not None and second_solution is not None:
            print("The equation has 2 solutions:",
                  first_solution, "and", second_solution)
        elif first_solution is not None and second_solution is None:
            print("The equation has 1 solution:", first_solution)
        elif first_solution is None and second_solution is not None:
            print("The equation has 1 solution:", second_solution)
        elif first_solution is None and second_solution is None:
            print("The equation has no solutions")
