"""
Main program to set up and run a snake game.
"""
import pygame

from snake_model import Snake, Item, Board
from snake_view import View
from snake_view import play_eaten_sound
from snake_controller import player_input

def main():
    """
    Play a game of snake.
    """

    # set up the board
    snake = Snake()
    food = Item()
    potion = Item()
    speed_boost = Item()
    game = Board(snake, food, potion, speed_boost)
    clock = pygame.time.Clock()

    ate_potion = False

    #initialize loop counters which will help us
    #make the effects of special items last only a certain
    #amount of time
    loop_counter1= 0
    loop_counter2= 0
    #how fast the game is running
    fps = 10

    while 1:

        View(game).draw_start_menu()
        player_input(game)
        game.check_game_over()
        game.item_snake_overlap()
        if game.food_eaten():
            play_eaten_sound()
            game.add_score()
            game.snake.add_snake_segment(game.snake.direction)
            game.food.spawn_new_item()

        if game.potion_eaten():
            #by setting the loop counter to 10, it makes sure
            #that the potion lasts for only 10 loops
            loop_counter1 = 10
            game.add_score()
            game.snake.add_snake_segment(game.snake.direction)
        ate_potion = bool(loop_counter1 > 0)

        View(game).draw(ate_potion)

        if game.speed_eaten():
            game.add_score()
            game.snake.add_snake_segment(game.snake.direction)
            #by setting the loop counter to 10, it makes sure
            #that the potion lasts for only 10 loops
            loop_counter2 = 10
        if loop_counter2>0:
            fps = 20
        else:
            fps = 10


        if game.new_game is True:
            main()

        clock.tick(fps)
        loop_counter1 -= 1
        loop_counter2 -= 1



if __name__ == "__main__":
    main()
