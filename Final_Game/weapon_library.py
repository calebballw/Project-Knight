import pygame
white = (255, 255, 255)
black = (0,0,0)
class Bow(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.bow = pygame.image.load("bow.png").convert()
        
        self.image = self.bow
        self.image.set_colorkey(black)
        
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x