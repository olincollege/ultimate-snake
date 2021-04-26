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


class Snake():
    def __init__(self):
        # Call the parent class (Sprite) constructor
                        
        self.body_pos = [[10,10],[11,10],[12,10]]
        self.movex = 0
        self.movey = 0
        
    def change_direction(self,x,y):
  
        self.movex = x
        self.movey = y
     
    def create_segment(self):
        segment_surface = pygame.Surface((grid_size,grid_size))
        segment_surface.fill(green)
        # Fetch the rectangle object that has the dimensions of the image
        segment_rect = segment_surface.get_rect()
        return segment_rect
        
     
    def update(self):
        #get segments for new body
        
        #copy old snake without tail (to make moving forward motion)
        new_body_pos = self.body_pos[:-1]
       
        #creates new head 
        head_x = new_body_pos[0][0] + self.movex
        head_y = new_body_pos[0][1] + self.movey
                
        head = [head_x, head_y]
        
        new_body_pos.insert(0,head)
        self.body_pos = new_body_pos

        
    def draw(self):
        self.update()
        for segment in self.body_pos:
            #get rect for each segment
            new_segment = self.create_segment()
            #place rect based on position
            new_segment.x = segment[0] * grid_size
            new_segment.y = segment[1] * grid_size
            pygame.draw.rect(screen, green, new_segment)
        

        
class Food(pygame.sprite.Sprite):
    def __init__(self):
        
        # Generate random location for food to spawn
        food_location_x = random.randint(0,grid_number-1)*grid_size
        food_location_y = random.randint(0,grid_number-1)*grid_size
        
        #Create an image of the food
        self.image = pygame.Surface((grid_size,grid_size))
        self.image.fill(red)
        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()
        self.rect.x = food_location_x
        self.rect.y = food_location_y
        
    def draw(self):
        pygame.draw.rect(screen, red, self.rect)

        
#initialize pygame and create window
pygame.init()
#for sound
pygame.mixer.init()

screen = pygame.display.set_mode((width, height))


pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

snake = Snake()
food = Food()

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
            snake.change_direction(-1,0)

            # if left arrow key is pressed
        if keys[pygame.K_RIGHT]:
            # increment in x co-ordinate
            snake.change_direction(1,0)

            # if left arrow key is pressed
        if keys[pygame.K_UP]:
            # decrement in y co-ordinate
            snake.change_direction(0,-1)

            # if left arrow key is pressed
        if keys[pygame.K_DOWN]:
            # increment in y co-ordinate 
            snake.change_direction(0,1)


    
    #draw/render
    screen.fill(black)
    snake.draw()
    food.draw()
    
   
    #after drawing everything update the display
    pygame.display.update()
    
pygame.quit()