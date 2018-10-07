import pygame
from settings import Settings
from pygame.time import Clock
from button import Button
import game_functions as gf

def Game_Over(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, clock):
    """creates a start screen"""
    over = True

    while over:
        """shows the game over screen until the player clicks the play button"""
        screen.fill((20, 20, 20))
        largeText = pygame.font.Font('freesansbold.ttf', 80)
        smallText =  pygame.font.Font('freesansbold.ttf', 40)

        Text1Surf = largeText.render("Game Over", True, (255, 0, 0))
        Text1Rect = Text1Surf.get_rect()
        Text2Surf = smallText.render("Play Again?", True, (255, 255, 255))
        Text2Rect = Text2Surf.get_rect()
        Text3Surf = smallText.render("Your High Score: " + str(stats.high_score), True, (255, 255, 255))
        Text3Rect = Text3Surf.get_rect()

        Text1Rect.center = ((ai_settings.screen_width / 2), (ai_settings.screen_height / 20) * 4)
        screen.blit(Text1Surf, Text1Rect)
        Text2Rect.center = ((ai_settings.screen_width / 2), (ai_settings.screen_height / 20) * 11)
        screen.blit(Text2Surf, Text2Rect)
        Text3Rect.center = ((ai_settings.screen_width / 2), (ai_settings.screen_height / 20) * 8)
        screen.blit(Text3Surf, Text3Rect)

        pygame.mouse.set_visible(True)

        # checks if the play button has been pressed
        play_button.draw_button()
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            over = False

        pygame.display.update()
        clock.tick(60)
