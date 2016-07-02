import pygame
white = (255, 255, 255)
class Key(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.key1 = pygame.image.load("key.png").convert()
        
        self.image = self.key1
        self.image.set_colorkey(white)
        
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
