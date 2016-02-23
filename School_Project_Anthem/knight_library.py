import pygame
white = (255, 255, 255)
black = (0, 0, 0)
class Knight(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.doofl = pygame.image.load("Heinz_Doofenshmirtz.png").convert()
        self.doofr = pygame.image.load("Doof Right.png").convert()
        
        self.image = self.doofl
        self.image.set_colorkey(black)
        
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        
        self.change = 3
        self.cos = False
    def update(self):
        if self.cos == False:
            self.rect.x += self.change
            if self.rect.x >= 500:
                self.image = self.doofl
                self.image.set_colorkey(black)
                self.change = -3
            if self.rect.x <= 200:
                self.image = self.doofr
                self.image.set_colorkey(white)
                self.change = 3
        else:
            self.rect.x = 700
            self.rect.y = 200
            self.rect.y += self.change
            if self.rect.y >= 400:
                self.change = -3
            if self.rect.y <= 200:
                self.change = 3
