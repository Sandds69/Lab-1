# Importing libraries
import pygame
import time
import random

# Initial snake speed
snake_speed = 5
 
# Window size
window_x = 720
window_y = 480
 
# Defining colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
 
# Initialising pygame
pygame.init()
 
# Initialise game window
pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((window_x, window_y))
 
# FPS
fps = pygame.time.Clock()
 
# Snake head
snake_position = [100, 50]
 
# Defining first 4 blocks of snake body
snake_body = [[100, 50], [90, 50], [80, 50],[70, 50]]

# Fruit position
fruit_position = [random.randint(10, 60) * 10, random.randint(10, 30) * 10]

# Is fruit in the game?
fruit_spawn = True
 
# Setting default snake direction
direction = 'RIGHT'
change_to = direction
 
# Initial score
score = 0
level = 1
weight = random.randrange(10, 70, 10)
 
# Displaying Score
def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect() 
    game_window.blit(score_surface, score_rect)

# Displaying level
def show_level(color, font, size):
    # creating font object score_font
    level_font = pygame.font.SysFont(font, size)
    # create the display surface object 
    level_surface = level_font.render('Level : ' + str(level), True, color)
    # create a rectangular object for the text
    level_rect = level_surface.get_rect()
    level_rect.topright = (window_x - 10, 0)
    # displaying text
    game_window.blit(level_surface, level_rect)
 
# Game over function
def game_over():
   
    # creating font
    my_font = pygame.font.SysFont('times new roman', 50)
     
    # creating a text surface
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, RED)
     
    game_over_rect = game_over_surface.get_rect()
     
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
     
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
     
    time.sleep(2)
    pygame.quit()
    quit()

# Foods which are disappearing after some time(timer)
CUSTOM_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CUSTOM_EVENT, 10000)
 
 
# Main Function
while True:


    # handling key events
    for event in pygame.event.get():

        #disapperaing fruit
        if event.type == CUSTOM_EVENT:
            fruit_spawn = False

        if event.type == pygame.QUIT:
            game_over()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
 
    # If two keys pressed simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
 
    # Snake body growing mechanism
    snake_body.insert(0, list(snake_position))
    if (fruit_position[0] <= snake_position[0] < fruit_position[0] + weight) and (fruit_position[1] <= snake_position[1] < fruit_position[1] + weight):
        score += weight
        level = 1 + score // 100
        fruit_spawn = False
        weight = random.randrange(10, 70, 10)
    else:
        snake_body.pop()

    # speed
    snake_speed = level * 20

    # if fruit is not on the map spawn it    
    if not fruit_spawn:
        fruit_position = [random.randint(10, 60) * 10, random.randint(10, 30) * 10]
         
    fruit_spawn = True
    game_window.fill(BLACK)
    
    # drawing
    for pos in snake_body:
        pygame.draw.rect(game_window, GREEN,
                         pygame.Rect(pos[0], pos[1], 10, 10))
        
    pygame.draw.rect(game_window, WHITE, pygame.Rect(
        fruit_position[0], fruit_position[1], weight, weight))
 
    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
 
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
 
    # displaying score continuously
    show_score(WHITE, 'times new roman', 20)
    show_level(WHITE, 'times new roman', 20)

    
 
    # Refresh game screen
    pygame.display.update()
 
    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)