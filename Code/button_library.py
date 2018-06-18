import pygame
white = (255, 255, 255)
black = (0,0,0)
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.red_circle = pygame.image.load("Images/red_circle.png").convert()
        self.green_circle = pygame.image.load("Images/green_circle.png").convert()
        
        self.image = self.red_circle
        self.image.set_colorkey(black)
        
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
    def change_color(self):
        self.image = self.green_circle
        self.image.set_colorkey(black)