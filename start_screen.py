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
        smallText =  pygame.font.Font('freesansbold.ttf', 40)
        smallerText = pygame.font.Font('freesansbold.ttf', 20)
        Text1Surf, Text1Rect = text_objects("Space", largeText)
        Text2Surf, Text2Rect = text_objects("Invaders", smallText)
        Text3Surf, Text3Rect = text_objects("First to 5 points wins", smallText)
        Text4Surf, Text4Rect = text_objects("By: Ivan Rosales", smallerText)

        Text1Rect.center = ((ai_settings.screen_width / 2), (ai_settings.screen_height / 20) * 3)
        screen.blit(Text1Surf, Text1Rect)
        Text2Rect.center = ((ai_settings.screen_width / 2), (ai_settings.screen_height / 20) * 6)
        screen.blit(Text2Surf, Text2Rect)
        Text3Rect.center = ((ai_settings.screen_width / 2), (ai_settings.screen_height / 20) * 14)
        screen.blit(Text3Surf, Text3Rect)
        Text4Rect.center = ((ai_settings.screen_width / 2), (ai_settings.screen_height / 20) * 17)
        screen.blit(Text4Surf, Text4Rect)

        # checks if the play button has been pressed
        play_button.draw_button()
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            intro = False

        pygame.display.update()
        clock.tick(60)

def text_objects(text, font):
    textSurface = font.render(text, True,(0, 255, 0) )
    return textSurface, textSurface.get_rect()