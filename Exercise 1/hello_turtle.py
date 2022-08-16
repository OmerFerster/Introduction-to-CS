#################################################################
# FILE : hello_turtle.py
# WRITER : Omer Ferster , omerferster , 206893653
# EXERCISE : intro2cse ex1 2021
# DESCRIPTION: A simple program that use Turtle to draw a flowers garden
#################################################################

import turtle


def draw_petal():
    """ The Function draws a single Petal """
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)


def draw_flower():
    """ The function draws a single Flower """
    turtle.left(45)
    draw_petal()  # The next lines draws 4 petals
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(135)
    turtle.forward(150)  # drawing the straw of the flower


def draw_flower_and_advance():
    """ The function draws a single flower, and
        advance another place for another flower """
    draw_flower()  # drawing the flower
    turtle.right(90)  # The next lines make the advanced without drawing
    turtle.up()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.down()  # ready for drawing again at a new place


def draw_flower_bed():
    """ The function draws 3 flowers at the garden """
    turtle.up()  # The next lines moves turtle to starting point
    turtle.forward(200)
    turtle.left(180)
    turtle.down()
    draw_flower_and_advance()  # The next lines draws the garden
    draw_flower_and_advance()
    draw_flower_and_advance()


######################################

if __name__ == "__main__":
    draw_flower_bed()
    turtle.done()  # Turtle done drawing
