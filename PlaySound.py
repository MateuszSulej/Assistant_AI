import pygame


def playSound(fileName):
    pygame.mixer.init()

    pygame.mixer.music.load(fileName)

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
