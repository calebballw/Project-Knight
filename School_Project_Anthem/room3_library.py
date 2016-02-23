import pygame
import wall1
import room_library
import knight_library

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

class Room3(room_library.Room):
    def __init__(self):
        self.background_image = pygame.image.load("Uncharted Forest.png").convert()
        room_library.Room.__init__(self)
        walls = [ [540,180,20,420], #Right Wall
                  [220,180,20,420], #Left Wall
                  [240,180,300,20], #Top Wall
                  [0,580,240,20], #Bottom Left Wall
                  [550,580,330,20] #Bottom Right Wall
                ]
        for item in walls:
            wall = wall1.Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)