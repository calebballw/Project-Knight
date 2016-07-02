import pygame
white = (255, 255, 255)
class Knight(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.knightf = pygame.image.load("knight_front.png").convert()
        self.knightb = pygame.image.load("knightb.png").convert()
        
        self.image = self.knightf
        self.image.set_colorkey(white)
        
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        
        self.change = 3
    def update(self):
        self.rect.y += self.change
        if self.rect.y >= 500:
            self.image = self.knightb
            self.image.set_colorkey(white)
            self.change = -3
        if self.rect.y <= 200:
            self.image = self.knightf
            self.change = 3
