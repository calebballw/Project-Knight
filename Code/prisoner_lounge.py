import pygame
import wall1
from room import Room
import knight_library
import key_library


black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

class Prisoner_Lounge(Room):
    def __init__(self):
        self.background_image = pygame.image.load("Images/prisoners lounge.jpg").convert()
        Room.__init__(self)
        walls = [ [0,0,20,235], #Left Top Wall
                  [0,365,20,235], #Left Bottom Wall
                  [780,0,20,600], #Right Wall
                  [0,0,780,20], #Top Wall
                  [0,580,320,20], #Bottom Left Wall
                  [550,580,330,20]  #Bottom Right Wall
                ]
        for item in walls:
            wall = wall1.Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)
        self.key = key_library.Key(400, 300)
        self.dc_key_list.add(self.key)
        
        self.enemy = knight_library.Knight(200, 100)
        self.enemy_sprites.add(self.enemy)
        self.enemy2 = knight_library.Knight(700, 100)
        self.enemy_sprites.add(self.enemy2)
        
    def reset_knights(self):
        self.enemy.reset()
        self.enemy2.reset()

