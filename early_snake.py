import pygame
import sys

class Board:
    def __init__(self,snake,food):
        self.snake = snake
        self.food = food
        self.length = 500
        self.height = 500
        self.score = 0


class Snake(Board):
    x = 0
    y = 0
    coordinates = [[250, 250], [280,250],[310,250]]
    snake_length = 1

    def __init__(self):
        self.board = Board
        self._direction = None
        self.speed = 3


    def move(self,direction):
        new_coordinates = self.coordinates[:-1]
        
        head_x = new_coordinates[0][0] + direction[0]
        head_y = new_coordinates[0][1] + direction[1]
        
        head = [head_x, head_y]
        
        new_coordinates.insert(0,head)
        self.coordinates = new_coordinates
        
        self._direction = direction

    def add_snake_segment(self):
        pass

    def directions(self):
        return self._direction

    def speed_multiplier(self):
        pass


class Food:
    def __init__(self):
        self.board = Board

    def draw(self):
        pass


class View(Board):
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Ultimate Snake Game")
    background = pygame.Surface((500, 500))
    background.fill(pygame.Color('black'))
    surface = pygame.Surface((30, 30))
    surface.fill(pygame.Color('blue'))

    def __init__(self, board):
        self.board = board
        self.back = self.background.get_rect(center=(self.board.length/2, self.board.height/2))
        self.screen = pygame.display.set_mode((self.board.length, self.board.height))

    def draw(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.screen.blit(self.background,self.back)
        
        for segment in self.board.snake.coordinates:
            
            rect = self.surface.get_rect(center=(segment[0], segment[1]))
            rect.x = segment[0]
            rect.y = segment[1]       
            self.screen.blit(self.surface, rect)
        pygame.display.update()
        
   


class Controller(Board):
    def __init__(self, board):
        self.board = board

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.board.snake.move([-1*30,0])
        elif keys[pygame.K_RIGHT]:
            self.board.snake.move([1*30,0])
        elif keys[pygame.K_UP]:
            self.board.snake.move([0,-1*30])
        elif keys[pygame.K_DOWN]:
            self.board.snake.move([0,1*30])
        else:
            try:
                direction = self.board.snake.directions()
                self.board.snake.move(direction)
            except TypeError:
                pass



game = Board(Snake(),Food())
clock = pygame.time.Clock()
while 1:
    View(game).draw()
    Controller(game).player_input()
    clock.tick(10)
    