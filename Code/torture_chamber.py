import pygame
from room import Room
import wall1
import key_library
import knight_library

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

class Torture_Chamber(Room):
    def __init__(self):
        self.background_image = pygame.image.load("Images/torture_room.jpg")
        Room.__init__(self)
        walls = [ [0,20,20,580], #Left Wall
                  [780,0,20,600], #Right Wall
                  [0,0,320,20], #Top Left Wall
                  [450,0,330,20], #Top Right Wall
                  [20,580,760,20] #Bottom Wall
                ]
        for item in walls:
            wall = wall1.Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)
        self.key = key_library.Key(400, 300)
        self.wr_key_list.add(self.key)
        
        self.enemy = knight_library.Knight(200, 100)
        self.enemy_sprites.add(self.enemy)
        self.enemy2 = knight_library.Knight(700, 100)
        self.enemy_sprites.add(self.enemy2)
        
    def reset_knights(self):
        self.enemy.reset()
        self.enemy2.reset()

