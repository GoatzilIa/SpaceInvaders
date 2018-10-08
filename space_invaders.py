import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
from bunker import Bunker
import game_functions as gf
import start_screen as ss
import game_over as go

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Space Invaders")
    clock = pygame.time.Clock()
    
    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")
    
    # Create an instance to store game statistics, and a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Set the background color.
    bg_color = (230, 230, 230)
    
    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    alienMS = Alien(ai_settings, screen, 6)
    bullets = Group()
    aliens = Group()
    bunkers = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    gf.create_bunkers(ai_settings, screen, bunkers)

    # show the game intro
    ss.Start_Screen(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, clock)
    # go.Game_Over(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, clock)

    # starter tick
    start_ticks = pygame.time.get_ticks()
    seconds = 0
    counter = 1
    flip = True
    flag = True

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
            aliens, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                bullets, alienMS)
            gf.check_MS_hit(ai_settings, stats, sb, screen, bullets, alienMS)
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, alienMS,
            bullets, play_button, seconds, flag, bunkers)

        # checks if no lives are left and displays the "game over" screen
        if stats.ships_left == 0:
            stats.game_active = False
            go.Game_Over(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, clock)
            seconds = int((pygame.time.get_ticks() - start_ticks) / 500)
            counter = seconds

        # keeps track of the seconds the game has been running for
        seconds = int((pygame.time.get_ticks() - start_ticks) / 500)

        # changes the alien image depending on how long the program has been running (animation)
        if seconds == counter:
            counter += 1
            if flip:
                gf.flip_aliens_1(aliens)
                flip = False
            elif not flip:
                gf.flip_aliens_2(aliens)
                flip = True

run_game()
