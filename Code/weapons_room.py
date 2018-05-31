import pygame
import wall1
from room import Room
import knight_library
import weapon_library

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

class Weapons_Room(Room):
    def __init__(self):
        self.background_image = pygame.image.load("Images/Weapons_Room.jpg").convert()
        Room.__init__(self)
        walls = [ [0,0,20,600], #Right Wall
                  [780,0,20,600], #Left Wall
                  [0,580,780,20], #Bottom Wall
                  [0,0,450,20], #Top Left Wall
                  [650,0,130,20] #Top Right Wall
                ]
        for item in walls:
            wall = wall1.Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)
            self.weapon = weapon_library.Bow(250, 250)
            self.weapons_list.add(self.weapon)
            
        self.enemy = knight_library.Knight(200, 100)
        self.enemy_sprites.add(self.enemy)
        self.enemy2 = knight_library.Knight(700, 100)
        self.enemy_sprites.add(self.enemy2)
        
    def reset_knights(self):
        self.enemy.reset()
        self.enemy2.reset()

