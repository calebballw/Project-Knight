import pygame
import wall1
import player_library
import room_library
import room1_library
import room2_library
import room3_library
import room4_library
import room5_library
import room6_library
import room7_library
import room8_library
import room9_library
import room10_library
import room11_library
import room12_library
import knight_library
import bullet_library
#Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

class Game():
    def __init__(self):
        #Game Functionality
        self.menu_image = pygame.image.load("intro.png")
        self.background_image = pygame.image.load("lava_pit.png").convert()
        self.torture = pygame.image.load("torture_room.jpg").convert()
        self.prince = pygame.image.load("prince_right.png").convert()
        self.bad_dude = pygame.image.load("knightb.png").convert()
        self.game_over = False
        self.lava_over = False
        self.dragon_key_yes = False
        self.wr_key_yes = False
        self.exit_key_yes = False
        self.weapons_yes = False
        self.you_win = False
        self.display_s = True
        self.arrows = 10
        self.game_start = True
        self.inu = 1
        #Main lists
        self.rooms = []
        self.movingsprites = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()
        #Torture Chamber
        self.room = room1_library.Torture_Chamber()
        self.rooms.append(self.room)
        #Dragon Wait Room
        self.room = room2_library.DWR()
        self.rooms.append(self.room)
        #Dragon Cave
        self.room = room3_library.Dragon_Cave()
        self.rooms.append(self.room)
        #Weapons Room
        self.room = room4_library.Weapons_Room()
        self.rooms.append(self.room)
        #Execution Chamber
        self.room = room5_library.Execution_Chamber()
        self.rooms.append(self.room)
        #Hallway
        self.room = room6_library.Hallway()
        self.rooms.append(self.room)
        #Lava Pit
        self.room = room7_library.Lava_Pit()
        self.rooms.append(self.room)
        #First Cell
        self.room = room8_library.First_Cell()
        self.rooms.append(self.room)
        #Exit Hallway
        self.room = room9_library.Exit_Hallway()
        self.rooms.append(self.room)
        #Second Cell
        self.room = room10_library.Second_Cell()
        self.rooms.append(self.room)
        #Prisoner's Lounge
        self.room = room11_library.Prisoner_Lounge()
        self.rooms.append(self.room)
        #Cafeteria
        self.room = room12_library.Cafeteria()
        self.rooms.append(self.room)
        #room setup
        self.current_room_no = 5
        self.current_room = self.rooms[self.current_room_no]
        #Player
        self.player = player_library.Player(300, 50)
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
                    if self.inu == 5:
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
                    self.player.flip("left")
                    self.player.changespeed(-5, 0)
                #Right Arrow Key, Move Right
                elif event.key == pygame.K_RIGHT:
                    self.player.flip("right")
                    self.player.changespeed(5, 0)
                #Up Arrow Key, Move Up
                elif event.key == pygame.K_UP:
                    self.player.flip("up")
                    self.player.changespeed(0, -5)
                #Down Arrow Key, Move Down
                elif event.key == pygame.K_DOWN:
                    self.player.flip("down")
                    self.player.changespeed(0, 5)
                #Spacebar, Shoot Something
                elif event.key == pygame.K_SPACE:
                    if self.weapons_yes == True and self.arrows > 0:
                        self.bullet = bullet_library.Bullet()
                        self.bullet.rect.x = self.player.rect.x + 30
                        self.bullet.rect.y = self.player.rect.y
                        if self.player.image == self.player.princeb:
                            self.bullet.way("up")
                        elif self.player.image == self.player.princef:
                            self.bullet.way("down")
                        elif self.player.image == self.player.princel:
                            self.bullet.way("left")
                        elif self.player.image == self.player.princer:
                            self.bullet.way("right")
                        self.bullet_list.add(self.bullet)
                        self.arrows -= 1
 
            # Reset speed when key goes up
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(5, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.changespeed(-5, 0)
                elif event.key == pygame.K_UP:
                    self.player.changespeed(0, 5)
                elif event.key == pygame.K_DOWN:
                    self.player.changespeed(0, -5)
        return False
    def change_rooms(self, nr):
        #Moves player to the next room
        self.current_room_no = nr
        self.current_room = self.rooms[nr]
    def run_logic(self):
        if not self.game_over and not self.lava_over:
            if self.player.lives <= -100:
                self.game_over = True
            #Makes all the sprites move
            #moves the player
            self.player.update(self.current_room.wall_list, self.current_room.enemy_sprites)
            
            #moves the knights
            self.current_room.enemy_sprites.update()
            
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
            
            #records that you have a key
            if key_hit_list:
                self.wr_key_yes = True
            if dc_key_hit_list:
                self.dragon_key_yes = True
            if eh_key_hit_list:
                self.exit_key_yes = True
            if weapon_hit_list:
                self.weapons_yes = True
                
            #Checks to see if the bullet hit anything
            for bullet in self.bullet_list:
                bullet_hit_list = pygame.sprite.spritecollide(self.bullet, self.current_room.enemy_sprites, True)
                for block in bullet_hit_list:
                    self.bullet_list.remove(self.bullet)
                if self.bullet.rect.y < -10:
                    self.bullet_list.remove(self.bullet)
                    
            #Checks to see if you went up out of the room
            if self.player.rect.y < -15:
                if self.current_room_no == 0:
                    self.change_rooms(1)
                    self.player.rect.y = 600
                elif self.current_room_no == 1:
                    if self.dragon_key_yes == True:
                        self.change_rooms(2)
                        self.player.rect.y = 600
                    else:
                        self.player.rect.y += 50
                elif self.current_room_no == 3:
                    self.player.rect.x = 350
                    self.change_rooms(4)
                elif self.current_room_no == 2:
                    self.change_rooms(7)
                elif self.current_room_no == 7:
                    self.change_rooms(8)
                elif self.current_room_no == 9:
                    self.change_rooms(10)
                elif self.current_room == 8:
                    self.game_over = True
                    self.you_win = True
                if self.current_room_no != 1:
                    self.player.rect.y = 600
                
            #Checks to see if you went down and out of the room
            if self.player.rect.y > 601:
                if self.current_room_no == 1:
                    self.change_rooms(0)
                elif self.current_room_no == 2:
                    self.change_rooms(1)
                elif self.current_room_no == 4:
                    if self.wr_key_yes == True:
                        self.player.rect.x = 550
                        self.change_rooms(3)
                        self.player.rect.y = 0
                    else:
                        self.player.rect.y -= 50
                elif self.current_room_no == 8:
                    self.change_rooms(7)
                    self.player.rect.y = 0
                elif self.current_room_no == 7:
                    if self.dragon_key_yes == True:
                        self.change_rooms(2)
                        self.player.rect.y = 0
                    else:
                        self.player.rect.y -= 50
                elif self.current_room_no == 10:
                    self.change_rooms(9)
                if self.current_room_no != 4 and self.current_room_no != 7:
                    self.player.rect.y = 0
            #Checks to see if you went right and out of the room
            if self.player.rect.x > 790:
                if self.current_room_no == 1:
                    self.change_rooms(4)
                elif self.current_room_no == 7:
                    self.change_rooms(9)
                elif self.current_room_no == 8:
                    self.change_rooms(10)
                elif self.current_room_no == 11:
                    self.change_rooms(8)
                self.player.rect.x = 0
            #Checks to see if you went left and out of the room
            if self.player.rect.x < 0:
                if self.current_room_no == 4:
                    self.change_rooms(1)
                    self.player.rect.x = 790
                elif self.current_room_no == 9:
                    self.change_rooms(7)
                    self.player.rect.x = 790
                elif self.current_room_no == 10:
                    self.change_rooms(8)
                    self.player.rect.x = 790
                elif self.current_room_no == 8:
                    self.change_rooms(11)
                    self.player.rect.x = 790
            #Specific to leaving hallway only
            if self.player.rect.x > 605 and self.player.rect.y > 280:
                if self.current_room_no == 5:
                    self.player.rect.y = 280
                    self.change_rooms(1)
                    self.player.rect.x = 0
            if self.player.rect.x > 605 and self.player.rect.y < 280:
                if self.current_room_no == 5:
                    self.player.rect.y = 280
                    self.change_rooms(7)
                    self.player.rect.x = 0
            if self.player.rect.y > 500:
                if self.current_room_no == 5:
                    self.change_rooms(6)
                    self.player.rect.y = 0
            if self.current_room_no == 6 and self.player.rect.y >= 50:
                self.lava_over = True
            #Specific to entering hallway only
            if self.player.rect.x < 0:
                if self.current_room_no == 1:
                    self.change_rooms(5)
                    self.player.rect.x = 585
                    self.player.rect.y = 360
                elif self.current_room_no == 7:
                    self.change_rooms(5)
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
            #Displays how many lives you have
            font = pygame.font.SysFont('Calibri', 25, True, False)
            text = font.render("Lives:" + str(self.player.lives), True, red)
            screen.blit(text, [150, 350])
            text2 = font.render("Arrows:" + str(self.arrows), True, blue)
            if self.weapons_yes == True:
                screen.blit(text2, [500, 350])
            #flips all this to the screen
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
            elif self.inu == 2:
                text = font.render("Stop! You can't do this!!!", True, black)
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
        