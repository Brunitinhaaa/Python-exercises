import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('D:/ESTUDOS/PYTHON/Python-exercicios/CURSO-EM-VIDEO-EXERCISES/ex026.mp3')

pygame.mixer.music.play()
print("Let's listen to music using Python modules")

while pygame.mixer.music.get_busy(): 
    pygame.time.Clock().tick(10)

print("Music has finished playing!")
