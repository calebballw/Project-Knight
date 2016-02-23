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
        self.menu_image = pygame.image.load("Intro Anthem.png")
        self.display_s = True
        self.game_over = False
        self.key_yes = 0
        self.yoshi_yes = False
        self.light_yes = False
        self.cos = False
        self.gameoverscreen = pygame.image.load("You Win Anthem.png")
        #Main lists
        self.rooms = []
        self.movingsprites = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()
        #Room1
        self.room = room1_library.Room1()
        self.rooms.append(self.room)
        #Room2
        self.room = room2_library.Room2()
        self.rooms.append(self.room)
        #Room3
        self.room = room3_library.Room3()
        self.rooms.append(self.room)
        #Room4
        self.room = room4_library.Room4()
        self.rooms.append(self.room)
        #Room5
        self.room = room5_library.Room5()
        self.rooms.append(self.room)
        #Room6
        self.room = room6_library.Room6()
        self.rooms.append(self.room)
        #room setup
        self.current_room_no = 0
        self.current_room = self.rooms[self.current_room_no]
        #Player
        self.player = player_library.Player(400, 300)
        self.movingsprites.add(self.player)
        
    def display_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.display_s = False
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
        if not self.game_over:
            #Makes all the sprites move
            #moves the player
            self.player.update(self.current_room.wall_list, self.current_room.enemy_sprites)
            
            #moves the knights
            self.current_room.enemy_sprites.update()
            self.current_room.friendly.update("F")
            
            #allows you to pick up the key
            key_hit_list = pygame.sprite.spritecollide(self.player, self.current_room.key_list, True)
            yoshi_hit = pygame.sprite.spritecollide(self.player, self.current_room.friendly, False)
            light_hit_list = pygame.sprite.spritecollide(self.player, self.current_room.light, True)
            light2_hit_list = pygame.sprite.spritecollide(self.player, self.current_room.light2, True)
            
            #makes the bullets move
            self.bullet_list.update()
            
            #records that you have a key
            if key_hit_list:
                self.key_yes += 1
            if yoshi_hit:
                self.yoshi_yes = True
                self.current_room.friendly.update("T")
            if light_hit_list:
                self.light_yes = True
            if light2_hit_list:
                self.cos = True
                
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
                    if self.cos == True:
                        self.change_rooms(2)
                        self.player.rect.y = 600
                    else:
                        self.player.rect.y += 100
                elif self.current_room_no == 4:
                    self.change_rooms(0)
                    self.player.rect.y = 600
                        
                
            #Checks to see if you went down and out of the room
            if self.player.rect.y > 601:
                if self.current_room_no == 1:
                    self.change_rooms(0)
                elif self.current_room_no == 2:
                    self.change_rooms(0)
                elif self.current_room_no == 0:
                    self.change_rooms(4)
                self.player.rect.y = 0
            #Checks to see if you went right and out of the room
            if self.player.rect.x > 801:
                if self.current_room_no == 0:
                    if self.yoshi_yes == True:
                        self.change_rooms(1)
                        self.player.rect.x = 0
                    else:
                        self.player.rect.x -= 100
                elif self.current_room_no == 3:
                    self.change_rooms(0)
                    self.player.rect.x = 0
                elif self.current_room_no == 4:
                    self.change_rooms(5)
                    self.player.rect.x = 0
            #Checks to see if player went left and out of the room
            if self.player.rect.x < -10:
                if self.current_room_no == 1:
                    self.change_rooms(0)
                    self.player.rect.x = 800
                elif self.current_room_no == 0:
                    if self.light_yes == True:
                        self.change_rooms(3)
                        self.player.rect.x = 800
                    else:
                        self.player.rect.x += 100
                elif self.current_room_no == 5:
                    self.change_rooms(4)
                    self.player.rect.x = 800
            #Checks to see if you won
            if self.current_room_no == 2:
                if self.player.rect.y <= 400:
                    self.game_over = True
                    
                
    def display_screen(self, screen):
        if self.display_s == False and not self.game_over:
            #Displays backround image for each room
            screen.blit(self.current_room.background_image, [0, 0])
            #Displays all the sprites and moving objects
            self.movingsprites.draw(screen)
            self.current_room.friendly.draw(screen)
            self.current_room.wall_list.draw(screen)
            self.current_room.enemy_sprites.draw(screen)
            self.current_room.key_list.draw(screen)
            self.bullet_list.draw(screen)
            if self.key_yes == 3:
                self.current_room.light.draw(screen)
            if self.current_room_no == 3:
                if self.player.rect.x <= 600:
                    self.current_room.light2.draw(screen)
            #flips all this to the screen
            pygame.display.flip()
        elif self.display_s == True:
            screen.blit(self.menu_image, [0, 0])
            pygame.display.flip()
        elif self.game_over == True:
            screen.blit(self.gameoverscreen, [0, 0])
            pygame.display.flip()