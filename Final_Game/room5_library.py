import pygame
import wall1
import room_library
import knight_library

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

class Execution_Chamber(room_library.Room):
    def __init__(self):
        self.background_image = pygame.image.load("execution chamber.jpg").convert()
        room_library.Room.__init__(self)
        walls = [ [0,0,20,235], #Left Top Wall
                  [0,365,20,235], #Left Bottom 
                  [780,0,20,600], #Right Top Wall
                  [0,0,780,20], #Top Wall
                  [0,580,320,20], #Bottom Left Wall
                  [450,580,330,20]  #Bottom Right Wall
                ]
        for item in walls:
            wall = wall1.Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)