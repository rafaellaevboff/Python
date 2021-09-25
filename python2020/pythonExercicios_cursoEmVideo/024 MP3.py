import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('024mp3.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass

#ou pygame.event.wait()