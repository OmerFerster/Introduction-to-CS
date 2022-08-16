
import sys
from car import Car
from board import Board
from helper import load_json


class Game:

    """
    The class represent the Game object, each game initializes with
    his Board object that the game will be played on him.
    The class handles A full session of the RUSH HOUR game by getting user
    input each turn and moves the cars accordingly. A game will be finished
    only when user choose to stop or if a certain car reach the target cell
    """

    VALID_NAMES = 'YBOGWR'
    VALID_DIRECTIONS = 'udlr'
    VALID_ORIENTATIONS = '01'
    MIN_LENGTH, MAX_LENGTH = 2, 4
    COMMA, STOP = ',', '!'
    COMMA_IND = 1
    STOPPED = 'The game has stopped'
    WON = 'You Won the game'

    def __init__(self, board):
        """
        Initialize a new Game object
        :param board: An object of type board
        """
        self.__board = board  # The Board object the game will played on

    def __single_turn(self):
        """
        The function responsible A single turn iteration of the game, include
        A treatment to user input, check it validness and make moves according
        to user choice, if input is invalid An appropriate msg will be printed
        :return: None while user input is not STOP game or WIN game
        """
        user_input = input()
        if user_input == Game.STOP:
            return Game.STOPPED  # user choose to stop the game
        if len(user_input) == 3 and user_input[Game.COMMA_IND] == Game.COMMA:
            car_name, direction = user_input.split(Game.COMMA)  # extract move
            if car_name not in Game.VALID_NAMES:
                print('Your car name is invalid')
            elif direction not in Game.VALID_DIRECTIONS:
                print('Your direction is invalid')
            elif self.__board.move_car(car_name, direction):
                print(self.__board)  # print updated board after the move
                if self.__board.cell_content(self.__board.target_location()):
                    return Game.WON  # user reach target cell (3, 7)
            else:
                print('Your move is invalid')  # cannot apply user move
        else:
            print('Your input must follow this form: Name,Direction')

    def play(self):
        """
        The main driver of the Game. Manages the game until completion
        :return: None
        """
        if self.__board.cell_content(self.__board.target_location()):
            print(Game.WON)
        else:
            turn = self.__single_turn()
            while turn != Game.STOPPED and turn != Game.WON:
                turn = self.__single_turn()
            print(turn)  # prints whether user won / stopped the game


if __name__ == "__main__":
    board = Board()
    car_config = dict(load_json(sys.argv[1]))  # extract game info form json
    for name in car_config:
        length = car_config[name][0]
        location = tuple(car_config[name][1])
        orientation = car_config[name][2]
        if name in Game.VALID_NAMES:
            if Game.MIN_LENGTH <= length <= Game.MAX_LENGTH:
                if location in board.cell_list():
                    if str(orientation) in Game.VALID_ORIENTATIONS:
                        car_object = Car(name, length, location, orientation)
                        if board.add_car(car_object):
                            pass  # The car has been added successfully
    game = Game(board)
    print(board)
    game.play()  # starting A game
