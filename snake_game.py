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
    potion = Item()
    game = Board(snake, food, potion)
    clock = pygame.time.Clock()
    
    potion = False

    loop_counter = 0
    
    while 1:
        
        View(game).draw_start_menu()
        Controller(game).player_input()
        game.game_over()
        game.item_snake_overlap()
        if game.food_eaten():
            game.add_score()
            game.snake.add_snake_segment(game.snake.directions())
            game.food.spawn_new_item()   
            
        if game.potion_eaten():
             loop_counter = 10
        if loop_counter>0:
            potion = True
        else:
            potion = False
            
        View(game).draw(potion)
                
 
        if game._new_game is True:
            main()
        
        clock.tick(10)
        loop_counter -= 1
    


if __name__ == "__main__":
    main()
