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
    x = 250
    y = 250
    coordinates = [[250,250]]
    snake_length = 1

    def __init__(self):
        self.board = Board
        self._direction = None


    def move(self,direction):
        self.x += direction[0]
        self.y += direction[1]
        self.add_coordinates(self.x,self.y)
        self._direction = direction

    def add_coordinates(self, x, y):
        self.coordinates.append([x,y])
        if len(self.coordinates) > self.snake_length:
            self.coordinates = self.coordinates[1:]

    def add_snake_segment(self):
        pass

    def directions(self):
        return self._direction


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
    surface = pygame.Surface((10, 10))
    surface.fill(pygame.Color('blue'))

    def __init__(self, board):
        self.board = board
        self.rect = self.surface.get_rect(center=(self.board.snake.coordinates[0][0], self.board.snake.coordinates[0][1]))
        self.back = self.background.get_rect(center=(self.board.length/2, self.board.height/2))
        self.screen = pygame.display.set_mode((self.board.length, self.board.height))

    def draw(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.screen.blit(self.background,self.back)
        self.screen.blit(self.surface, self.rect)
        pygame.display.update()


class Controller(Board):
    def __init__(self, board):
        self.board = board

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.board.snake.move([-1,0])
        elif keys[pygame.K_RIGHT]:
            self.board.snake.move([1,0])
        elif keys[pygame.K_UP]:
            self.board.snake.move([0,-1])
        elif keys[pygame.K_DOWN]:
            self.board.snake.move([0,1])
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
    clock.tick(60)
    