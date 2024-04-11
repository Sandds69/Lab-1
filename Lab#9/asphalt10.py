# Imports
import pygame, sys
from pygame.locals import *
import random, time, os

# Direction of files
os.chdir("C:\\Users\\Admin\\Desktop\\Пары\\PP-Labs\\Lab#8\\file")
 
# Initialzing 
pygame.init()
 
# Setting up FPS 
FPS = 120
FramePerSec = pygame.time.Clock()
 
# Creating colors
RED   = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0
 
# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Background
background = pygame.image.load("AnimatedStreet.png")
 
# Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Racer")
 
# Setting an enemy car
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

# New class Coin for coins                   
class Coin(pygame.sprite.Sprite):
    def __init__(self, side_length):
        super().__init__() 
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (side_length, side_length))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 20)  

    def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            C1.kill()
            setupCoin()

 
# Setting up Sprites        
P1 = Player()
E1 = Enemy()


 
# Creating Sprites Groups
coins = pygame.sprite.Group()
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1)

# Spawning coin
def setupCoin():
    global C1, length
    if len(coins) == 0:
        length = random.choice([10, 30, 50, 70])
        C1 = Coin(length)
        coins.add(C1)
        all_sprites.add(C1)

 
# Game Loop
while True:
    
    setupCoin()

       
    # Cycles through all events occurring  
    for event in pygame.event.get():  
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0))
    
    # Money score on the right corner
    money = font_small.render(str(COINS), True, BLACK)
    DISPLAYSURF.blit(money, (360,10))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
 
    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    
    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()      
    
    # Picking a coin
    if pygame.sprite.spritecollideany(P1, coins):
          pygame.display.update()
          COINS += length // 10
          C1.kill()
          setupCoin()



    # Respawn coins if they collide with enemy car
    if pygame.sprite.spritecollideany(E1, coins):
          pygame.display.update()
          C1.kill()
          setupCoin()

    # Increase the speed of Enemy when the player earns N coins
    if COINS >= 10: SPEED = 5 + (COINS // 10)
          
         
    pygame.display.update()
    FramePerSec.tick(FPS)