import pygame
from settings import Settings
from pygame.time import Clock
from button import Button
import game_functions as gf

def Start_Screen(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, clock):
    """creates a start screen"""
    intro = True

    while intro:
        """shows the start screen until the player clicks the play button"""
        screen.fill((20, 20, 20))
        largeText = pygame.font.Font('freesansbold.ttf', 80)
        mediumText = pygame.font.Font('freesansbold.ttf', 60)
        smallText =  pygame.font.Font('freesansbold.ttf', 35)
        smallerText = pygame.font.Font('freesansbold.ttf', 20)


        Text1Surf = largeText.render("SPACE", True, (255, 255, 255))
        Text1Rect = Text1Surf.get_rect()
        Text2Surf = mediumText.render("INVADERS", True, (0, 255, 0))
        Text2Rect = Text2Surf.get_rect()

        Text3Surf = smallText.render(" = 50 points", True, (255, 255, 255))
        Text3Rect = Text3Surf.get_rect()
        Image3Surf = pygame.image.load('images/Alien1.png')
        Image3Rect = Image3Surf.get_rect()

        Text5Surf = smallText.render(" = 50 points", True, (255, 255, 255))
        Text5Rect = Text5Surf.get_rect()
        Image5Surf = pygame.image.load('images/Alien2.png')
        Image5Rect = Image5Surf.get_rect()

        Text6Surf = smallText.render(" = 50 points", True, (255, 255, 255))
        Text6Rect = Text6Surf.get_rect()
        Image6Surf = pygame.image.load('images/Alien3.png')
        Image6Rect = Image6Surf.get_rect()

        Text7Surf = smallText.render(" = 50 points", True, (255, 255, 255))
        Text7Rect = Text7Surf.get_rect()
        Image7Surf = pygame.image.load('images/AlienMS.png')
        Image7Rect = Image7Surf.get_rect()

        Text4Surf = smallerText.render("By: Ivan Rosales", True, (255, 255, 255))
        Text4Rect = Text4Surf.get_rect()

        Text1Rect.center = ((ai_settings.screen_width / 2), (ai_settings.screen_height / 20) * 3)
        screen.blit(Text1Surf, Text1Rect)
        Text2Rect.center = ((ai_settings.screen_width / 2), (ai_settings.screen_height / 20) * 5)
        screen.blit(Text2Surf, Text2Rect)

        Text3Rect.center = ((ai_settings.screen_width / 2) + 50, (ai_settings.screen_height / 20) * 7)
        screen.blit(Text3Surf, Text3Rect)
        Image3Rect.centery = Text3Rect.centery
        Image3Rect.centerx = Text3Rect.centerx - 150
        screen.blit(Image3Surf, Image3Rect)

        Text5Rect.center = ((ai_settings.screen_width / 2) + 50, (ai_settings.screen_height / 20) * 9)
        screen.blit(Text3Surf, Text5Rect)
        Image5Rect.centery = Text5Rect.centery
        Image5Rect.centerx = Text5Rect.centerx - 150
        screen.blit(Image5Surf, Image5Rect)

        Text6Rect.center = ((ai_settings.screen_width / 2) + 50, (ai_settings.screen_height / 20) * 11)
        screen.blit(Text3Surf, Text6Rect)
        Image6Rect.centery = Text6Rect.centery
        Image6Rect.centerx = Text6Rect.centerx - 150
        screen.blit(Image6Surf, Image6Rect)

        Text7Rect.center = ((ai_settings.screen_width / 2) + 50, (ai_settings.screen_height / 20) * 13)
        screen.blit(Text3Surf, Text7Rect)
        Image7Rect.centery = Text7Rect.centery
        Image7Rect.centerx = Text7Rect.centerx - 150
        screen.blit(Image7Surf, Image7Rect)

        Text4Rect.center = ((ai_settings.screen_width / 2), (ai_settings.screen_height / 20) * 17)
        screen.blit(Text4Surf, Text4Rect)



        # checks if the play button has been pressed
        play_button.draw_button()
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            intro = False

        pygame.display.update()
        clock.tick(60)
