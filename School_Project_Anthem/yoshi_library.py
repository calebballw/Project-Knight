import pygame
white = (255, 255, 255)
black = (0, 0, 0)
class Yoshi(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.yoshil = pygame.image.load("Yoshi_Left.png").convert()
        self.yoshir = pygame.image.load("Yoshi_Right.png").convert()
        
        self.image = self.yoshir
        self.image.set_colorkey(white)
        
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        
        self.change = 3
        self.helpy = 3
        self.helpx = 0
    def update(self, hels):
        if hels == "F":
            self.rect.x += self.change
            if self.rect.x >= 500:
                self.image = self.yoshil
                self.image.set_colorkey(white)
                self.change = -3
            if self.rect.x <= 200:
                self.image = self.yoshir
                self.image.set_colorkey(white)
                self.change = 3
        else:
            self.change = 0
            self.rect.y += self.helpy
            if self.rect.y >= 300:
                self.helpy = 0
                self.helpx = 3
            self.rect.x += self.helpx
            if self.rect.x >= 700:
                self.helpx = 0