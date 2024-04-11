import pygame
pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
x = 400
y = 300
clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    width = screen.get_width()
    height = screen.get_height()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y >= 25: y -= 20
    if pressed[pygame.K_DOWN] and y <= height - 25: y += 20
    if pressed[pygame.K_LEFT] and x >= 25: x -= 20
    if pressed[pygame.K_RIGHT] and x <= width - 25: x += 20


    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)
    pygame.display.flip()
    clock.tick(60)