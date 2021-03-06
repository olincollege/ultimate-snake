"""
Snake game view.
"""
import sys
import pygame
from snake_controller import get_mouse_position


def play_eaten_sound():
    """
    Plays a crunch sound.
    """
    food_eaten_sound = pygame.mixer.Sound('sounds/snake_eat_sound.wav')
    pygame.mixer.Sound.play(food_eaten_sound)


def play_click_sound():
    """
    Plays a click sound
    """
    click_sound = pygame.mixer.Sound('sounds/click_sound.wav')
    pygame.mixer.Sound.play(click_sound)


class View():
    """
    Pygame based view of a snake game.

    Attributes:
        _START_MENU: A png image of the start menu.
        _END_MENU: A png image of the end menu.
        _board: A Board instance representing the snake game to
            display.
        _screen: A display surface representing the window to display
            the rest of the game components on.
        _head_image: A png image representing the head of the snake.
        _start_menu_surface: A surface representing the start menu.
        _end_menu_surface: A surface representing the end menu.
        _start_menu_rect: A rect representing the start menu.
        _end_menu_rect: A rect representing the end menu.
    """
    _START_MENU = pygame.image.load('images/start_menu.png')
    _END_MENU = pygame.image.load('images/end_menu.png')

    def __init__(self, board):
        """
        Create a new view of a snake game.

        Args:
            _board: A Board instance representing the snake game to
                display.
            _screen: A display surface representing the window to display
                the rest of the game components on.
            _head_image: A png image representing the head of the snake.
            _start_menu_surface: A surface representing the start menu.
            _end_menu_surface: A surface representing the end menu.
            _start_menu_rect: A rect representing the start menu.
            _end_menu_rect: A rect representing the end menu.
        """

        self._board = board
        self._screen = pygame.display.set_mode((self._board.LENGTH + \
            self._board.BORDER_WIDTH,self._board.HEIGHT+self._board.BORDER_WIDTH))
        self._head_image = pygame.image.load('images/snake_left.png')
        self._start_menu_surface = pygame.display.set_mode((self._board.LENGTH + \
            self._board.BORDER_WIDTH,self._board.HEIGHT+self._board.BORDER_WIDTH))
        self._end_menu_surface = pygame.display.set_mode((self._board.LENGTH + \
            self._board.BORDER_WIDTH,self._board.HEIGHT+self._board.BORDER_WIDTH))
        self._start_menu_rect = self._START_MENU.get_rect(center = (300,300))
        self._end_menu_rect = self._END_MENU.get_rect(center = (300,300))

    def get_head_image(self):
        """
        Gets the correct image for the snake head.

        Gets the correct orientation of the snake head based on
        the snake's head position in relation to its body.
        """

        head_up = pygame.image.load('images/snake_up.png')
        head_down = pygame.image.load('images/snake_down.png')
        head_right = pygame.image.load('images/snake_right.png')
        head_left = pygame.image.load('images/snake_left.png')

        # figures out what image of the head to use based on
        # the relative position of the body and head
        head_orientation_x = self._board.snake.coordinates[1][0] - \
            self._board.snake.coordinates[0][0]
        head_orientation_y = self._board.snake.coordinates[1][1] - \
            self._board.snake.coordinates[0][1]
        if head_orientation_x == self._board.snake.GRID_SIZE and head_orientation_y == 0:
            self._head_image = head_left
        elif head_orientation_x == -self._board.snake.GRID_SIZE and head_orientation_y == 0:
            self._head_image = head_right
        elif head_orientation_x == 0 and head_orientation_y == self._board.snake.GRID_SIZE:
            self._head_image = head_up
        elif head_orientation_x == 0 and head_orientation_y == -self._board.snake.GRID_SIZE:
            self._head_image = head_down

    def draw(self, ate_potion):
        """
        Display a representation of the snake game.
        """

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Ultimate Snake Game")

        icon = pygame.image.load('images/snake_icon.png')
        pygame.display.set_icon(icon)

        self._screen.fill('white')

        self.draw_apple()
        self.draw_border()
        self.draw_potion()
        self.draw_speed()

        if ate_potion:
            self.draw_invisible_snake()
        elif not ate_potion:
            self.draw_snake()
        self.draw_menus()
        self.draw_score()

        pygame.display.update()

    def draw_apple(self):
        """
        Displays the apple item.
        """
        # blit an image of an apple for the food
        apple_image = pygame.image.load('images/apple.png').convert_alpha()
        apple_rect = apple_image.get_rect()
        apple_rect.x = self._board.food.item_location[0]
        apple_rect.y = self._board.food.item_location[1]
        self._screen.blit(apple_image, apple_rect)

    def draw_potion(self):
        """
        Displays the potion item.
        """
        # blit an image of the potion for the invisibility potion
        potion_image = pygame.image.load('images/potion.png').convert_alpha()
        potion_rect = potion_image.get_rect()
        potion_rect.x = self._board.potion.item_location[0]
        potion_rect.y = self._board.potion.item_location[1]
        self._screen.blit(potion_image, potion_rect)

    def draw_speed(self):
        """
        Draws the speed boost item.
        """
        # blit an image of the speed boost for the speed boost item
        lightning_image = pygame.image.load(
            'images/lightning.png').convert_alpha()
        lightning_rect = lightning_image.get_rect()
        lightning_rect.x = self._board.speed_boost.item_location[0]
        lightning_rect.y = self._board.speed_boost.item_location[1]
        self._screen.blit(lightning_image, lightning_rect)

    def draw_snake(self):
        """
        Displays the snake head and body.
        """
       # get head image and blit
        self.get_head_image()
        head_rect = self._head_image.get_rect()
        head_rect.x = self._board.snake.coordinates[0][0]
        head_rect.y = self._board.snake.coordinates[0][1]
        self._screen.blit(self._head_image, head_rect)

        # get surface for each snake body chunk, and blit each one
        for segment in self._board.snake.coordinates[1:]:
            surface = pygame.Surface((30, 30))
            surface.fill(pygame.Color('blue'))
            segment_rect = surface.get_rect()
            segment_rect.x = segment[0]
            segment_rect.y = segment[1]
            self._screen.blit(surface, segment_rect)

    def draw_invisible_snake(self):
        """
        Displays invisible snake.

        Draws the invisible snake by not displaying anything.
        """

    def draw_border(self):
        """
        Displays the border frame around the screen.
        """
        # create frame around the game window
        # top line
        pygame.draw.rect(self._screen, (169, 169, 169), [
                         0, 0, self._board.LENGTH, self._board.BORDER_WIDTH*2])
        # bottom line
        pygame.draw.rect(self._screen, (169, 169, 169), [
                         0, self._board.HEIGHT, self._board.LENGTH, self._board.BORDER_WIDTH])
        # left line
        pygame.draw.rect(self._screen, (169, 169, 169), [
                         0, 0, self._board.BORDER_WIDTH, self._board.HEIGHT])
        # right line
        pygame.draw.rect(self._screen, (169, 169, 169), [
                         self._board.LENGTH, 0, self._board.BORDER_WIDTH, self._board.LENGTH +
                         self._board.BORDER_WIDTH])

    def draw_score(self):
        """
        Displays the score.
        """
        # display score
        score = str(self._board.score)
        font = pygame.font.SysFont(None, 60)
        score_text = font.render(f'Score: {score}', True, 'black')
        self._screen.blit(score_text, (30, 10))
        pygame.display.update()

    def draw_start_menu(self):
        """
        Displays the start menu.
        """
        self._start_menu_surface.blit(self._START_MENU, self._start_menu_rect)

    def draw_game_over(self):
        """
        Displays the game over menu.
        """
        self._end_menu_surface.blit(self._END_MENU, self._end_menu_rect)

    def draw_menus(self):
        """
        Draws each menu as needed.
        """
        # Draws starts screen.
        while self._board.start_game is False:
            self.draw_start_menu()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Will exit start screen if mouse cursor clicks on start button.
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self._start_menu_rect.collidepoint(get_mouse_position()):
                        play_click_sound()
                        self._board.start_game = True
        # Draws game over screen.
        while self._board.game_over is True:
            self._screen.fill('white')
            self.draw_game_over()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Will trigger new game if mouse cursor clicks on restart button.
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self._end_menu_rect.collidepoint(get_mouse_position()):
                        play_click_sound()
                        self._board.new_game = True
            break
