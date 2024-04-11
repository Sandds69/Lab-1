import pygame
pygame.init()

screen = pygame.display.set_mode((800, 800))
done = False

font = pygame.font.Font(None, 25)
text = font.render("Control: Play - Space, Pause - Space, Previous song - Left arrow, Next song - Right arrow", True, (255, 255, 255))
music = ["song1.mp3", "song2.mp3"]

def updateInfo():
    global info
    info = font.render(f"Current song: {music[currentSong]}, Paused: {str(isPaused)}", True, (255, 255, 255))

currentSong = 0
isPlaying, isPaused = False, False
updateInfo()



pygame.mixer_music.load(music[currentSong])

def playSong():
    global isPaused, isPlaying, info
    
    if isPlaying: 
        pygame.mixer_music.pause()
        isPlaying = False
        isPaused = True
    else:
        if isPaused: pygame.mixer_music.unpause()
        else: pygame.mixer_music.play()
        isPlaying = True
        isPaused = False
    
    updateInfo()

def nextSong():
    global currentSong, music, isPaused, isPlaying, info
    if currentSong < len(music) - 1: currentSong += 1
    else: currentSong = 0
    isPlaying, isPaused = False, False
    pygame.mixer_music.load(music[currentSong])
    
    playSong()


def previousSong():
    global currentSong, music, isPaused, isPlaying, info
    if currentSong > 0: currentSong -= 1
    else: currentSong = len(music) - 1
    isPlaying, isPaused = False, False
    pygame.mixer_music.load(music[currentSong])
    
    playSong()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            playSong()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            nextSong()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            previousSong()
    
    
    
    screen.fill((0, 0, 0))
    screen.blit(text, (50, 50))
    screen.blit(info, (250, 200))

    pygame.display.flip()