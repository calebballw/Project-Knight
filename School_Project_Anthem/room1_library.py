import pygame
import room_library
import wall1
import key_library
import yoshi_library

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

class Room1(room_library.Room):
    def __init__(self):
        self.background_image = pygame.image.load("Street_Sweeper.jpg")
        room_library.Room.__init__(self)
        walls = [ [0,0,240,20], #Top Left Wall
                  [550,0,330,20], #Top Right Wall
                  [220,20,20,210], #Vertical House Top Left
                  [550,20,20,210], #Vertical House Top Right
                  [20,230,220,10], #Horizontal House Top Left
                  [550,230,230,10], #Horizontal House Top Right
                  [550,380,230,10], #Horizontal House Bottom Right
                  [20,380,220,10], #Horizontal House Bottom Left
                  [220,380,20,220], #Vertical House Bottom Left
                  [550,380,20,220] #Vertical House Bottom Right
                ]
        for item in walls:
            wall = wall1.Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)
        self.yoshi = yoshi_library.Yoshi(400, 100)
        self.friendly.add(self.yoshi)