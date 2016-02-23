import pygame
white = (255,255,255)
black = (0,0,0)
class Key(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.key1 = pygame.image.load("wires.png").convert()
        
        self.image = self.key1
        self.image.set_colorkey(black)
        
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
class Screen(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.screen = pygame.image.load("screen.png")
        
        self.image = self.screen
        
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
class Power(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.power = pygame.image.load("power.png")
        self.image = self.power
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
class Light(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.light = pygame.image.load("lightbulb.png")
        self.image = self.light
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
    
    
