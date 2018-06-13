import pygame
import bullet_library
from room import Room

white = (255, 255, 255)
black = (0, 0, 0)
class Dragon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.dragon = pygame.image.load("Images/dragon.png").convert()
        self.dragonl = pygame.image.load("Images/dragonl.png").convert()
        
        self.image = self.dragon
        self.image.set_colorkey(black)
        
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        
        self.changex = 3
        self.changey = 0
    
    def update(self, x, y):
        self.rect.x += self.changex
        self.rect.y += self.changey
        
        if y - self.rect.y == 0:
            self.changey = 0
        else:
            self.changey = ((y - self.rect.y)/abs(y - self.rect.y))*3
        if x - self.rect.x == 0:
            self.changex = 0
        else:
            self.changex = ((x - self.rect.x)/abs(x - self.rect.x))*3
            if self.changex < 0:
                self.image = self.dragonl
                self.image.set_colorkey(black)
            else:
                self.image = self.dragon
                self.image.set_colorkey(black)       
        #self.bullet = bullet_library.Bullet()
        #self.bullet.rect.x = self.rect.x + 30
        #self.bullet.rect.y = self.rect.y
        #if self.image == self.dragon:
        #    self.bullet.way("right")
        #else:
        #    self.bullet.way("left")
        #self.fire.add(self.bullet)
