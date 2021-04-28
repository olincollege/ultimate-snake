import pygame
import sys

class Snake:
    x = 250
    y = 250
    coordinates = [(250,250)]
    length = 1
    def __init__(self):
        self._direction = None
    def move(self,direction):
        self.x += direction[0]
        self.y += direction[1]
        self.add_coordinates(self.x,self.y)
        self._direction = direction

    def add_coordinates(self, x, y):
        self.coordinates.append((x,y))
        if len(self.coordinates) > self.length:
            self.coordinates = self.coordinates[1:]
    def add_snake(self):
        pass
    def directions(self):
        return self._direction


class View(Snake):
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Ultimate Snake Game")
    length = 500
    height = 500
    screen = pygame.display.set_mode((length, height))
    background = pygame.Surface((500,500))
    background.fill(pygame.Color('black'))
    surface = pygame.Surface((10, 10))
    surface.fill(pygame.Color('blue'))

    def __init__(self, Snake):
        self.player = Snake
        self.rect = self.surface.get_rect(center=(player.coordinates[0][0], player.coordinates[0][1]))
        self.back = self.background.get_rect(center=(self.length/2, self.height/2))
    def draw(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.screen.blit(self.background,self.back)
        self.screen.blit(self.surface, self.rect)
        pygame.display.update()


class Controller(Snake):
    def __init__(self, Snake):
        self.player = Snake

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move([-1,0])
        elif keys[pygame.K_RIGHT]:
            player.move([1,0])
        elif keys[pygame.K_UP]:
            player.move([0,-1])
        elif keys[pygame.K_DOWN]:
            player.move([0,1])
        else:
            try:
                direction = player.directions()
                player.move(direction)
            except TypeError:
                pass



player = Snake()
clock = pygame.time.Clock()
while 1:
    View(player).draw()
    Controller(player).player_input()
    clock.tick(60)
    