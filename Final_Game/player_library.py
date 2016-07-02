import pygame
import wall1
import knight_library

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 3
        self.princef = pygame.image.load("prince.png").convert()
        self.princeb = pygame.image.load("princeb.png").convert()
        self.princel = pygame.image.load("prince_left.png").convert()
        self.princer = pygame.image.load("prince_right.png").convert()
        self.princed = pygame.image.load("prince_dead.png").convert()
        
        self.image = self.princef
        self.image.set_colorkey(white)
        
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
    def print_character(self, character):
        self.image = character
        self.image.set_colorkey(white)
    def flip(self, direction):
        if direction == "up":
            self.print_character(self.princeb)
        if direction == "down":
            self.print_character(self.princef)
        if direction == "left":
            self.print_character(self.princel)
        if direction == "right":
            self.print_character(self.princer)
        
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y
    def update(self, walls, badguys):
        self.rect.x += self.change_x
        
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
        block_hit_list = pygame.sprite.spritecollide(self, badguys, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.x += -50
                self.lives -= 1
            if self.change_x < 0:
                self.rect.x += 50
                self.lives -= 1
                
        self.rect.y += self.change_y
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
                
        block_hit_list = pygame.sprite.spritecollide(self, badguys, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.y += -100
                self.lives -= 1
            if self.change_y < 0:
                self.rect.y += 100
                self.lives -= 1
                
                