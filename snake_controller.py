"""
Snake game controller.
"""

import pygame


def player_input(board):
    """
    Obtain input from the user based on which arrow keys are
    pressed.

    Args:
        board: A Board instance representing the snake game to
            send moves to.
    """

    # get the state of all keyboard buttons.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        board.snake.move([-1 * board.snake.grid_size, 0])
    elif keys[pygame.K_RIGHT]:
        board.snake.move([1 * board.snake.grid_size, 0])
    elif keys[pygame.K_UP]:
        board.snake.move([0, -1 * board.snake.grid_size])
    elif keys[pygame.K_DOWN]:
        board.snake.move([0, 1 * board.snake.grid_size])
    else:
        try:
            direction = board.snake.direction
            board.snake.move(direction)
        except TypeError:
            pass
