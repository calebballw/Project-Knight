import pygame
import wall1
import room_library
import knight_library
import key_library
import game_knight

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

class Room2(room_library.Room):
    def __init__(self):
        self.background_image = pygame.image.load("Equality's Cave.jpg").convert()
        room_library.Room.__init__(self)
        walls = [ [0,0,20,240], #Left top Wall
                  [0,400,20,260], #left bottom wall
                  [780,0,20,600], #Right Wall
                  [0,0,800,20], #Top Wall
                  [0,580,800,20] #Bottom Wall
                ]
        for item in walls:
            wall = wall1.Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)
        self.key = key_library.Light(500, 100)
        self.light.add(self.key)
