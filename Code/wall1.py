import pygame

white = (255, 255, 255)
black = (0, 0, 0)
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)
        
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x