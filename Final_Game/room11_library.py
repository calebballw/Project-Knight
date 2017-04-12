import pygame
import wall1
import room_library
import knight_library
import key_library

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

class Prisoner_Lounge(room_library.Room):
    def __init__(self):
        self.background_image = pygame.image.load("prisoners lounge.jpg").convert()
        room_library.Room.__init__(self)
        walls = [ [0,0,20,235], #Left Top Wall
                  [0,365,20,235], #Left Bottom Wall 
                  [780,0,20,600], #Right Wall
                  [0,0,780,20], #Top Wall
                  [0,580,320,20], #Bottom Left Wall
                  [450,580,330,20]  #Bottom Right Wall
                ]
        for item in walls:
            wall = wall1.Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)
        self.key = key_library.Key(400, 300)
        self.dc_key_list.add(self.key)