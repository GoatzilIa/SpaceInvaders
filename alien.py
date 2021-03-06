import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen, row_number):
        """Initialize the alien, and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.row_num = row_number

        # Load the alien image, and set its rect attribute.
        if self.row_num == 0 or self.row_num == 1:
            self.image = pygame.image.load('images/Alien1.png')
        elif self.row_num == 2 or self.row_num == 3:
            self.image = pygame.image.load('images/Alien2.png')
        elif self.row_num == 4 or self.row_num == 5:
            self.image = pygame.image.load('images/Alien3.png')
        elif self.row_num == 6:
            self.image = pygame.image.load('images/AlienMS.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        if self.row_num == 6:
            self.rect.right = 0
            self.rect.y = 90

        # Store the alien's exact position.
        self.x = float(self.rect.x)
        
    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    def update(self):
        """Move the alien right or left."""
        if self.row_num == 6:
            self.x += 2
        else:
            self.x += (self.ai_settings.alien_speed_factor *
                        self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

