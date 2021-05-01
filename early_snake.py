import pygame
import sys
import random


class Board:
    length = 600
    height = 600
    grid_size = 30
    border_width = 30
        
    def __init__(self, snake, food):
        self.snake = snake
        self.food = food
        self.score = 0


    def food_eaten(self):    
        if self.snake.coordinates[0] == self.food.food_location:
            return True
        
    def game_over(self):
        if self.snake_collision() or self.wall_collision():
            print('Game Over!')
            pygame.quit()
            sys.exit()
    
    def food_snake_overlap(self):
        #checks if food spawns on food
        for segment in self.snake.coordinates[1:]:
            if segment == self.food.food_location:
                self.food.spawn_new_food()
                
    def add_score(self):
        self.score += 1

    def snake_collision(self):
        if self.snake.coordinates[0] in self.snake.coordinates[1:]:
            return True
        return False

    def wall_collision(self):
        if self.snake.coordinates[0][0] > self.length-self.border_width or self.snake.coordinates[0][0] < self.border_width or self.snake.coordinates[0][1] > self.height-self.border_width or self.snake.coordinates[0][1] < self.border_width*2:
            return True
        return False


class Snake:
    grid_size = 30

    def __init__(self):
        self._direction = None
        self.speed = 3
        self.coordinates = [[10 * self.grid_size, 10 * self.grid_size], [11 * self.grid_size, 10 * self.grid_size], [12 * self.grid_size, 10 * self.grid_size]]



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
        # create random locations while accounting for borders
        #have to do -2 since coordinates are in terms of top left
        self.food_location_x = random.randint(1, 20 - 2) * 30
        self.food_location_y = random.randint(2, 20 - 2) * 30
        self.food_location = [self.food_location_x, self.food_location_y]

    def spawn_new_food(self):
        self.food_location_x = random.randint(1, 20 - 2) * 30
        self.food_location_y = random.randint(2, 20 - 2) * 30
        self.food_location = [self.food_location_x, self.food_location_y]


class View(Board):
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Ultimate Snake Game")
    surface = pygame.Surface((30, 30))
    surface.fill(pygame.Color('blue'))

    def __init__(self, board):
        self.board = board
        self.screen = pygame.display.set_mode((self.board.length + self.board.border_width, self.board.height+self.board.border_width))       
        self.head_up = pygame.image.load('images/snake_up.png').convert_alpha()
        self.head_down = pygame.image.load('images/snake_down.png').convert_alpha()
        self.head_right = pygame.image.load('images/snake_right.png').convert_alpha()
        self.head_left = pygame.image.load('images/snake_left.png').convert_alpha()
        self.head_image = self.head_left
        
    def get_head_image(self):
        head_orientation_x = self.board.snake.coordinates[1][0] - self.board.snake.coordinates[0][0]
        head_orientation_y = self.board.snake.coordinates[1][1] - self.board.snake.coordinates[0][1]
        if head_orientation_x == 30 and head_orientation_y == 0:
            self.head_image = self.head_left
        elif head_orientation_x == -30 and head_orientation_y == 0:
            self.head_image = self.head_right
        elif head_orientation_x == 0 and head_orientation_y == 30:
            self.head_image = self.head_up
        elif head_orientation_x == 0 and head_orientation_y == -30:
            self.head_image = self.head_down
        
    def draw(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.screen.fill('white')
            
       #get head image and blit
        self.get_head_image()
        head_rect = self.head_image.get_rect()
        head_rect.x = self.board.snake.coordinates[0][0]
        head_rect.y = self.board.snake.coordinates[0][1]
        self.screen.blit(self.head_image,head_rect)
        
        for segment in self.board.snake.coordinates[1:]:
            segment_rect = self.surface.get_rect()
            segment_rect.x = segment[0]
            segment_rect.y = segment[1]
            self.screen.blit(self.surface, segment_rect)
        
        apple_image= pygame.image.load('images/apple.png').convert_alpha()
        apple_rect = apple_image.get_rect()
        apple_rect.x = self.board.food.food_location[0]
        apple_rect.y = self.board.food.food_location[1]
        self.screen.blit(apple_image, apple_rect)
        
        #create frame
        # top line
        pygame.draw.rect(self.screen, (169,169,169), [0,0,self.board.length,self.board.border_width*2])
        # bottom line
        pygame.draw.rect(self.screen, (169,169,169), [0,self.board.height,self.board.length,self.board.border_width])
        # left line
        pygame.draw.rect(self.screen, (169,169,169), [0,0,self.board.border_width, self.board.height])
        # right line
        pygame.draw.rect(self.screen, (169,169,169), [self.board.length,0,self.board.border_width, self.board.length+self.board.border_width])
        
        # display score  
        score = str(self.board.score)
        font = pygame.font.SysFont(None, 60)
        score_text = font.render(f'Score: {score}', True, 'black')
        self.screen.blit(score_text, (30, 10))
        

        
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
    game.game_over()
    game.food_snake_overlap()
    if game.food_eaten():
        game.add_score()
        game.snake.add_snake_segment(game.snake.directions())
        game.food.spawn_new_food() 
    clock.tick(10)