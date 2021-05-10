"""
Snake game implementation.
"""

import random


class Board:
    """
    Snake game board with basic play functionality that combines
    interactions between the snake, food, and the environment.

    Attributes:
        LENGTH: An int representing the length of the game window.
        HEIGHT: An int representing the height of the game window.
        BORDER_WIDTH: An int representing the number of pixels
            in the border that frames the game window.
        _start_game: A boolian representing if the game should start or not.
        _new_game: A boolian representing if the game should restart or
            not.
        _snake: A Snake instance representing the snake to interact
            with.
        _food: An Item instance representing the food to interact
            with.
        _score: An int representing the player's score based on the amount
            of items the snake has eaten.
        _potion: An Item instance representing the potion to interact
            with.
        _speed_boost: An Item instance representing the speed boost to
            interact with.
        _game_over: A boolian representing if the game should end or
            not.

    """
    LENGTH = 600
    HEIGHT = 600
    BORDER_WIDTH = 30
    start_game = False
    new_game = False

    def __init__(self, snake, food, potion, speed_boost):
        """
        Create a board in which the snake, food, and environment
        interact.

        Args:
        _snake: A Snake instance representing the snake to interact
            with.
        _food: An Item instance representing the food to interact
            with.
        _score: An int representing the player's score based on how many
            items the snake has eaten.
        _potion: An Item instance representing the potion to interact
            with.
        _speed_boost: An Item instance representing the speed boost item to
            interact with.
        _game_over: A boolian representinf if the game should end or
            not.

        """
        self._snake = snake
        self._food = food
        self._score = 0
        self._potion = potion
        self._speed_boost = speed_boost
        self.game_over = False

    @property
    def snake(self):
        """
        Return the snake.
        """
        return self._snake

    @property
    def food(self):
        """
        Return the food.
        """
        return self._food

    @property
    def potion(self):
        """
        Return the potion.
        """
        return self._potion

    @property
    def speed_boost(self):
        """
        Return the speed_boost.
        """
        return self._speed_boost

    @property
    def score(self):
        """
        Return the current score.
        """
        return self._score

    def food_eaten(self):
        """
        Returns a boolian based on if the snake has eaten food.

        Returns a boolian based on if the head of the snake has
        overlapped with any food. True means that the snake has
        eaten food, false means that the snake has not eaten.

        Returns:
            A boolian representing if the snake has eaten food.
        """
        return self._snake.coordinates[0] == self._food.item_location

    def potion_eaten(self):
        """
        Returns a boolian based on if the snake has eaten a potion.

        Returns a boolian based on if the head of the snake has
        overlapped with any potion. True means that the snake has
        eaten a potion, false means that the snake has not eaten.

        Returns:
            A boolian representing if the snake has eaten a potion.
        """
        return self._snake.coordinates[0] == self._potion.item_location

    def speed_eaten(self):
        """
        Returns a boolian based on if the snake has eaten a speed boost.

        Returns a boolian based on if the head of the snake has
        overlapped with a speed boost. True means that the snake has
        eaten a speed boost, false means that the snake has not eaten.

        Returns:
            A boolian representing if the snake has eaten a speed boost.
        """
        return self._snake.coordinates[0] == self._speed_boost.item_location

    def snake_collision(self):
        """
        Checks if the snake has collided with itself. True means that it has.

        Returns:
            A boolian representing if the snake had has collided with its body.
        """
        return self._snake.coordinates[0] in self._snake.coordinates[1:]

    def wall_collision(self):
        """
        Checks if the snake has collided with the walls. True means that it has.

        Returns:
            A boolian representing if the snake head has collided with the wall.
        """
        return (self._snake.coordinates[0][0] > self.LENGTH-self.BORDER_WIDTH or
                self._snake.coordinates[0][0] < self.BORDER_WIDTH or
                self._snake.coordinates[0][1] > self.HEIGHT-self.BORDER_WIDTH or
                self._snake.coordinates[0][1] < self.BORDER_WIDTH*2)

    def check_game_over(self):
        """
        Returns a boolian based on if the game should end.

        Returns True if the game should end, returns False if
        the game should continue. Whether the game ends or not
        is based on if the snake has collided with itself or a
        wall.

        Returns:
            A boolian representing if the game should end.
        """
        if self.snake_collision() or self.wall_collision():
            self.game_over = True

    def item_snake_overlap(self):
        """
        Checks if any item spawns on the snake.

        Checks if any item spawns on top of the snake. If it has
        then a new item will spawn.
        """

        # check each chunk of the snake
        for segment in self._snake.coordinates[1:]:
            if segment == self._food.item_location:
                self._food.spawn_new_item()
            elif segment == self._potion.item_location:
                self._potion.spawn_new_item()
            elif segment == self._speed_boost.item_location:
                self._speed_boost.spawn_new_item()

    def add_score(self):
        """
        Adds a point to the score.
        """

        self._score += 1


class Snake:
    """
    A representation of the snake in the snake game.

    Attributes:
        GRID_SIZE: An int representing the number of pixels in each
            body segment.
        _direction: An int representing the direction the snake should
            move.
        _coordinates: A list of lists. Each inner list represents one
            segment of the snake body and containts two ints representing
            the coordinates of the segment.
    """

    # grid size effects the size of the snake chunks and how
    # many blocks the snake moves each time
    GRID_SIZE = 30

    def __init__(self):
        """
        Create a new snake.

        Args:
            _direction: An int representing the direction the snake should
                move.
            _coordinates: A list of lists. Each inner list represents one
                segment of the snake body and containts two ints representing
                the coordinates of the segment.
        """
        self._direction = 0
        # initial coordinates of each chunk of the snake
        self._coordinates = [[10 * self.GRID_SIZE, 10 * self.GRID_SIZE], [
            11 * self.GRID_SIZE, 10 * self.GRID_SIZE], [12 * self.GRID_SIZE, 10 * self.GRID_SIZE]]

    @property
    def coordinates(self):
        """
        Return the coordinates of the snake.
        """
        return self._coordinates

    @property
    def direction(self):
        """
        Return the direction the snake is going.
        """
        return self._direction

    def move(self, direction):
        """
        Moves each snake segment according to the direction.
        """
        # make a copy of the old snake without the last block
        # this will help simulate the snake moving
        new_coordinates = self._coordinates[:-1]

        # update the x and y of the head to new positions
        head_x = new_coordinates[0][0] + direction[0]
        head_y = new_coordinates[0][1] + direction[1]

        head = [head_x, head_y]

        new_coordinates.insert(0, head)
        self._coordinates = new_coordinates

        self._direction = direction

    def add_snake_segment(self, direction):
        """
        Adds a new segment to the end of the snake.
        """
        head_x = self._coordinates[0][0] + direction[0]
        head_y = self._coordinates[0][1] + direction[1]

        head = [head_x, head_y]

        self._coordinates.insert(0, head)

        self._direction = direction


class Item:
    """
    A representation of the items in the snake game.

    Attributes:
        _item_location_x: The x coordinate of the item location.
        _item_location_y: The y coordinate of the item location.
        _item_location: The coordinates of the item location.
    """

    def __init__(self):
        """
        Create a new piece of food.

        Args:
        _item_location_x: The x coordinate of the item location.
        _item_location_y: The y coordinate of the item location.
        _item_location: The coordinates of the item location.
        """
        # Generate random location for food to spawn
        # create random locations while accounting for borders
        # have to do -2 since coordinates are in terms of top left
        self._item_location_x = random.randint(1, 20 - 2) * 30
        self._item_location_y = random.randint(2, 20 - 2) * 30
        self._item_location = [self._item_location_x, self._item_location_y]

    @property
    def item_location(self):
        """
        Return the coordinates of the item.
        """
        return self._item_location

    def spawn_new_item(self):
        """
        Spawns a new location for the item.
        """
        self._item_location_x = random.randint(1, 20 - 2) * 30
        self._item_location_y = random.randint(2, 20 - 2) * 30
        self._item_location = [self._item_location_x, self._item_location_y]
