import pygame
import wall1
import room_library
import room1_library
import room2_library
import player_library
import game_knight
#Define Colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
#Tells how big the screen is
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
#The whole game in one function
def main():
    #setup screen
    pygame.init()
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    #Add Caption    
    pygame.display.set_caption("My Game")
    #Game Variables
    done = False
    clock = pygame.time.Clock()
    game = game_knight.Game()
    #Main Program Loop
    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_screen(screen)
        clock.tick(60)
    pygame.quit()
#Play the Game
main()