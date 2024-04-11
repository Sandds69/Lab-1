from datetime import *
import pygame


pygame.init()

screen = pygame.display.set_mode((700, 525))
done = False

clock = pygame.image.load("mainclock.png")
minuteHand = pygame.image.load("rightarm.png")
secondHand = pygame.image.load("leftarm.png")

clock = pygame.transform.scale(clock, (int(clock.get_width() / 2), int(clock.get_height() / 2)))
minuteHand = pygame.transform.scale(minuteHand, (int(minuteHand.get_width() / 2), int(minuteHand.get_height() / 2)))
secondHand = pygame.transform.scale(secondHand, (int(secondHand.get_width() / 2), int(secondHand.get_height() / 2)))


clockRect = clock.get_rect(center=(350, 262))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    seconds = datetime.now().second
    minutes = datetime.now().minute
    
    secondAngle = seconds * 6
    rotatedSecond = pygame.transform.rotate(secondHand, -secondAngle)
    minuteAngle = minutes * 6
    rotatedMinute = pygame.transform.rotate(minuteHand, -minuteAngle)

    secondRect = rotatedSecond.get_rect(center=clockRect.center)
    minuteRect = rotatedMinute.get_rect(center=clockRect.center)

    screen.fill((255, 255, 255))
    
    screen.blit(clock, clockRect)
    screen.blit(rotatedMinute, minuteRect)
    screen.blit(rotatedSecond, secondRect)

    pygame.display.flip()