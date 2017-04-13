import pygame
import wall1
from room import Room
import knight_library
import key_library

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

class Dragon_Cave(Room):
    def __init__(self):
        self.background_image = pygame.image.load("Dragon_Cave.jpg").convert()
        Room.__init__(self)
        walls = [ [0,0,20,600], #Right Wall
                  [780,0,20,600], #Left Wall
                  [0,580,320,20], #Bottom Left Wall
                  [450,580,330,20], #Bottom Right Wall
                  [0,0,320,20], #Top Left Wall
                  [480,0,330,20] #Top Right Wall
                ]
        for item in walls:
            wall = wall1.Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)
        self.key = key_library.Key(400, 300)
        self.exit_hallway_key_list.add(self.key)
