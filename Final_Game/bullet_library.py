import pygame
black = (0,0,0)
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.iv = pygame.Surface([4, 10])
        self.ih = pygame.Surface([10, 4])
        
        self.image = self.iv
        self.image.fill(black)
        
        self.rect = self.image.get_rect()
        self.change_y = 10
        self.change_x = 10

    def print_image(self, direction):
        self.image = direction
        self.image.fill(black)
        
    def way(self, direction):
        if direction == "up":
            self.print_image(self.iv)
            self.change_y = -10
        if direction == "down":
            self.print_image(self.iv)
            self.change_y = 10
        if direction == "left":
            self.print_image(self.ih)
            self.change_x = -10
        if direction == "right":
            self.print_image(self.ih)
            self.change_x = 10
    def update(self):
        if self.image == self.iv:
            self.rect.y += self.change_y
        elif self.image == self.ih:
            self.rect.x += self.change_x
    
        