###################################################
# FILE : shapes.py
# WRITER : Omer Ferster , omerferster , 206893653
# EXERCISE : intro2cse ex2 2021
# DESCRIPTION: A calculations of shapes area
# according user input: (shape and dimensions)
###################################################

import math

PI = math.pi


def circle_area(radius):
    """ The function returns the circle area with given radius.
        param radius: The circle radius """
    return PI * (radius**2)  # returns circle area


def rectangle_area(vertical_side, horizontal_side):
    """ The function returns the rectangle area with given sides.
        param vertical_side: The first side of the rectangle
        param horizontal_side: The second side of the rectangle """
    return vertical_side * horizontal_side  # returns rectangle area


def triangle_area(triangle_length):
    """ The function returns an all equal sides triangle area.
        param triangle_length: The triangle length """
    return ((triangle_length**2) * math.sqrt(3)) / 4  # returns triangle area


def shape_area():
    """ The function returns the area of shapes (circle,rectangle,triangle).
        The user choose the shape dimensions according his input """
    user_choice = input("Choose shape (1=circle, 2=rectangle, 3=triangle): ")
    if user_choice == '1':  # circle has been chosen
        circle_radius = float(input())
        return circle_area(circle_radius)
    elif user_choice == '2':   # rectangle has been chosen
        first_rectangle_side = float(input())
        second_rectangle_side = float(input())
        return rectangle_area(first_rectangle_side, second_rectangle_side)
    elif user_choice == '3':   # triangle has been chosen
        triangle_side = float(input())
        return triangle_area(triangle_side)
    else:
        return None  # returns None if choice is Non-Valid
