#################################################################
# FILE : math_print.py
# WRITER : Omer Ferster , omerferster , 206893653
# EXERCISE : intro2cse ex1 2021
# DESCRIPTION: A simple program that uses math library functions
#################################################################

import math


def golden_ratio():
    """ The function prints the golden ratio """
    print((1 + math.sqrt(5)) / 2)


def six_squared():
    """ The function prints 6 power by 2 value """
    print(math.pow(6, 2))


def hypotenuse():
    """ The function prints the hypotenuse value of 12 and 5 right triangle """
    print(math.sqrt(math.pow(12, 2) + math.pow(5, 2)))


def pi():
    """ The function print the π value """
    print(math.pi)


def e():
    """ The function prints the e value """
    print(math.e)


def squares_area():
    """ The function prints the squares area between 1-10 length """
    print(math.pow(1, 2), math.pow(2, 2), math.pow(3, 2),
          math.pow(4, 2), math.pow(5, 2), math.pow(6, 2),
          math.pow(7, 2), math.pow(8, 2), math.pow(9, 2), math.pow(10, 2))


######################################

if __name__ == "__main__":
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()
