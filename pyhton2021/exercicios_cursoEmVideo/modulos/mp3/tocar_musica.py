import pygame

pygame.mixer.init()
# iniciar mixer e dps pygame e só depois rodar a música
pygame.init()
pygame.mixer.music.load('ClaraValverde_ChegueiPraFicar.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy(): pass
