"""
Snake game implementation.
"""

import random


class Board:
    """
    Snake game board with basic play functionality that combines
    interactions between the snake, food, and the environment.

    Attributes:
        length: An int representing the length of the game window.
        height: An int representing the height of the game window.
        border_width: An int representing the number of pixels
            in the border that frames the game window.
        _snake: A Snake instance representing the snake to interact
            with.
        _food: A Food instance representing the food to interact
            with.
        _score: An int representing the player's score based on food
            the snake has eaten.
    """
    length = 600
    height = 600
    border_width = 30

    def __init__(self, snake, food):
        """
        Create a board in which the snake, food, and environment
        interact.

        Args:
            _snake: A Snake instance representing the snake to interact
                with.
            _food: A Food instance representing the food to interact
                with.
            _score: An int representing the player's score based on food
                the snake has eaten.
        """
        self._snake = snake
        self._food = food
        self._score = 0

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
        return self._snake.coordinates[0] == self._food.food_location

    def game_over(self):
        """
        Returns a boolian based on if the game should end.

        Returns True if the game should end, returns False if
        the game should continue. Whether the game ends or not
        is based on if the snake has collided with itself or a
        wall.

        Returns:
            A boolian representing if the game should end.
        """
        return self.snake_collision() or self.wall_collision()

    def food_snake_overlap(self):
        """
        Checks if the food spawns on the snake.

        Checks if the food spawns on top of the snake. If it has
        then new food will spawn.
        """
        # checks if food spawns on the snake
        for segment in self._snake.coordinates[1:]:
            if segment == self._food.food_location:
                self._food.spawn_new_food()

    def add_score(self):
        """
        Adds a point to the score.
        """

        self._score += 1

    def snake_collision(self):
        """
        Checks if the snake has collided with itself. True means that it has.

        Returns:
            A boolian representing if the snake has collided with itself.
        """
        return self._snake.coordinates[0] in self._snake.coordinates[1:]

    def wall_collision(self):
        """
        Checks if the snake has collided with the walls. True means that it has.

        Returns:
            A boolian representing if the snake has collided with the wall.
        """
        return (self._snake.coordinates[0][0] > self.length-self.border_width or
            self._snake.coordinates[0][0] < self.border_width or
            self._snake.coordinates[0][1] > self.height-self.border_width or
            self._snake.coordinates[0][1] < self.border_width*2)


class Snake:
    """
    A representation of the snake in the snake game.

    Attributes:
        grid_size: An int representing the number of pixels in each
            body segment.
        _direction: An int representing the direction the snake should
            move.
        _speed: An int representing how fast the snake is moving.
        _coordinates: A list of lists. Each inside list represents one
            segment of the snake body and containts two ints representing
            the coordinates of the segment.
    """
    grid_size = 30

    def __init__(self):
        """
        Create a new snake.

        Args:
            _direction: An int representing the direction the snake should
                move.
            _speed: An int representing how fast the snake is moving.
            _coordinates: A list of lists. Each inside list represents one
                segment of the snake body and containts two ints representing
                the coordinates of the segment.
        """
        self._direction = 0
        self._speed = 3
        self._coordinates = [[10 * self.grid_size, 10 * self.grid_size], [
            11 * self.grid_size, 10 * self.grid_size], [12 * self.grid_size, 10 * self.grid_size]]

    @property
    def coordinates(self):
        """
        Return the coordinates of the snake.
        """
        return self._coordinates

    def move(self, direction):
        """
        Moves each snake segment according to the direction.
        """
        new_coordinates = self._coordinates[:-1]

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

    def directions(self):
        """
        Return the direction the snake is going.
        """
        return self._direction

    def speed_multiplier(self):
        """
        Increases the speed of the snake.
        """


class Food:
    """
    A representation of the food in the snake game.

    Attributes:
        _food_location_x: The x coordinate of the food location.
        _food_location_y: The y coordinate of the food location.
        _food_location: The coordinates of the food location.
    """

    def __init__(self):
        """
        Create a new piece of food.

        Args:
            _food_location_x: The x coordinate of the food location.
            _food_location_y: The y coordinate of the food location.
            _food_location: The coordinates of the food location.
        """
        # Generate random location for food to spawn
        # create random locations while accounting for borders
        # have to do -2 since coordinates are in terms of top left
        self._food_location_x = random.randint(1, 20 - 2) * 30
        self._food_location_y = random.randint(2, 20 - 2) * 30
        self._food_location = [self._food_location_x, self._food_location_y]

    @property
    def food_location(self):
        """
        Return the coordinates of the food.
        """
        return self._food_location

    def spawn_new_food(self):
        """
        Spawns a new location for the food.
        """
        self._food_location_x = random.randint(1, 20 - 2) * 30
        self._food_location_y = random.randint(2, 20 - 2) * 30
        self._food_location = [self._food_location_x, self._food_location_y]
