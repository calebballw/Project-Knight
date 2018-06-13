import pygame
import wall1
import player_library
import room
from torture_chamber import Torture_Chamber
from dwr import DWR
from dragon_cave import Dragon_Cave
from weapons_room import Weapons_Room
from execution_chamber import Execution_Chamber
from hallway import Hallway
from lava_pit import Lava_Pit
from first_cell import First_Cell
from exit_hallway import Exit_Hallway
from second_cell import Second_Cell
from prisoner_lounge import Prisoner_Lounge
from cafeteria import Cafeteria
import knight_library
import bullet_library
import math_stuff
import dragon_library
#Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

class Game():
    def __init__(self):
        #Game Functionality
        self.count = 0
        self.menu_image = pygame.image.load("Images/intro.png")
        self.background_image = pygame.image.load("Images/lava_pit.png").convert()
        self.torture = pygame.image.load("Images/torture_room.jpg").convert()
        self.prince = pygame.image.load("Images/prince_right.png").convert()
        self.bad_dude = pygame.image.load("Images/knightb.png").convert()
        self.game_over = False
        self.lava_over = False
        self.dragon_key_yes = False
        self.wr_key_yes = False
        self.exit_key_yes = False
        self.weapons_yes = True
        self.you_win = False
        self.display_s = True
        self.arrows = 30
        self.game_start = True
        self.inu = 0

        #Main lists
        self.rooms = {}
        self.movingsprites = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()
        self.fire_list = pygame.sprite.Group()
        

        self.rooms['torture_chamber'] = Torture_Chamber()
        self.rooms['DWR'] = DWR()
        self.rooms['dragon_cave'] = Dragon_Cave()
        self.rooms['weapons_room'] = Weapons_Room()
        self.rooms['execution_chamber'] = Execution_Chamber()
        self.rooms['hallway'] = Hallway()
        self.rooms['lava_pit'] = Lava_Pit()
        self.rooms['first_cell'] = First_Cell()
        self.rooms['exit_hallway'] = Exit_Hallway()
        self.rooms['second_cell'] = Second_Cell()
        self.rooms['prisoner_lounge'] = Prisoner_Lounge()
        self.rooms['cafeteria'] = Cafeteria()

        #room setup
        self.current_room_name = 'dragon_cave'
        print ("setexithallway")
        self.current_room = self.rooms[self.current_room_name]

        #Player
        self.player = player_library.Player(300, 300)
        self.movingsprites.add(self.player)

    def display_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.display_s = False
    def game_star(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    self.inu += 1
                    if self.inu == 3:
                        self.game_start = False


    def process_events(self):
        for event in pygame.event.get():
            #Checks to see if you exit the game
            if event.type == pygame.QUIT:
                return True
            #Checks to see if you type
            elif event.type == pygame.KEYDOWN:
                #Left Arrow Key, Move Left
                if event.key == pygame.K_LEFT:
                    if self.weapons_yes:
                        self.player.flipbow("left")
                    else:
                        self.player.flip("left")
                    self.player.changespeed(-10, 0)
                #Right Arrow Key, Move Right
                elif event.key == pygame.K_RIGHT:
                    if self.weapons_yes:
                        self.player.flipbow("right")
                    else:
                        self.player.flip("right")
                    self.player.changespeed(10, 0)
                #Up Arrow Key, Move Up
                elif event.key == pygame.K_UP:
                    if self.weapons_yes:
                        self.player.flipbow("up")
                    else:
                        self.player.flip("up")
                    self.player.changespeed(0, -10)
                #Down Arrow Key, Move Down
                elif event.key == pygame.K_DOWN:
                    if self.weapons_yes:
                        self.player.flipbow("down")
                    else:
                        self.player.flip("down")
                    self.player.changespeed(0, 10)
                #Spacebar, Shoot Something
                elif event.key == pygame.K_SPACE:
                    if self.weapons_yes == True and self.arrows > 0:
                        self.bullet = bullet_library.Bullet()
                        self.bullet.rect.x = self.player.rect.x + 30
                        self.bullet.rect.y = self.player.rect.y
                        if self.player.image == self.player.bprinceb:
                            self.bullet.way("up")
                        elif self.player.image == self.player.bprincef:
                            self.bullet.way("down")
                        elif self.player.image == self.player.bprincel:
                            self.bullet.way("left")
                        elif self.player.image == self.player.bprincer:
                            self.bullet.way("right")
                        self.bullet_list.add(self.bullet)
                        
                        #self.fire = bullet_library.Bullet()
                        #self.fire.rect.x = self.current_room.dragon.rect.x + 30
                        #self.fire.rect.y = self.current_room.dragon.rect.y
                        #if self.current_room.dragon.image == self.current_room.dragon.dragon:
                        #    self.fire.way("right")
                        #else:
                        #    self.fire.way("left")
                        #self.fire_list.add(self.fire)
                        self.arrows -= 1

            # Reset speed when key goes up
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(10, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.changespeed(-10, 0)
                elif event.key == pygame.K_UP:
                    self.player.changespeed(0, 10)
                elif event.key == pygame.K_DOWN:
                    self.player.changespeed(0, -10)
        return False

    def change_rooms(self, name):
        #Moves player to the next room
        self.current_room_name = name
        self.current_room = self.rooms[name]
        self.current_room.reset_knights()


    def run_logic(self):
        if not self.game_over and not self.lava_over:
            #Makes all the sprites move
            #moves the player
            self.player.update(self.current_room.wall_list, self.current_room.enemy_sprites, self.current_room.boss)

            #moves the knights
            self.current_room.enemy_sprites.update(self.player.position()[0], self.player.position()[1])
            
            #moves the boss
            #self.current_room.boss.update(self.player.position()[0], self.player.position()[1])
            if self.current_room_name == 'dragon_cave':
                self.current_room.boss.update(self.player.position()[0], self.player.position()[1])
                if self.count % 10 == 0:
                    self.fire = bullet_library.Bullet()
                    self.fire.rect.x = self.current_room.dragon.rect.x + 30
                    self.fire.rect.y = self.current_room.dragon.rect.y
                    if self.current_room.dragon.image == self.current_room.dragon.dragon:
                       self.fire.way("right")
                    else:
                        self.fire.way("left")
                    self.fire_list.add(self.fire)
                self.count += 1
                self.current_room.dragon.fire.update()

            #Checks to see if the knight kills you
            if self.player.lives < 1:
                self.game_over = True

            #allows you to pick up the key
            key_hit_list = pygame.sprite.spritecollide(self.player, self.current_room.wr_key_list, True)
            dc_key_hit_list = pygame.sprite.spritecollide(self.player, self.current_room.dc_key_list, True)
            eh_key_hit_list = pygame.sprite.spritecollide(self.player, self.current_room.exit_hallway_key_list, True)
            weapon_hit_list = pygame.sprite.spritecollide(self.player, self.current_room.weapons_list, True)

            #makes the bullets move
            self.bullet_list.update()
            self.fire_list.update()
            #records that you have a key
            if key_hit_list:
                self.wr_key_yes = True
                #self.rooms['execution_chamber'].door_open()
            if dc_key_hit_list:
                self.dragon_key_yes = True
            if eh_key_hit_list:
                self.exit_key_yes = True
            if weapon_hit_list:
                self.weapons_yes = True
                print ("hi")

            #Checks to see if the bullet hit anything
            for bullet in self.bullet_list:
                bullet_hit_list = pygame.sprite.spritecollide(self.bullet, self.current_room.enemy_sprites, True)
                for block in bullet_hit_list:
                    self.bullet_list.remove(self.bullet)
                if self.bullet.rect.y < -10:
                    self.bullet_list.remove(self.bullet)
                    
#knights distance from the player                    
#dok = ((math_stuff.distance_form(self.rooms['DWR'].enemy.position())) - (math_stuff.distance_form(self.player.position())))    
            
            #Checks to see if you went up out of the room
            if self.player.rect.y < -15:
                if self.current_room_name == 'torture_chamber':
                    self.change_rooms('DWR')
                    self.player.rect.y = 550
                    self.player.rect.x = 440
                    self.rooms['DWR'].reset_knights()
                elif self.current_room_name == 'DWR':
                    if self.dragon_key_yes == True:
                        self.change_rooms('dragon_cave')
                        self.player.rect.y = 550
                        self.player.rect.x = 375
                    else:
                        self.player.rect.y += 50
                elif self.current_room_name == 'weapons_room':
                    self.player.rect.x = 350
                    self.change_rooms('execution_chamber')
                elif self.current_room_name == 'dragon_cave':
                    if self.exit_key_yes == True:
                        self.change_rooms('first_cell')
                        self.player.rect.x = 385
                    else:
                        self.player.rect.y += 50
                elif self.current_room_name == 'first_cell':
                    self.change_rooms('exit_hallway')
                    self.player.rect.x = 350
                    self.player.rect.y = 550
                elif self.current_room_name == 'second_cell':
                    self.change_rooms('prisoner_lounge')
                elif self.current_room_name == 'exit_hallway':
                    if self.exit_key_yes == True:
                        self.game_over = True
                        self.you_win = True
                    else:
                        print ("elsehere")
                        self.player.rect.y += 50
                if self.current_room_name != 'DWR' and self.current_room_name != 'exit_hallway':
                    self.player.rect.y = 550

            #Checks to see if you went down and out of the room
            if self.player.rect.y > 551:
                if self.current_room_name == 'DWR':
                    self.change_rooms('torture_chamber')
                    self.player.rect.x = 350
                elif self.current_room_name == 'dragon_cave':
                    if self.exit_key_yes == False:
                        self.player.rect.y -= 50
                    else:
                        self.change_rooms('DWR')
                        self.rooms['DWR'].reset_knights()
                elif self.current_room_name == 'execution_chamber':
                    if self.wr_key_yes == True:
                        self.player.rect.x = 550
                        self.change_rooms('weapons_room')
                        self.player.rect.y = 0
                    else:
                        self.player.rect.y -= 50
                elif self.current_room_name == 'exit_hallway':
                    self.change_rooms('first_cell')
                    self.player.rect.y = 0
                    self.player.rect.x = 400
                elif self.current_room_name == 'first_cell':
                    if self.dragon_key_yes == True:
                        self.change_rooms('dragon_cave')
                        self.player.rect.y = 0
                        self.player.rect.x = 350
                    else:
                        self.player.rect.y -= 50
                elif self.current_room_name == 'prisoner_lounge':
                    self.change_rooms('second_cell')
                if self.current_room_name != 'execution_chamber' and self.current_room_name != 'first_cell':
                    self.player.rect.y = 0
            #Checks to see if you went right and out of the room
            if self.player.rect.x > 790:
                if self.current_room_name == 'DWR':
                    self.change_rooms('execution_chamber')
                elif self.current_room_name == 'first_cell':
                    self.change_rooms('second_cell')
                    self.player.rect.y = 270
                elif self.current_room_name == 'exit_hallway':
                    self.change_rooms('prisoner_lounge')
                elif self.current_room_name == 'cafeteria':
                    self.change_rooms('exit_hallway')
                self.player.rect.x = 0
            #Checks to see if you went left and out of the room
            if self.player.rect.x < 0:
                if self.current_room_name == 'execution_chamber':
                    self.change_rooms('DWR')
                    self.player.rect.x = 790
                    self.rooms['DWR'].reset_knights()
                elif self.current_room_name == 'second_cell':
                    self.change_rooms('first_cell')
                    self.player.rect.x = 790
                elif self.current_room_name == 'prisoner_lounge':
                    self.change_rooms('exit_hallway')
                    self.player.rect.x = 790
                elif self.current_room_name == 'exit_hallway':
                    self.change_rooms('cafeteria')
                    self.player.rect.x = 790
                    self.rooms['cafeteria'].reset_knights()
            #Specific to leaving hallway only
            if self.player.rect.x > 605 and self.player.rect.y > 280:
                if self.current_room_name == 'hallway':
                    self.player.rect.y = 280
                    self.change_rooms('DWR')
                    self.rooms['DWR'].reset_knights()
                    self.player.rect.x = 0
            if self.player.rect.x > 605 and self.player.rect.y < 280:
                if self.current_room_name == 'hallway':
                    self.player.rect.y = 280
                    self.change_rooms('first_cell')
                    self.player.rect.x = 0
            if self.player.rect.y > 500:
                if self.current_room_name == 'hallway':
                    self.change_rooms('lava_pit')
                    self.player.rect.y = 0
            if self.current_room_name == 'lava_pit' and self.player.rect.y >= 50:
                self.lava_over = True
            #Specific to entering hallway only
            if self.player.rect.x < 0:
                if self.current_room_name == 'DWR':
                    self.change_rooms('hallway')
                    self.player.rect.x = 585
                    self.player.rect.y = 360
                    self.rooms['DWR'].enemy.reset()
                elif self.current_room_name == 'first_cell':
                    self.change_rooms('hallway')
                    self.player.rect.x = 585
                    self.player.rect.y = 110

    def display_screen(self, screen):
        if not self.game_over and not self.lava_over and not self.display_s and not self.game_start:
            #Displays backround image for each room
            screen.blit(self.current_room.background_image, [0, 0])
            #Displays all the sprites and moving objects
            self.movingsprites.draw(screen)
            self.current_room.wall_list.draw(screen)
            self.current_room.enemy_sprites.draw(screen)
            self.current_room.wr_key_list.draw(screen)
            self.current_room.dc_key_list.draw(screen)
            self.current_room.exit_hallway_key_list.draw(screen)
            self.current_room.weapons_list.draw(screen)
            self.bullet_list.draw(screen)
            self.fire_list.draw(screen)
            self.current_room.boss.draw(screen)
            #Displays how many lives you have
            font = pygame.font.SysFont('Calibri', 25, True, False)
            text = font.render("Lives:" + str(self.player.lives), True, red)
            screen.blit(text, [150, 350])
            text2 = font.render("Arrows:" + str(self.arrows), True, blue)
            if self.weapons_yes == True:
                screen.blit(text2, [500, 350])
            #flips all this to the screen
            pygame.display.flip()
        elif self.game_over == True and self.you_win == True:
            font = pygame.font.SysFont('Calibri', 75, True, False)
            #screen.fill(white)
            text = font.render("You Win!", True, black)
            text_rect = text.get_rect()
            text_x = screen.get_width() / 2 - text_rect.width / 2
            text_y = screen.get_height() / 2 - text_rect.height / 2
            screen.blit(text, [text_x, text_y])
            pygame.display.flip()
        elif self.game_over == True:
            font = pygame.font.SysFont('Calibri', 75, True, False)
            #screen.fill(white)
            text = font.render("Game Over!", True, black)
            text_rect = text.get_rect()
            text_x = screen.get_width() / 2 - text_rect.width / 2
            text_y = screen.get_height() / 2 - text_rect.height / 2
            screen.blit(text, [text_x, text_y])
            pygame.display.flip()
        elif self.display_s == True:
            screen.blit(self.menu_image, [0, 0])
            pygame.display.flip()
        elif self.game_start == True:
            font = pygame.font.SysFont('Calibri', 50, True, False)
            screen.blit(self.torture, [0, 0])
            self.prince.set_colorkey(white)
            screen.blit(self.prince, [30, 180])
            self.bad_dude.set_colorkey(white)
            screen.blit(self.bad_dude, [350, 180])
            if self.inu == 0:
                text = font.render("Ah! Your killing me!", True, black)
                text_rect = text.get_rect()
                text_x = screen.get_width() / 2 - text_rect.width / 2
                text_y = screen.get_height() / 2 - text_rect.height / 2
                screen.blit(text, [text_x, text_y])
            elif self.inu == 1:
                text = font.render("Stop! You can't do this!!!", True, black)
                text_rect = text.get_rect()
                text_x = screen.get_width() / 2 - text_rect.width / 2
                text_y = screen.get_height() / 2 - text_rect.height / 2
                screen.blit(text, [text_x, text_y])
            elif self.inu == 2:
                text = font.render("Please! Stop!", True, black)
                text_rect = text.get_rect()
                text_x = screen.get_width() / 2 - text_rect.width / 2
                text_y = screen.get_height() / 2 - text_rect.height / 2
                screen.blit(text, [text_x, text_y])
            pygame.display.flip()
        else:
            screen.blit(self.background_image, [0, 0])
            font = pygame.font.SysFont('Calibri', 75, True, False)
            #screen.fill(white)
            text = font.render("Game Over!", True, black)
            text_rect = text.get_rect()
            text_x = screen.get_width() / 2 - text_rect.width / 2
            text_y = screen.get_height() / 2 - text_rect.height / 2
            screen.blit(text, [text_x, text_y])
            pygame.display.flip()
#Prisoner's lounge needs two doors
#Exit hallway needs to be locked
#Need other doors opened as well as locked
