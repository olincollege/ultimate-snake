"""
Snake game view.
"""
import sys
import pygame


class View():
    """
    Pygame based view of a snake game.

    Attributes:
        surface: A 30x30 surface representing a blue block .
        head_up: A png image representing the head of the snake in
            an upwards orientation.
        head_down: A png image representing the head of the snake in
            a downwards orientation
        head_right: A png image representing the head of the snake facing
            right.
        head_left: A png image representing the head of the snake facing
            left.
        _board: A Board instance representing the snake game to
            display.
        _screen: A display surface representing the window to display
            the rest of the game components on.
        _head_image: A png image representing the head of the snake.
    """

    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Ultimate Snake Game")
    surface = pygame.Surface((30, 30))
    surface.fill(pygame.Color('blue'))
    head_up = pygame.image.load('images/snake_up.png')
    head_down = pygame.image.load('images/snake_down.png')
    head_right = pygame.image.load('images/snake_right.png')
    head_left = pygame.image.load('images/snake_left.png')

    def __init__(self, board):
        """
        Create a new view of a snake game.

        Args:
            _board: A Board instance representing the snake game to
                display.
            _screen: A display surface representing the window to display
                the rest of the game components on.
            _head_image: A png image representing the head of the snake.
        """

        self._board = board
        self._screen = pygame.display.set_mode((self._board.length + \
            self._board.border_width,self._board.height+self._board.border_width))
        self._head_image = self.head_left

    def get_head_image(self):
        """
        Gets the correct image for the snake head.

        Gets the correct orientation of the snake head based on
        the snake's head coordinates in relation to its body.
        """
        head_orientation_x = self._board.snake.coordinates[1][0] - \
            self._board.snake.coordinates[0][0]
        head_orientation_y = self._board.snake.coordinates[1][1] - \
            self._board.snake.coordinates[0][1]
        if head_orientation_x == 30 and head_orientation_y == 0:
            self._head_image = self.head_left
        elif head_orientation_x == -30 and head_orientation_y == 0:
            self._head_image = self.head_right
        elif head_orientation_x == 0 and head_orientation_y == 30:
            self._head_image = self.head_up
        elif head_orientation_x == 0 and head_orientation_y == -30:
            self._head_image = self.head_down

    def draw(self):
        """
        Display a representation of the snake game.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self._screen.fill('white')

       # get head image and blit
        self.get_head_image()
        head_rect = self._head_image.get_rect()
        head_rect.x = self._board.snake.coordinates[0][0]
        head_rect.y = self._board.snake.coordinates[0][1]
        self._screen.blit(self._head_image, head_rect)

        # get surface for each snake body chunk, and blit each one
        for segment in self._board.snake.coordinates[1:]:
            segment_rect = self.surface.get_rect()
            segment_rect.x = segment[0]
            segment_rect.y = segment[1]
            self._screen.blit(self.surface, segment_rect)

        # blit an image of an apple for the food
        apple_image = pygame.image.load('images/apple.png').convert_alpha()
        apple_rect = apple_image.get_rect()
        apple_rect.x = self._board.food.food_location[0]
        apple_rect.y = self._board.food.food_location[1]
        self._screen.blit(apple_image, apple_rect)

        # create frame around the game window
        # top line
        pygame.draw.rect(self._screen, (169, 169, 169), [
                         0, 0, self._board.length, self._board.border_width*2])
        # bottom line
        pygame.draw.rect(self._screen, (169, 169, 169), [
                         0, self._board.height, self._board.length, self._board.border_width])
        # left line
        pygame.draw.rect(self._screen, (169, 169, 169), [
                         0, 0, self._board.border_width, self._board.height])
        # right line
        pygame.draw.rect(self._screen, (169, 169, 169), [
                         self._board.length, 0, self._board.border_width, self._board.length+ \
                            self._board.border_width])

        # display score
        score = str(self._board.score)
        font = pygame.font.SysFont(None, 60)
        score_text = font.render(f'Score: {score}', True, 'black')
        self._screen.blit(score_text, (30, 10))

        pygame.display.update()