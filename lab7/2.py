import pygame

pygame.init()

songs = ['C:\programmingFORbss\pp2\pp2-21B030328\lab7\sounds\lab7_musics_music_gta.mp3', 'C:\programmingFORbss\pp2\pp2-21B030328\lab7\sounds\canyekyey feat Leomart - а ты думала.mp3', 'C:\programmingFORbss\pp2\pp2-21B030328\lab7\sounds\gustavo-santaolalla-the-last-of-us.mp3', 'C:\programmingFORbss\pp2\pp2-21B030328\lab7\sounds\got8.mp3']
background = ['C:\programmingFORbss\pp2\pp2-21B030328\lab7\images\gta_background.jpg', 'C:\programmingFORbss\pp2\pp2-21B030328\lab7\images\canyekyey.jpg','C:\programmingFORbss\pp2\pp2-21B030328\lab7\images\The last of us.jpg', 'C:\programmingFORbss\pp2\pp2-21B030328\lab7\images\GOT.jpg']
screen = pygame.display.set_mode((900, 720))
running = True
gta_background = pygame.image.load('C:\programmingFORbss\pp2\pp2-21B030328\lab7\images\gta_background.jpg')
canyekyey = pygame.image.load('C:\programmingFORbss\pp2\pp2-21B030328\lab7\images\canyekyey.jpg')
res_canyekyey = pygame.transform.scale(canyekyey, (720,720))
tlou = pygame.image.load('C:\programmingFORbss\pp2\pp2-21B030328\lab7\images\The last of us.jpg')
res_tlou = pygame.transform.scale(tlou,(720,720))
got = pygame.image.load('C:\programmingFORbss\pp2\pp2-21B030328\lab7\images\GOT.jpg')
res_got = pygame.transform.scale(got,(720,720))
Pause = False
current_song = 0
pygame.display.set_caption('Music')
font = pygame.font.SysFont("comicsansms", 72)
text = font.render("Press ENTER", True, 'Red')
screen.blit(text, (200, 300))


def change(current_song):
    global songs
    global screen
    pygame.mixer.music.load(songs[current_song])
    if songs[current_song] == 'C:\programmingFORbss\pp2\pp2-21B030328\lab7\sounds\got8.mp3':
        screen = pygame.display.set_mode((720, 720))
        screen.blit(res_got, (0, 0))
        pygame.mixer.music.play(0)
    if songs[current_song] == 'C:\programmingFORbss\pp2\pp2-21B030328\lab7\sounds\canyekyey feat Leomart - а ты думала.mp3':
        screen = pygame.display.set_mode((720, 720))
        screen.blit(res_canyekyey, (0, 0))
        pygame.mixer.music.play(0)
    if songs[current_song] == 'C:\programmingFORbss\pp2\pp2-21B030328\lab7\sounds\lab7_musics_music_gta.mp3':
        screen = pygame.display.set_mode((900, 720))
        screen.blit(gta_background, (0, 0))
        pygame.mixer.music.play(0)
    if songs[current_song] == 'C:\programmingFORbss\pp2\pp2-21B030328\lab7\sounds\gustavo-santaolalla-the-last-of-us.mp3':
        screen = pygame.display.set_mode((720, 900))
        screen.blit(res_tlou, (0, 0))
        pygame.mixer.music.play(0)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_song -= 1
                if current_song < 0:
                    current_song = len(songs) - 1
                change(current_song)
            if event.key == pygame.K_RIGHT:
                current_song += 1
                if current_song > len(songs) -1:
                    current_song = 0
                change(current_song)
            if event.key == pygame.K_RETURN: change(current_song=0)
            if event.key == pygame.K_SPACE:
                Pause = not Pause
                if Pause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

    pygame.display.flip()