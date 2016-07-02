import pygame
import wall1
import room_library
import knight_library

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

class Cafeteria(room_library.Room):
    def __init__(self):
        self.background_image = pygame.image.load("Cafeteria.png").convert()
        room_library.Room.__init__(self)
        walls = [ [0,0,20,600], #Left Wall
                  [780,0,20,235], #Right Top Wall
                  [780,365,20,235], #Right Bottom Wall
                  [0,0,780,20], #Top Wall
                  [0,580,780,20] #Bottom Wall
                ]
        for item in walls:
            wall = wall1.Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)