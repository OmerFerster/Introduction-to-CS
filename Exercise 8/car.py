
ROW = 0
COLUMN = 1


class Car:

    """
    The class represent the Cars objects, each car in the game initializes
    with it properties: name, length, location, orientation.
    VERTICAL cars can only move UP & DOWN directions.
    HORIZONTAL cars can only move LEFT & RIGHT directions.
    The class handles situations of changing car coordinates according to a
    valid movekey for a specific car object.
    """

    VERTICAL_MOVES = 'ud'
    HORIZONTAL_MOVES = 'lr'
    VERTICAL = 0
    HORIZONTAL = 1
    UP, DOWN, RIGHT, LEFT = 'u', 'd', 'r', 'l'

    def __init__(self, name, length, location, orientation):
        """
        The function represent A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) cell
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        head_row, head_col = self.__location
        car_coords = [self.__location]  # initial car coords lst with head
        for i in range(1, self.__length):
            if self.__orientation == Car.VERTICAL:
                car_coords.append((head_row + i, head_col))  # vertical car
            elif self.__orientation == Car.HORIZONTAL:
                car_coords.append((head_row, head_col + i))  # horizontal car
        return car_coords

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements
        permitted by this specific car
        """
        vertical_dict = {'u': 'moves the car 1 step UP, -1 from row ind',
                         'd': 'moves the car 1 step DOWN, +1 to row ind'}
        horizontal_dict = {'l': 'moves the car 1 step LEFT, -1 from col ind',
                           'r': 'moves the car 1 step RIGHT, +1 to col ind'}
        if self.__orientation == Car.VERTICAL:
            return vertical_dict
        elif self.__orientation == Car.HORIZONTAL:
            return horizontal_dict

    def movement_requirements(self, movekey):
        """
        :param movekey: A string representing the key of the required move
        :return: A list of cell locations which must be empty in order for
        this move to be legal
        """
        must = []  # initial returned lst as empty
        car_coords = self.car_coordinates()  # extract car coordinates
        if self.__orientation == Car.VERTICAL:
            if movekey == Car.UP:
                must.append((car_coords[0][ROW] - 1, car_coords[0][COLUMN]))
            if movekey == Car.DOWN:
                must.append((car_coords[-1][ROW] + 1, car_coords[-1][COLUMN]))
        elif self.__orientation == Car.HORIZONTAL:
            if movekey == Car.LEFT:
                must.append((car_coords[0][ROW], car_coords[0][COLUMN] - 1))
            if movekey == Car.RIGHT:
                must.append((car_coords[-1][ROW], car_coords[-1][COLUMN] + 1))
        return must  # A 'must be empty' cells returned

    def move(self, movekey):
        """
        :param movekey: A string representing the key of the required move
        :return: True upon success, False otherwise
        """
        if self.movement_requirements(movekey):
            if self.__orientation == Car.VERTICAL:
                if movekey in Car.VERTICAL_MOVES:
                    self.__change_coords(movekey)  # changing car coordinates
                    return True
            elif self.__orientation == Car.HORIZONTAL:
                if movekey in Car.HORIZONTAL_MOVES:
                    self.__change_coords(movekey)  # changing car coordinates
                    return True
        return False  # invalid move

    def get_name(self):
        """
        :return: The name of this car
        """
        return self.__name

    def __change_coords(self, movekey):
        """
        The function updates the car coordinates according to the movekey
        :param movekey: The direction the car need to move
        :return: An updated list of tuples which represent car coordinates
        """
        head = self.__location  # The head location of the car
        if self.__orientation == Car.VERTICAL:
            if movekey == Car.UP:
                self.__location = (head[ROW] - 1, head[COLUMN])
            if movekey == Car.DOWN:
                self.__location = (head[ROW] + 1, head[COLUMN])
        elif self.__orientation == Car.HORIZONTAL:
            if movekey == Car.LEFT:
                self.__location = (head[ROW], head[COLUMN] - 1)
            if movekey == Car.RIGHT:
                self.__location = (head[ROW], head[COLUMN] + 1)
        return self.car_coordinates()  # returns new coordinates
