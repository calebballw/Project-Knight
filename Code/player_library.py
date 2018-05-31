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
        self.lives = 7
        self.princef = pygame.image.load("Images/prince.png").convert()
        self.princeb = pygame.image.load("Images/princeb.png").convert()
        self.princel = pygame.image.load("Images/prince_left.png").convert()
        self.princer = pygame.image.load("Images/prince_right.png").convert()
        self.princed = pygame.image.load("Images/prince_dead.png").convert()
        self.bprincef = pygame.image.load("Images/bow_man_front.png").convert()
        self.bprinceb = pygame.image.load("Images/bow_man_back.png").convert()
        self.bprincer = pygame.image.load("Images/bow_man_right.png").convert()
        self.bprincel = pygame.image.load("Images/bow_man_left.png").convert()
        
        self.image = self.princef
        self.image.set_colorkey(white)
        
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
    def print_character(self, character, color=None):
        if color is None:
            color = white
        else:
            color = color
        self.image = character
        self.image.set_colorkey(color)
    
    def flip(self, direction):
        if direction == "up":
            self.print_character(self.princeb)
        if direction == "down":
            self.print_character(self.princef)
        if direction == "left":
            self.print_character(self.princel)
        if direction == "right":
            self.print_character(self.princer)
    def flipbow(self, direction):
        if direction == "up":
            self.print_character(self.bprinceb, black)
        if direction == "down":
            self.print_character(self.bprincef, black)
        if direction == "left":
            self.print_character(self.bprincel, black)
        if direction == "right":
            self.print_character(self.bprincer, black)
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y
    def update(self, walls, badguys, dragon):
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
        
        block_hit_list = pygame.sprite.spritecollide(self, dragon, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.y += -100
                self.lives -= 1
            if self.change_y <0:
                self.rect.y += 100
                self.lives -= 1
            if self.change_x > 0:
                self.rect.x += -100
                self.lives -= 1
            if self.change_x < 0:
                self.rect.x += 100
                self.lives -= 1
        
                
    def position(self):
        return [self.rect.x, self.rect.y]
                
                