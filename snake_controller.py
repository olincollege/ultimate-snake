"""
Snake game controller.
"""

import pygame


class Controller():
    """
    Pygame-based controller for snake game that takes user
    input from the arrow keys that represent where the snake
    should move.

    Attributes:
        _board: A Board instance representing the snake game to
            send moves to.
    """

    def __init__(self, board):
        """
        Create a new controller for a snake game.

        Args:
            _board: A Board instance representing the snake game to
                send moves to.
        """
        self._board = board

    def player_input(self):
        """
        Obtain input from the user based on which arrow keys are
        pressed.
        """

        # get the state of all keyboard buttons.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self._board.snake.move([-1 * self._board.snake.grid_size, 0])
        elif keys[pygame.K_RIGHT]:
            self._board.snake.move([1 * self._board.snake.grid_size, 0])
        elif keys[pygame.K_UP]:
            self._board.snake.move([0, -1 * self._board.snake.grid_size])
        elif keys[pygame.K_DOWN]:
            self._board.snake.move([0, 1 * self._board.snake.grid_size])
        else:
            try:
                direction = self._board.snake.direction
                self._board.snake.move(direction)
            except TypeError:
                pass
