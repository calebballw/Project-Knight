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
        
        self.originx = x
        self.originy = y
        
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        
        self.changex = 3
        self.changey = 0
        
        self.stun_check = 1
        self.lives = 3
    
    def update(self, x, y, bullets):
        self.rect.x += self.changex * self.stun_check
        self.rect.y += self.changey * self.stun_check
        
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
        
        dragon_hit_list = pygame.sprite.spritecollide(self, bullets, True)
        for dragon in dragon_hit_list:
            if self.stun_check == 0:
                self.lives -= 1
                self.rect.x += 50
                self.stun_check = 1
    def reset(self):
        self.rect.x = self.originx
        self.rect.y = self.originy
    
    def stunned(self):
        self.rect.x = self.originx
        self.rect.y = self.originy
        self.stun_check = 0
    
    def unstunned(self):
        self.stun_check = 1
    
