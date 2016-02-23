import pygame

white = (255, 255, 255)
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface([width, height])
        self.image.fill(white)
        self.image.set_colorkey(white)
        
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x