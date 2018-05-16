import pygame
import wall1
from room import Room
import knight_library

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

class Hallway(Room):
    def __init__(self):
        self.background_image = pygame.image.load("hallway.jpg").convert()
        Room.__init__(self)
        walls = [ [210,0,20,600], #Left Wall
                  [585,0,20,90], #Right Top Wall
                  [585,190,20,150], #Right Middle Wall
                  [585,440,20,160], #Right Bottom Wall
                  [0,0,780,20], #Top Wall
                  [0,580,230,20], #Bottom Left Wall
                  [585,580,330,20]  #Bottom Right Wall
                ]
        for item in walls:
            wall = wall1.Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)
        self.enemy = knight_library.Knight(200, 50)
        self.enemy_sprites.add(self.enemy)
        self.enemy2 = knight_library.Knight(400, 500)
        self.enemy_sprites.add(self.enemy2)
        
    def reset_knights(self):
        self.enemy.reset()
        self.enemy2.reset()
