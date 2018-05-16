import pygame

white = (255, 255, 255)
black = (0, 0, 0)
class Dragon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.dragon = pygame.image.load("dragon.png").convert()
        self.dragonr = pygame.image.load("dragon_r.png").convert()
        
        self.image = self.dragon
        self.image.set_colorkey(black)
        
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        
        self.changex = 3
        self.changey = 0
    
    def update(self):
        self.rect.x += self.changex
        self.rect.y += self.changey
        
        
        if self.rect.x >= 400:
            self.changex = 0
            self.changey = 3
        if self.rect.y >= 300:
            self.changey = 0
            self.changex = -3
        if self.rect.x <= 100:
            self.changex = 0
            self.changey = -3
        if self.rect.y <= 75 and self.rect.x <= 400:
            self.changey = 0
            self.changex = 3
        
