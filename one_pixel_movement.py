import pygame
import random

#define max framerate and screen parameters
grid_size = 40
grid_number = 21
width = grid_size*grid_number
height = grid_size*grid_number
FPS = 10

#define colors
green = (0, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        
        #Create an image of the snake
        self.image = pygame.Surface((grid_size,grid_size))
        self.image.fill(green)
        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()
        self.rect.center = (width/2, height/2)
        
        #initialize direction
        self.movex = 0
        self.movey = 0
        
    def direction(self,x,y):
        
        self.movex = x
        self.movey = y
        
    def update(self):
        self.rect.x += self.movex
        self.rect.y += self.movey
        
        
        
class Food(pygame.sprite.Sprite):
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        
        # Generate random location for food to spawn
        food_location_x = random.randint(0,grid_number-1)*grid_size
        food_location_y = random.randint(0,grid_number-1)*grid_size
        
        #Create an image of the food
        self.image = pygame.Surface((grid_size,grid_size))
        self.image.fill(red)
        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()
        self.rect.center = (food_location_x,food_location_y)

        
#initialize pygame and create window
pygame.init()
#for sound
pygame.mixer.init()

screen = pygame.display.set_mode((width, height))


pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

snake = Snake()
snake.rect.x = height/2  # go to x
snake.rect.y = width/2  # go to y

food = Food()
all_sprites.add(snake)
all_sprites.add(food)

#Game Loop
running = True
while running:
    #keep loop running at the right speed
    clock.tick(FPS)
    #process inputs (events)
    for event in pygame.event.get():
    #check for closing window
        if event.type == pygame.QUIT:
            running = False
        
        # stores keys pressed  
        keys = pygame.key.get_pressed()

        # if left arrow key is pressed 
        if keys[pygame.K_LEFT]:
            # decrement in x co-ordinate
            snake.direction(-grid_size,0)

            # if left arrow key is pressed
        if keys[pygame.K_RIGHT]:
            # increment in x co-ordinate
            snake.direction(grid_size,0)

            # if left arrow key is pressed
        if keys[pygame.K_UP]:
            # decrement in y co-ordinate
            snake.direction(0,-grid_size)

            # if left arrow key is pressed
        if keys[pygame.K_DOWN]:
            # increment in y co-ordinate 
            snake.direction(0,grid_size)

    #update
    all_sprites.update()
    
    #draw/render
    screen.fill(black)
    all_sprites.draw(screen)
   
    #after drawing everything update the display
    pygame.display.update()
    
pygame.quit()