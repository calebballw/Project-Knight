import pygame

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
        
        """
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
        """
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
        
