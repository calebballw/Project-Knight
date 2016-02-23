import pygame
import wall1
import room_library
import knight_library
import key_library

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

class Room4(room_library.Room):
    def __init__(self):
        self.background_image = pygame.image.load("Council of Scholars.png").convert()
        room_library.Room.__init__(self)
        walls = [ [0,0,20,600], #Left top Wall
                  [780,0,20,240], #Right Top Wall
                  [780,400,20,260], #Right Bottom Wall
                  [20,400,800,20], #1st bottom wall
                  [0,0,800,20], #1st Top Wall
                  [20,150,800,20], # 2nd Top Wall
                  [0,580,800,20], # 2nd Bottom Wall
                  [325,245,150,20], #Table Top Wall
                  [475,245,10,75], #Table Right Wall
                  [325,310,150,10], #Table Bottom Wall
                  [325,245,10,75] #Table Left Wall
                ]
        for item in walls:
            wall = wall1.Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)
        self.enemy = knight_library.Knight(100, 150)
        self.enemy_sprites.add(self.enemy)
        self.enemy = knight_library.Knight(100, 450)
        self.enemy_sprites.add(self.enemy)
        self.key = key_library.Light(100, 300)
        self.light2.add(self.key)
