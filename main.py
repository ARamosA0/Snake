import pygame, sys
from pygame.locals import *


pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (175,0,0)
green = (34,177,76)
yellow = (175,175,0)
blue = (30,144,255)
light_green = (0,255,0)
light_red = (255,0,0)
light_yellow = (255,255,0)
light_blue = (0,191,255)
grey = (217, 215, 214)


screen_ancho = 500
screen_alto = 300

small = pygame.font.SysFont(None , 25)
medium = pygame.font.SysFont(None, 30)
large = pygame.font.SysFont(None, 40)
title = pygame.font.SysFont(None, 80)


clock = pygame.time.Clock()


screen = pygame.display.set_mode((screen_ancho, screen_alto))
pygame.display.update()
pygame.display.set_caption("ARCADE")

def mensaje_def(msg, color,pos_1, pos_2, tam):
    mesg  = tam.render(msg, True, color)
    screen.blit(mesg, [pos_1, pos_2])


def cargarimagen():
    img = []
    serpiente = img.append(pygame.image.load("Proyectos_python/serpiente/unnamed.png"))
    pacman = img.append(pygame.image.load("Proyectos_python/serpiente/pac-man-1931043.jpg"))



def principal():
    click = False
    while True:
 
        screen.fill(grey)
        mensaje_def("ARCADE", green, 130,  50, title) 
        
       
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(20, 120, 200, 150)
        button_2 = pygame.Rect(280, 120, 200, 150)

        if button_1.collidepoint((mx, my)):
            if click:
                pass
        if button_2.collidepoint((mx, my)):
            if click:
                pass
        pygame.draw.rect(screen, (black), button_1)
        pygame.draw.rect(screen, (black), button_2)
        

 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        clock.tick(30)
    pass


principal()













