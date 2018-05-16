import pygame
import player_library
import game_knight
white = (255, 255, 255)
class Knight(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.knightf = pygame.image.load("knight_front.png").convert()
        self.knightb = pygame.image.load("knightb.png").convert()
        
        self.image = self.knightf
        self.image.set_colorkey(white)
        
        self.orginx = x
        self.orginy = y
        
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        
        self.changex = 3
        self.changey = 3 
    def update(self, x, y):
        self.rect.y += self.changey
        self.rect.x += self.changex
        
        if y - self.rect.y == 0:
            self.changey = 0
        else:
            self.changey = ((y - self.rect.y)/abs(y - self.rect.y))*3
        if x - self.rect.x == 0:
            self.changex = 0
        else:
            self.changex = ((x - self.rect.x)/abs(x - self.rect.x))*3
            
    def position(self):
        return [self.rect.x, self.rect.y]
    
    def reset(self):
        self.rect.x = self.orginx
        self.rect.y = self.orginy
