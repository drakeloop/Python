#Faça um programa no python que reproduza arquivos mp3.

import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('exs021raizforte.mp3')
pygame.mixer_music.play()
pygame.event.wait()

#todo teste não deu certo, seguindo adiante para otimizar tempo.
