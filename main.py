
# * * IMPORTS 
import tkinter as tk
from tkinter import ttk
import pygame
import os
import random
import pyfiglet
# import time

# TODO (GENERELL): 
# TODO - ADD LEVEL SYSTEM THAT CHANGES LVL AFTER U KILLED SERAIN AMOUNT OF MOBS AND
# TODO   THEN MAKES THE GAME HARDER BY ADDING MORE MONSTERS THAT ARE ALSO FASTER AND 
# TODO   MAKE MORE DMG
# TODO
# TODO - ADD A SHOP, THERE YOU CAN BUY THEN AUTOMATIC TURRETS THAT SHOOT FOR YOU
# TODO   AND STUFF LIKE THAT
# TODO 
# TODO - ADD A KIVY, TK, OR WHATEVER GUI TO THE GAME (ALSO TO THE SHOP I GUESS)
# TODO
# TODO - ADD INSTALLER SCRIPT AND LAUNCHER

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('door', type=int, choices=range(1, 4))

# INITIATE PYGAME
pygame.init()
    
# * * SET VARS
win_height = 400  # RESOLUTION
win_width = 800   # RESOLUTION

win = pygame.display.set_mode((win_width, win_height))  # SET WINDOW
log_cooldown = 50   
log = 0
slowmo_in_ms = 20
dev_mode = False
# ENEMY
ENEMY_COUNT = 3
ENEMY_SPEED_MULTIPLIER = 0.3
# BULLET
GLOBAL_BULLET_SPEED = 5
# TOWER
TOWER_HEALTH = 100
# SHOP 
shop_cooldown = 0

pixel_font = os.path.join("Assets/font", "m5x7.ttf")
pixel_font_path = "Assets/font/m5x7.ttf"

# PLAYER (charakter)
left = [pygame.image.load(os.path.join("Assets/Hero", "L1.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L2.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L3.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L4.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L5.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L6.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L7.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L8.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L9.png"))
        ]
right = [pygame.image.load(os.path.join("Assets/Hero", "R1.png")),
         pygame.image.load(os.path.join("Assets/Hero", "R2.png")),
         pygame.image.load(os.path.join("Assets/Hero", "R3.png")),
         pygame.image.load(os.path.join("Assets/Hero", "R4.png")),
         pygame.image.load(os.path.join("Assets/Hero", "R5.png")),
         pygame.image.load(os.path.join("Assets/Hero", "R6.png")),
         pygame.image.load(os.path.join("Assets/Hero", "R7.png")),
         pygame.image.load(os.path.join("Assets/Hero", "R8.png")),
         pygame.image.load(os.path.join("Assets/Hero", "R9.png"))
         ]
# ENEMY
left_enemy = [pygame.image.load(os.path.join("Assets/Enemy", "L1E.png")),
              pygame.image.load(os.path.join("Assets/Enemy", "L2E.png")),
              pygame.image.load(os.path.join("Assets/Enemy", "L3E.png")),
              pygame.image.load(os.path.join("Assets/Enemy", "L4E.png")),
              pygame.image.load(os.path.join("Assets/Enemy", "L5E.png")),
              pygame.image.load(os.path.join("Assets/Enemy", "L6E.png")),
              pygame.image.load(os.path.join("Assets/Enemy", "L7E.png")),
              pygame.image.load(os.path.join("Assets/Enemy", "L8E.png")),
              pygame.image.load(os.path.join("Assets/Enemy", "L9P.png")),
              pygame.image.load(os.path.join("Assets/Enemy", "L10P.png")),
              pygame.image.load(os.path.join("Assets/Enemy", "L11P.png"))
              ]
right_enemy = [pygame.image.load(os.path.join("Assets/Enemy", "R1E.png")),
               pygame.image.load(os.path.join("Assets/Enemy", "R2E.png")),
               pygame.image.load(os.path.join("Assets/Enemy", "R3E.png")),
               pygame.image.load(os.path.join("Assets/Enemy", "R4E.png")),
               pygame.image.load(os.path.join("Assets/Enemy", "R5E.png")),
               pygame.image.load(os.path.join("Assets/Enemy", "R6E.png")),
               pygame.image.load(os.path.join("Assets/Enemy", "R7E.png")),
               pygame.image.load(os.path.join("Assets/Enemy", "R8E.png")),
               pygame.image.load(os.path.join("Assets/Enemy", "R9P.png")),
               pygame.image.load(os.path.join("Assets/Enemy", "R10P.png")),
               pygame.image.load(os.path.join("Assets/Enemy", "R11P.png"))
               ]

# BULLET
bullet_img_right = pygame.transform.scale(pygame.image.load("Assets/Bullets/bullet_right.png"), (40,40))
bullet_img_left = pygame.transform.scale(pygame.image.load("Assets/Bullets/bullet_left.png"), (40,40))
bullet_img2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Bullets", "light_bullet.png")), (20, 20))

# POWER UP'S
# HEAL
heal_img = pygame.transform.scale(pygame.image.load(
    os.path.join("Assets/Powerups", "heal.png")), (30, 30))

# CASH
cash_img = pygame.transform.scale(pygame.image.load(
    os.path.join("Assets/Powerups", "cash.png")), (30, 30))

# LIVES
lives_img = pygame.transform.scale(pygame.image.load(
    os.path.join("Assets/Powerups", "life.png")), (30, 30))

# DECLARE POWERUP TUPLES
powerup_imgs = (heal_img, cash_img, lives_img)
powerup_types = ("heal", "cash", "lives")

# TOWER 
# tower_img = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Tower.png")), (180, 200)) # TODO: FIND A BETTER ASSET FOR THE TOWER
tower_img = pygame.transform.scale(pygame.image.load("Assets/Tower.png"), (200, 280))

# BACKGROUND
background = pygame.transform.scale(pygame.image.load(
    os.path.join("Assets", "Background.png")), (win_width, win_height)).convert()

# MUSIC AND SOUNDS
coin_sound = pygame.mixer.Sound("Assets/Audio/coin.wav")
level_up_sound = pygame.mixer.Sound("Assets/Audio/level_up.wav")
shoot_sound = pygame.mixer.Sound("Assets/Audio/shoot.wav")

bg_music = pygame.mixer.music.load('Assets/Audio/music.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.07)

# bg_music = pygame.mixer.Sound('Assets/Audio/music.wav')
# bg_music.set_volume(0.2)
# bg_music.play()

# * * DEFINE CHARAKTER / PLAYER CLASS
class charakter: 
    def __init__(self, x, y):
        # WALKS
        self.x = x
        self.y = y
        self.vel_x = 3
        self.default_vel_x = 3
        self.speed = 40
        self.vel_y = 20
        self.face_right = True
        self.face_left = False
        self.STEP_INDEX = 0
        # JUMP
        self.jump = False
        # BULLET
        self.bullets = []
        self.shoot_allow = True
        self.hit_enemy = True
        # COOLDOWN
        self.cooldown_count = 0
        self.cooldown_end = 10
        # HEALTH
        self.health = 100
        self.lives = 1
        self.hitbox = (self.x, self.y, 64, 64)
        self.alive = True
        self.health_multiplier = 3
        # DAMAGE
        self.dmg = 10
        self.rapid_fire = False # IF TRUE THERES NO NEED TO LIFT UP THE SPACEBAR
        # CASH
        self.cash = 0

        # self.health = self.health * self.health_multiplier

    def move_charakter(self, userInput):
        self.vel_x = self.default_vel_x
        self.pickup_powerup()    
        if userInput[pygame.K_d] and self.x <= win_width - 62:
            self.x += self.vel_x
            self.face_right = True
            self.face_left = False
        elif userInput[pygame.K_a] and self.x >= 0:
            self.x -= self.vel_x
            self.face_right = False
            self.face_left = True
        else:
            self.STEP_INDEX = 0

    def draw(self, win):
        self.update_healthbar()
        self.hitbox = (self.x + 19, self.y + 15, 25, 48)
        if dev_mode:
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 1)
        if self.STEP_INDEX >= 45:
            self.STEP_INDEX = 0
        if self.face_left:
            win.blit(left[self.STEP_INDEX//5], (self.x, self.y))
            self.STEP_INDEX += 1
        if self.face_right:
            win.blit(right[self.STEP_INDEX//5], (self.x, self.y))
            self.STEP_INDEX += 1

        # BY DIVIDING THE STEP INDEX INTO 2 AND PUTING THE RESET COUNT TO 45 THE WALK ANIMATION IS 5x
        # THIS IS BECAUSE THERE ARE 9 PICS (5x = 45 PICS) BY THAT YOU HAVE TO DIVIDETHE STEP INDEX BY 5
        # SO YOU PRINT THE RIGHT PICTURES BECAUSE ELSE IT WOULD TRY TO PRINT 45 PICS BUT THERE ONLY 9

    def jump_motion(self, userInput):
        if userInput[pygame.K_w] and self.jump is False:
            self.jump = True

        if self.jump:
            # print("LOG, y: " + str(self.y) + " vel_y: " + str(self.vel_y))
            self.y -= self.vel_y / 2
            self.vel_y -= 1
            self.vel_x = self.vel_x * 2
        if self.vel_y < -20:
            self.jump = False
            self.vel_y = 20
        if self.jump == False:
            self.vel_x = 3.5

    def direction(self):
        if self.face_right:
            return 1
        if self.face_left:
            return -1

    def cooldown(self):
        if self.cooldown_count == self.cooldown_end:
            self.cooldown_count = 0
        elif self.cooldown_count > 0:
            self.cooldown_count += 1

    def shoot(self):
        if not userInput[pygame.K_SPACE]:
            self.shoot_allow = True
            # IF F IS NOT PRESSED THE PLAYER GETS THE PERMISSION TO SHOOT (shoot_allow GETS SET TO TRUE)
            # ELSE HE DONT BECAUSE shoot_allow IS SET TO FALSE AFTER THE PLAYER SHOOTS
        self.hit()
        self.cooldown()
        if userInput[pygame.K_SPACE] and self.cooldown_count == 0 and self.shoot_allow:
            shoot_sound.play()
            if self.rapid_fire == False:
                self.shoot_allow = False
            global GLOBAL_BULLET_SPEED
            bullet = Bullet(self.x, self.y, self.direction())
            self.bullets.append(bullet)
            self.cooldown_count = 1  # STARTS COUNTDOWN
            bullet.bullet_vel = 7
        for bullet in self.bullets:
            if bullet.off_screen():  # IF A BULLET GETS OFFSCREEN, IT GETS REMOVED
                self.bullets.remove(bullet)

            bullet.move()
            bullet.bullet_vel -= (0.01 / bullet.bullet_vel +
                                  bullet.bullet_vel / 40) / 5
            # print("LOG, bullet_vel = " + str(bullet.bullet_vel))

    def hit(self):
        for enemy in enemies:
            for bullet in self.bullets:
                if enemy.hitbox[0]< bullet.x < enemy.hitbox[0] + enemy.hitbox[2] and enemy.hitbox[1] < bullet.y < enemy.hitbox[1] + enemy.hitbox[3]:
                    self.hit_enemy = True
                    enemy.health -= self.dmg
                    # win.blit(str(self.dmg_count), (enemy.x + 50, enemy.y + 50)) 
                    for bullet in self.bullets:
                        self.bullets.remove(bullet)

    def update_healthbar(self):
        # self.health_multiplier = 3
        # if not self.health == (self.health * self.health_multiplier):
        #     self.health = self.health * self.health_multiplier
        
        if self.health < 0:
            self.lives -= 1
            self.health = 100 * self.health_multiplier
        
        if self.health > 100 * self.health_multiplier:
            self.lives += 1
            self.health -= 100 * self.health_multiplier 
        
        if self.health >= 0:
            if self.face_right:
                pygame.draw.rect(win, (255, 0, 0),
                                 (self.x + 15, self.y - 15, 30, 10))
            if self.face_left:
                pygame.draw.rect(win, (255, 0, 0),
                                 (self.x + 15, self.y - 15, 30, 10))

        if self.face_right:
            pygame.draw.rect(win, (0, 255, 0), (self.x + 15,
                             self.y - 15, (self.health / 3)  / self.health_multiplier, 10))
        if self.face_left:
            pygame.draw.rect(win, (0, 255, 0), (self.x + 15,
                             self.y - 15, (self.health / 3) / self.health_multiplier, 10))

    def pickup_powerup(self):
        for powerup in powerups:
            if player.hitbox[0] < powerup.x < player.hitbox[0] + player.hitbox[2] and player.hitbox[1] < powerup.y < player.hitbox[1] + player.hitbox[3] or player.hitbox[0] < powerup.x + 32 < player.hitbox[0] + player.hitbox[2] and player.hitbox[1] < powerup.y < player.hitbox[1] + player.hitbox[3]:
                if powerup.powerup_type == "lives":
                    self.lives += 1
                if powerup.powerup_type == "heal":
                    self.health += 10
                    self.update_healthbar()
                if powerup.powerup_type == "cash":
                    coin_sound.play()
                    cash_rand_nr = random.randrange(1,100,1)
                    print("LOG, cash_rand_nr = ", cash_rand_nr)
                    if cash_rand_nr < 80:
                        cash_add = random.randrange(1,10,1)
                        self.cash += cash_add
                        print("cash add = ", cash_add)
                    elif cash_rand_nr < 99:
                        cash_add = random.randrange(1,50,1)
                        self.cash += cash_add
                        print("cash add = ", cash_add)
                    elif self.cash == 99:
                        cash_add = random.randrange(1000,10000,1)
                        self.cash += cash_add
                        print("cash   add = ", cash_add)
                    elif self.cash == 100:
                        cash_add = random.randrange(100000,1000000,1)
                        self.cash += cash_add
                        print("cash add = ", cash_add)
                powerups.remove(powerup)

# * * DEFINE BULLET CLASS
class Bullet:
    def __init__(self, x, y, direction):
        GLOBAL_BULLET_SPEED
        self.x = x + 15
        self.y = y + 25
        self.direction = direction

    def draw_bullet(self):
        # if self.direction == 1:
        #     win.blit(bullet_img_left, (self.x, self.y))
        # if self.direction == -1:
        #     win.blit(bullet_img_right, (self.x + -4, self.y))
        if self.direction == 1:
            win.blit(bullet_img2, (self.x, self.y))
        if self.direction == -1:
            win.blit(bullet_img2, (self.x + -4, self.y))

    def move(self):
        # IF THE PLAYER IS FACING RIGHT, MOVE BULLET RIGHT (+X)
        if self.direction == 1:
            self.x += GLOBAL_BULLET_SPEED / 1.07

        # IF THE PLAYER IS FACING LEFT, MOVE BULLET LEFT (-X)
        if self.direction == -1:
            self.x -= GLOBAL_BULLET_SPEED / 1.07

    def off_screen(self):
        return not(self.x >= -6 and self.x <= win_width)

# * * DEFINE ENEMY CLASS
class Enemy:
    def __init__(self, x, y, direction):
        # COORDINATES AND WALKING
        self.x = x
        self.y = y
        self.direction = direction
        self.enemy_vel = (random.randrange(64, 128, 1) / 56) * ENEMY_SPEED_MULTIPLIER
        self.STEP_INDEX = 0
        self.move_now = True
        # HEALTH
        self.health = 100
        self.health_multiplier = 1
        self.hitbox = (self.x, self.y, 64, 64)
        # DAMAGE
        self.dmg = 3
        # COOLDOWN
        self.cooldown = 0
        # OTHER
        self.dmg_count = ""

    def step(self):
        if self.STEP_INDEX >= 180:
            self.STEP_INDEX = 0

    def draw(self, win):
        self.step()
        self.update_hitbox()
        self.update_healthbar()
        if self.direction == left:
            win.blit(left_enemy[self.STEP_INDEX//20], (self.x, self.y))
        if self.direction == right:
            win.blit(right_enemy[self.STEP_INDEX//20], (self.x, self.y))
        self.STEP_INDEX += 1

    def hit(self):
        if self.x < 127 and self.cooldown == 0:
            global TOWER_HEALTH
            TOWER_HEALTH -= 1
            self.cooldown = 10
        if player.hitbox[0] < enemy.x + 32 < player.hitbox[0] + player.hitbox[2] and player.hitbox[1] < enemy.y + 32 < player.hitbox[1] + player.hitbox[3]:
            self.move_now = False
            if player.health > 0 and self.cooldown == 0:
                player.health -= self.dmg
                self.cooldown = 10
                if player.health == 0 and player.lives > 0:
                    player.lives -= 1
                    player.health = 30
                elif player.health == 0 and player.lives == 0:
                    player.alive = False
        else:
            self.move_now = True

    def move(self):
        self.hit()
        if self.direction == left and self.move_now and not self.x  < 127:
            self.x -= self.enemy_vel
            self.cooldown = 0
        if self.direction == right and self.move_now:
            self.x += self.enemy_vel
            self.cooldown = 0
        if self.cooldown > 0:
            self.cooldown -= 1

    def off_screen(self):
        return not(self.x >= -50 and self.x <= win_width + 50)

    def update_hitbox(self):
        if self.direction == left:
            self.hitbox = (self.x + 25, self.y + 5, 30, 53)
            if dev_mode:
                pygame.draw.rect(win, (255, 0, 0), self.hitbox, 1 )
        if self.direction == right:
            self.hitbox = (self.x + 10, self.y + 5, 35, 53)
            if dev_mode:
                pygame.draw.rect(win, (255, 0, 0), self.hitbox, 1)

    def update_healthbar(self):
        if self.health >= 0:
            if self.direction == left:
                pygame.draw.rect(win, (255, 0, 0),
                                 (self.x + 25, self.y - 15, 30, 10))
            if self.direction == right:
                pygame.draw.rect(win, (255, 0, 0),
                                 (self.x + 15, self.y - 15, 30, 10))

        if self.direction == left:
            pygame.draw.rect(win, (0, 255, 0), (self.x + 25,
                             self.y - 15, (self.health / 3) * self.health_multiplier, 10))
        if self.direction == right:
            pygame.draw.rect(win, (0, 255, 0), (self.x + 15,
                             self.y - 15, (self.health / 3) * self.health_multiplier, 10)) 

        # if self.direction == left:
        #     pygame.draw.rect(win, (0, 255, 0), (self.x + 25,
        #                      self.y - 15, self.health / 3, 10))       

# * * DEFINE POWERUP CLASS
class Powerup:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.powerup_type = powerup_types[random.randint(0,2)] # TODO: FIX THE POWERUP PROBABILITY SYSTEMMMMMMMMMM
        self.powerup_img = ""
        
    def pick_texture(self):
        if self.powerup_type == "heal":
            self.powerup_img = powerup_imgs[0]
        if self.powerup_type == "cash":
            self.powerup_img = powerup_imgs[1]
        if self.powerup_type == "lives":
            self.powerup_img = powerup_imgs[2]

    def draw(self):
        self.pick_texture()
        win.blit(self.powerup_img, (self.x, self.y)) # DRAW HEAL

    # def pick_type(self):
    #     rand_nr5 = random.randrange(1,100,1)
    #     if rand_nr5 <= 50:
    #         return 1 # CASH
    #         self.powerup_type = 1
    #     elif rand_nr5 <= 80:
    #         return 0 # HEAL
    #         self.powerup_type = 0
    #     elif rand_nr5 <= 90:
    #         return 2 # LIVE
    #         self.powerup_type = 2
    #     self.powerup_type = powerup_types[self.powerup_type_num]

    def spawn(self):
        powerup = Powerup(enemy.x + 32, enemy.y + 30) # SPAWN POWERUP
        powerups.append(powerup)

# * * DEFINE DRAW GAME FUNC
def draw_game():
    
    # rand_nr5 = random.randrange(1,100,1)
    # if rand_nr5 <= 50:
    #     # CASH
    #     powerup_type_num = 1
    # elif rand_nr5 <= 80:
    #     # HEAL
    #     powerup_type_num = 0
    # elif rand_nr5 <= 90:
    #     # LIVE
    #     powerup_type_num = 2
    
    win.fill((0, 0, 0))           # FILL THE SCREEN BLACK
    win.blit(background, (0, 0))  # SHOW BG
    
    # TOWER
    win.blit(tower_img, (-5, 80))

    pygame.draw.rect(win, (255, 0, 0), (40, 160, 100, 10))
    # win.blit(tower_img, (-10, 175))
    pygame.draw.rect(win, (0, 255, 0), (40, 160, TOWER_HEALTH, 10))

    font = pygame.font.Font(pixel_font_path, 18) 
    # font = pygame.font.SysFont(pixel_font, 10)  # SELECT FONT
    tower_health_display = font.render(str(TOWER_HEALTH), True, (0, 0, 0))    # DEFINE LIFE DISPLAY
    win.blit(tower_health_display, (82, 157))    # SHOW LIVE DISPLAY
    
    for powerup in powerups:      # DRAW POWERUPS
        powerup.draw()
    player.draw(win)              # DRAW PLAYER  
    for bullet in player.bullets:
        bullet.draw_bullet()      # DRAW BULLETS
    for enemy in enemies:         # DRAW ENEMIES
        enemy.draw(win)
    font = pygame.font.Font(pixel_font_path, 35)   # SELECT FONT
    lives_display = font.render("Lives: " + str(player.lives), True,
                       (0, 0, 0))    # DEFINE LIFE DISPLAY
    health_display = font.render("Health: " + str(player.health),
                        True, (0, 0, 0))  # DEFINE HEALTH DISPLAY
    cash_display = font.render("Cash: " + str(player.cash) + "$",
                        True, (0, 0, 0))  # DEFINE cash DISPLAY
    win.blit(lives_display, (680, 10))    # SHOW LIVE DISPLAY
    win.blit(health_display, (680, 40))   # SHOW HEALTH DISPLAY
    win.blit(cash_display, (680, 70))     # SHOW CASH DISPLAY

    if player.alive == False:
        win.fill((0,0,0))
        font = pygame.font.SysFont(pixel_font_path, 20)  # SELECT FONT 
        font2 = pygame.font.SysFont(pixel_font_path, 50)  # SELECT FONT     
        game_over_msg = font2.render("GAME OVER", True, (255, 255, 255))    # DEFINE GAME OVER DISPLAY
        game_over_msg2 = font.render("PRESS R TO RESTART", True, (255, 255, 255))   # DEFINE GAME OVER DISPLAY
        game_over_msg3 = font.render(" PRESS ESC TO EXIT", True, (255, 255, 255))   # DEFINE GAME OVER DISPLAY
        textRect = game_over_msg.get_rect()
        textRect.center = (win_width//2, win_height//2 - 30)
        textRect2 = game_over_msg2.get_rect()
        textRect2.center = (win_width//2, win_height//2 + 20)
        textRect3 = game_over_msg2.get_rect()
        textRect3.center = (win_width//2, win_height//2 + 50)
        pygame.draw.rect(win, (255,255,255), pygame.Rect(win_width//4, win_height//4, win_width//4*2, win_height//4*2), 4) # DRAWS A NICE BOX AROUND THE HEADINGS
        win.blit(game_over_msg, textRect)   # SHOW GAME OVER MSG'S
        win.blit(game_over_msg2, textRect2) # 
        win.blit(game_over_msg3, textRect3) #
        if userInput[pygame.K_r]:           # RESETS GAME IF KEY "R" IS PRESSED
            # RESET ALL VARS AND REMOVE BULLETS AND ENEMIES: 
            player.alive = True
            player.health = 30
            player.lives = 1
            for enemy in enemies:
                enemies.remove(enemy)
            for bullet in player.bullets:
                player.bullets.remove(bullet)
            player.x = 250
            player.y = 295
            player.cash = 0
                
        
    for enemy in enemies:
        if enemy.direction == left:
            font2 = pygame.font.SysFont(pixel_font_path, 17)
            enemy_health_display = font2.render(
                str(enemy.health), True, (0, 0, 0))
            win.blit(enemy_health_display, (enemy.x + 32, enemy.y - 15))
        if enemy.direction == right:
            font2 = pygame.font.SysFont(pixel_font_path, 17)
            enemy_health_display = font2.render(
                str(enemy.health), True, (0, 0, 0))
            win.blit(enemy_health_display, (enemy.x + 22.5, enemy.y - 15))

    if player.face_right:
        font2 = pygame.font.SysFont(pixel_font_path, 17)
        player_health_display = font2.render(
            str(player.health), True, (0, 0, 0))
        win.blit(player_health_display, (player.x + 22.5, player.y - 15))
    if player.face_left:
        font2 = pygame.font.SysFont(pixel_font_path, 17)
        player_health_display = font2.render(
            str(player.health), True, (0, 0, 0))
        win.blit(player_health_display, (player.x + 22.5, player.y - 15))


    pygame.time.delay(1)          # WAIT 30 MS
    pygame.display.update()       # UPDATE DISPLAY

# * * DEFINE SHOP FUNC
class Shop:
    def __init__(self):
        self.test = "test"
       
    def start_gui(self):
    
        root = tk.Tk()
        root.geometry("400x400")

        quit_btn = ttk.Button(root, text="Exit", command=root.destroy)
        quit_btn.pack()
    
        update_label = ttk.Label(root)
        update_label.pack()
        update_label.configure(text="UPGRADES")

        level_dmg_btn = ttk.Button(text='damage ', command=lambda: self.level_up("dmg"))
        level_dmg_btn.pack()

        buy_rapid_fire_btn = ttk.Button(text='buy rapid_fire ', command=lambda: self.level_up("rapid_fire")) 
        buy_rapid_fire_btn.pack()

        level_reload_speed_btn = ttk.Button(text='upgrade reload_speed ', command=lambda: self.level_up("reload_speed"))
        level_reload_speed_btn.pack()

        level_speed_btn = ttk.Button(text='upgrade speed', command=lambda: self.level_up("speed"))
        level_speed_btn.pack()

        level_bullet_speed_btn = ttk.Button(text='upgrade bullet_speed', command=lambda: self.level_up("bullet_speed"))
        level_bullet_speed_btn.pack()

        add_cash_btn = ttk.Button(text='ADD CASH', command=lambda: self.add_cash()) 
        add_cash_btn.pack()

        # THX STACK FOR THIS FKN LAMBDA IDEA <3

        cash_tk_var = tk.IntVar()
        cash_tk_var.set(10000)
    
        cash_label = ttk.Label(root)
        cash_label.pack()
        cash_label.configure(textvariable=cash_tk_var)

        cash_tk_var.set(player.cash)

        def update_value():
            cash_tk_var.set(player.cash)
            root.update()
            print("player.cash is", player.cash)
            # time.sleep(1)

        root.update()
        root.after(0, update_value)
        root.mainloop()
        # print("test")

    def level_up(self, atribute):
        if atribute == "dmg" and player.dmg != 30:
            if player.cash >= 10:
                player.dmg += 5
                print("damage is ", player.dmg)
                player.cash -= 10
                level_up_sound.play()

        if atribute == "rapid_fire" and player.rapid_fire == False:
            if player.cash >= 30:
                player.rapid_fire = True
                print("rapid_fire is ", str(player.rapid_fire))
                player.cash -= 30

        if atribute == "reload_speed" and player.cooldown_end > 2:   
            # !BUG BULLETS DOESNT SHOW ANYMORE IF RAPID FIRE IS ENABLED AND COOLDOWN_END IS MAXES IDK WHYYYYY 
            if player.cash >= 10:
                player.cooldown_end -= 1
                print("cooldown_end is ", player.cooldown_end)
                player.cash -= 10

        if atribute == "speed" and player.default_vel_x < 15:
            if player.cash >= 10:
                player.default_vel_x += 3
                print("speed is ", player.default_vel_x)
                player.cash -= 10

        if atribute == "bullet_speed":
            global GLOBAL_BULLET_SPEED
            if GLOBAL_BULLET_SPEED < 15:
                if player.cash >= 10:
                    GLOBAL_BULLET_SPEED += 5
                    print("speed is ", GLOBAL_BULLET_SPEED)
                    player.cash -= 10

    def add_cash(self):
        player.cash += 100

# def update_multiplier(target):
          
# START PLAYER INSTANCE
player = charakter(250, 295)
player.health = player.health * player.health_multiplier

# DECLARE ENEMY ARRAY
enemies = []

for enemy in enemies:
    enemy.health_multiplier = 3
    enemy.health = enemy.health * enemy.health_multiplier


# DECLARE POWERUP ARRAY
powerups = []

# SETS RUN TO TRUE
run = True 

# START SHOP INSTANCE
shop1 = Shop()

# * * MAINLOOP
while run:
    # !BUG kind hard to explain but i got a problem with the enemy health_multiplier
    for enemy in enemies:
        if not enemy.health == (enemy.health * enemy.health_multiplier):
            enemy.health_multiplier = 3
            enemy.health = enemy.health * enemy.health_multiplier
    
    # INPUT
    userInput = pygame.key.get_pressed()

    # QUIT GAME
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if userInput[pygame.K_ESCAPE]:
        run = False

    if not userInput[pygame.K_e]:
        shop_allow = True

    if userInput[pygame.K_e] and shop_allow:
        shop1.start_gui()
        shop_allow = False

    # MOVEMENT
    player.move_charakter(userInput)
    player.jump_motion(userInput)

    # SHOOT
    player.shoot()

    # ENEMY
    if len(enemies) < ENEMY_COUNT:
        enemy = Enemy(750, 300, left)
        enemies.append(enemy)
        
        # !BUG THAT SHIT DOESNT WORK FML
        # if dev_mode == False:
        #     rand_nr = random.randint(0, 1)
        # # rand_nr = 0
        # # rand_nr = 1
        # if rand_nr == 1:
        #     enemy = Enemy(750, 300, left)
        #     enemies.append(enemy)
        # if rand_nr == 0:
        #     enemy = Enemy(-1, 300, right)
        #     enemies.append(enemy)
    for enemy in enemies:
        enemy.move()
        

        if enemy.off_screen():
            enemies.remove(enemy)

    # ENEMY HEALTH
    for enemy in enemies:
        if enemy.health < 1:
            
            rand_nr2 = random.randint(1, 3)  
            if rand_nr2 == 1:
                powerup = Powerup(enemy.x + 32, enemy.y + 30) # SPAWN POWERUP
                powerups.append(powerup)
            else:
                pass
                 
            enemies.remove(enemy)

    # * * DEV MODE
    if userInput[pygame.K_LCTRL] and userInput[pygame.K_d] and dev_mode == False:
        dev_mode = True
        print(pyfiglet.figlet_format("DEV-MODE ACTIVATED"))

    if userInput[pygame.K_LCTRL] and userInput[pygame.K_a] and dev_mode == True:
        dev_mode = False
        print(pyfiglet.figlet_format("DEV-MODE DE-ACTIVATED"))

    # LOG
    if log_cooldown > 0 and dev_mode:
        log_cooldown -= 1
    if userInput[pygame.K_l] and log_cooldown == 0 and dev_mode:
        print("LOG " + str(log))
        log_cooldown = 50
        log += 1
    if userInput[pygame.K_k] and log_cooldown == 0 and dev_mode:
        log_msg = input(":")
        print("LOG " + str(log) + "," + "LOG_MSG: " + log_msg)
        log_cooldown = 50
        log += 1

    # ENEMY SIDE SELECT
    if userInput[pygame.K_n] and dev_mode:
        rand_nr = 0
    if userInput[pygame.K_m] and dev_mode:
        rand_nr = 1

    # SPAWN POWERUP 
    if userInput[pygame.K_y] and dev_mode:
        powerup = Powerup(random.randrange(1,500),320) # SPAWN POWERUP
        powerups.append(powerup)
    
    # SLOWMO
    if userInput[pygame.K_j] and dev_mode:
        pygame.time.delay(int(slowmo_in_ms))
    if userInput[pygame.K_i]:
        slowmo_in_ms += 0.5
        print("LOG, slowmo_in_ms=" + str(int(slowmo_in_ms)))
    if userInput[pygame.K_o]:
        slowmo_in_ms -= 0.5
        print("LOG, slowmo_in_ms=" + str(int(slowmo_in_ms)))

    # ENEMY RESET
    if userInput[pygame.K_b] and dev_mode:
        for enemy in enemies:
            enemies.remove(enemy)

    # HEALTH
    if userInput[pygame.K_c] and dev_mode:
        player.health += 1
    if userInput[pygame.K_v] and dev_mode:
        player.health -= 1

    # LIVES
    if userInput[pygame.K_r] and dev_mode:
        player.lives += 1
    if userInput[pygame.K_t] and dev_mode:
        player.lives -= 1

    # DRAW GAME IN WINDOW
    draw_game()
