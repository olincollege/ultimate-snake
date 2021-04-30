import pygame
import sys
import random


class Board:
    def __init__(self, snake, food):
        self.snake = snake
        self.food = food
        self.length = 600
        self.height = 600
        self.score = 0
        self.grid_size = 30

    def food_eaten(self):
        #print(f'Snake Location: {self.snake.coordinates[0]}')
        #print(f'Food Location: {self.food.food_location}')
        if self.snake.coordinates[0] == self.food.food_location:
            #print('Eaten!')
            return True



class Snake:
    grid_size = 30
    x = 0
    y = 0
    #####A lot of the numbers here are based on the snake moving 30 each time.
    coordinates = [[10 * grid_size, 10 * grid_size], [11 * grid_size, 10 * grid_size], [12 * grid_size, 10 * grid_size]]
    snake_length = 1

    def __init__(self):
        self._direction = None
        self.speed = 3

    def move(self, direction):
        new_coordinates = self.coordinates[:-1]

        head_x = new_coordinates[0][0] + direction[0]
        head_y = new_coordinates[0][1] + direction[1]

        head = [head_x, head_y]

        new_coordinates.insert(0, head)
        self.coordinates = new_coordinates

        self._direction = direction

    def add_snake_segment(self, direction):
        head_x = self.coordinates[0][0] + direction[0]
        head_y = self.coordinates[0][1] + direction[1]

        head = [head_x, head_y]

        self.coordinates.insert(0, head)

        self._direction = direction

    def directions(self):
        return self._direction

    def speed_multiplier(self):
        pass


class Food:
    def __init__(self):
        # Generate random location for food to spawn
        # have to do -1 since the rects are drawn based on top left
        self.food_location_x = random.randint(0, 20 - 1) * 30
        self.food_location_y = random.randint(0, 20 - 1) * 30
        self.food_location = [self.food_location_x, self.food_location_y]

    def spawn_new_food(self):
        self.food_location_x = random.randint(0, 20 - 1) * 30
        self.food_location_y = random.randint(0, 20 - 1) * 30
        self.food_location = [self.food_location_x, self.food_location_y]


class View(Board):
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Ultimate Snake Game")
    background = pygame.Surface((600, 600))
    background.fill(pygame.Color('black'))
    surface = pygame.Surface((30, 30))
    surface.fill(pygame.Color('blue'))

    def __init__(self, board):
        self.board = board
        self.back = self.background.get_rect(topleft=(self.board.length / 2, self.board.height / 2))
        self.screen = pygame.display.set_mode((self.board.length, self.board.height))

    def draw(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.screen.blit(self.background, self.back)

        for segment in self.board.snake.coordinates:
            segment_rect = self.surface.get_rect()
            segment_rect.x = segment[0]
            segment_rect.y = segment[1]
            self.screen.blit(self.surface, segment_rect)

        apple_rect = self.surface.get_rect()
        apple_rect.x = self.board.food.food_location[0]
        apple_rect.y = self.board.food.food_location[1]
        self.screen.blit(self.surface, apple_rect)
        pygame.display.update()


class Controller(Board):
    def __init__(self, board):
        self.board = board

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.board.snake.move([-1 * self.board.grid_size, 0])
        elif keys[pygame.K_RIGHT]:
            self.board.snake.move([1 * self.board.grid_size, 0])
        elif keys[pygame.K_UP]:
            self.board.snake.move([0, -1 * self.board.grid_size])
        elif keys[pygame.K_DOWN]:
            self.board.snake.move([0, 1 * self.board.grid_size])
        else:
            try:
                direction = self.board.snake.directions()
                self.board.snake.move(direction)
            except TypeError:
                pass


game = Board(Snake(), Food())
clock = pygame.time.Clock()
while 1:
    View(game).draw()
    Controller(game).player_input()
    if game.food_eaten():
        game.snake.add_snake_segment(game.snake.directions())
        game.food.spawn_new_food()
    clock.tick(10)
    