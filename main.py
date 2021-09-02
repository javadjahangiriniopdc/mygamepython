from random import randint
from time import sleep

import pygame

pygame.init()
display = pygame.display.set_mode((500, 500))
run = True
x = 240
y = 200
pygame.mixer.music.load("world-m.ogg")
pygame.mixer.music.play()
myfont = pygame.font.Font('arial.ttf', 60)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.mixer.music.stop()
    display.fill((0, 0, 0))
    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)
    x = randint(0, 500)
    y = randint(0, 500)

    pygame.draw.circle(display, (R, G, B), (400, 300), 40, 5)
    pygame.draw.rect(display, (255, 0, 0), (x, y, 40, 40))

    text = myfont.render('text', False, (R, G, B))
    display.blit(text, (x, y))

    sleep(.001)
    pygame.display.update()
pygame.quit()
