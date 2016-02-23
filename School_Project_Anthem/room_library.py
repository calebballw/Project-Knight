import pygame
class Room():
    wall_list = None
    enemy_sprites = None
    key_list = None
    
    def __init__(self):
        self.wall_list = pygame.sprite.Group()
        self.friendly = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.key_list = pygame.sprite.Group()
        self.light = pygame.sprite.Group()
        self.light2 = pygame.sprite.Group()