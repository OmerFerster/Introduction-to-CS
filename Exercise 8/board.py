##################################################
# FILES : board.py, car.py, game.py
# WRITER : Omer Ferster , omerferster , 206893653
# EXERCISE : intro2cse ex9 2021
# DESCRIPTION: RUSH HOUR GAME WITH OOP
##################################################

ROW = 0
COLUMN = 1


class Board:

    """
    The class represent the Board game, The board initializes as 7*7 sized
    with empty spaces and A cars list represent all the cars that participate
    in our game and places inside the board. The board handles situations of
    moving cars across it according their possible moves and user choice
    """

    WIN_CELL = (3, 7)
    BOARD_SIZE = 7
    MIDDLE_ROW = 3
    EMPTY_SPOT = '_'

    def __init__(self):
        """ The function initialize A board with an empty list of cars """
        self.__cars = []  # The cars list in the board
        self.__board = [[Board.EMPTY_SPOT for _ in range(Board.BOARD_SIZE)]
                        for _ in range(Board.BOARD_SIZE)]  # board creation
        self.__board[Board.MIDDLE_ROW].append(Board.EMPTY_SPOT)

    def __str__(self):
        """
        This function is called when a board object is to be printed
        :return: A string of the current status of the board
        """
        printed_board = ''
        for line in self.__board:
            printed_board += ' '.join(line) + '\n'  # join every line
        return printed_board

    def cell_list(self):
        """
        This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        cell_lst = [(row_ind, col_ind) for row_ind in range(len(self.__board))
                    for col_ind in range(len(self.__board[0]))]
        cell_lst.append(self.target_location())
        return cell_lst

    def possible_moves(self):
        """
        This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description)
        representing legal moves
        """
        moves_lst = []  # initial moves list as empty
        for car in self.__cars:
            moves = car.possible_moves()
            for key in moves:
                requirement_cell = car.movement_requirements(key)[0]
                if requirement_cell in self.cell_list():
                    if self.cell_content(requirement_cell) is None:
                        moves_lst.append((car.get_name(), key, moves[key]))
        return moves_lst

    def target_location(self):
        """
        This function returns the coordinate which must be filled for victory
        :return: (row,col) of goal location
        """
        return Board.WIN_CELL

    def cell_content(self, coordinate):
        """
        The function checks if the given coordinates are empty
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        if coordinate in self.cell_list():
            row_ind, col_ind = coordinate
            if self.__board[row_ind][col_ind] != Board.EMPTY_SPOT:
                return self.__board[row_ind][col_ind]  # returns car name
        return None  # The cell is empty

    def add_car(self, car):
        """
        The function adds a car to the game board and cars list
        :param car: car object of car to add
        :return: True upon success, False if failed
        """
        if self.__name_exist(car.get_name())\
                or not self.__all_coords_in_board(car)\
                or self.__already_taken_place(car):
            return False  # can't add car to the board
        self.__cars.append(car)  # adds car to cars list
        self.__filled_cells_with(car, car.get_name())
        return True  # succeeded adding the car into the board

    def move_car(self, name, movekey):
        """
        The function moves car one step in given direction on the board
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        car = self.__car_from_name(name)  # extract car object from name
        if car is None or not car.movement_requirements(movekey):
            return False  # requirements movekey is invalid
        requirement_cell = car.movement_requirements(movekey)[0]
        if self.cell_content(requirement_cell)\
                or requirement_cell not in self.cell_list():
            return False  # cannot move towards this cell
        self.__filled_cells_with(car, Board.EMPTY_SPOT)  # erase old car place
        if car.move(movekey):
            self.__filled_cells_with(car, car.get_name())  # placing new place
            return True  # move has been occur
        return False

    def __name_exist(self, name):
        """
        The function finds if a certain car exist in our board game
        :param name: The car name
        :return: True if car exist in the board, False otherwise
        """
        for car in self.__cars:
            if car.get_name() == name:
                return True  # already got this car in board
        return False

    def __all_coords_in_board(self, car):
        """
        The function finds if all car coordinate are valid inside board cells
        :param car: A car object in the game
        :return: True if all car coordinates are valid, False otherwise
        """
        cells_lst = self.cell_list()
        for coord in car.car_coordinates():
            if coord not in cells_lst:
                return False  # invalid cell, not inside board
        return True  # all car cells inside board

    def __already_taken_place(self, car):
        """
        The function finds if car can be placed in it coordinates or not
        :param car: The car object
        :return: False if all coords in empty spaces, True otherwise
        """
        for coord in car.car_coordinates():
            if self.cell_content((coord[ROW], coord[COLUMN])):
                return True  # already taken cell
        return False

    def __car_from_name(self, name):
        """
        The function returns the car object that has this specific name
        :param name: The name of the car
        :return: A car object with this current name or None if not founded
        """
        for car in self.__cars:
            if car.get_name() == name:
                return car

    def __filled_cells_with(self, car, char):
        """
        The function placed the char in every car coordinate in the board
        :param car: The car object that about to make a move
        :param char: The specific char the coordinates will be fill with
        :return: None
        """
        filled_cells = car.car_coordinates()
        for coord in filled_cells:
            self.__board[coord[ROW]][coord[COLUMN]] = char
