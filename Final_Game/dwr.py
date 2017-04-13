import pygame
import wall1
from room import Room
import knight_library

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

class DWR(Room):
    def __init__(self):
        self.background_image = pygame.image.load("dragon wait room.jpg").convert()
        Room.__init__(self)
        walls = [ [0,0,20,235], #Left Top Wall
                  [0,365,20,235], #Left Bottom
                  [780,0,20,235], #Right Top Wall
                  [780,365,20,235], #Right Bottom Wall
                  [0,0,410,20], #Top Left Wall
                  [530,0,330,20], #Top Right Wall
                  [0,580,420,20], #Bottom Left Wall
                  [530,580,330,20]  #Bottom Right Wall
                ]
        for item in walls:
            wall = wall1.Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)
        self.enemy = knight_library.Knight(400, 300)
        self.enemy_sprites.add(self.enemy)
