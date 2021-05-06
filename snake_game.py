"""
Main program to set up and run a snake game.
"""
import sys
import pygame

from snake_model import Snake, Item, Board
from snake_view import View
from snake_controller import Controller

def main():
    """
    Play a game of snake.
    """

    # set up the board
    snake = Snake()
    food = Item()
    game = Board(snake, food)
    clock = pygame.time.Clock()

    i = 1
    while 1:
        View(game).draw_start_menu()
        View(game).draw()
        Controller(game).player_input()
        game.game_over()
        game.food_snake_overlap()
        if game.food_eaten():
            game.add_score()
            game.snake.add_snake_segment(game.snake.directions())
            game.food.spawn_new_item()
        if game._new_game is True:
            main()
        clock.tick(10)
    


if __name__ == "__main__":
    main()
