"""
Main program to set up and run a snake game.
"""
import sys
import pygame

from snake_model import Snake, Food, Board
from snake_view import View
from snake_controller import Controller

def main():
    """
    Play a game of snake.
    """

    # set up the board
    game = Board(Snake(), Food())
    clock = pygame.time.Clock()
    while 1:
        View(game).draw()
        Controller(game).player_input()
        if game.game_over():
            print('Game Over!')
            pygame.quit()
            sys.exit()

        game.food_snake_overlap()
        if game.food_eaten():
            game.add_score()
            game.snake.add_snake_segment(game.snake.directions())
            game.food.spawn_new_food()
        clock.tick(10)


if __name__ == "__main__":
    main()
