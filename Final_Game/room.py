import pygame
class Room(object):
    wall_list = None
    enemy_sprites = None
    wr_key_list = None
    
    def __init__(self):
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.wr_key_list = pygame.sprite.Group()
        self.dc_key_list = pygame.sprite.Group()
        self.exit_hallway_key_list = pygame.sprite.Group()
        self.weapons_list = pygame.sprite.Group()
