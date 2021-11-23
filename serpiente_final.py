#CAMBIAR COLOR DE SERP
#CAMBIAR VELOCIDAD 

import pygame, sys
import random
from pygame.locals import *

pygame.init()

#COLORES
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

#DIFICULTADES
easy = 20
mediumm = 40
hard = 60


screen_ancho = 500
screen_alto = 300

serp_block = 10


screen = pygame.display.set_mode((screen_ancho, screen_alto))
pygame.display.update()
pygame.display.set_caption("Snake")



clock = pygame.time.Clock()

small = pygame.font.SysFont(None , 25)
medium = pygame.font.SysFont(None, 30)
large = pygame.font.SysFont(None, 40)
title = pygame.font.SysFont(None, 80)




def score(score):
    numero = medium.render(str(score), True, black)
    screen.blit(numero, [0, 0])
 

def serp(serp_block, cuerpo_serp):
    for x in cuerpo_serp:
        pygame.draw.rect(screen, black, [x[0], x[1], serp_block, serp_block]) 
        
        

def mensaje_def(msg, color,pos_1, pos_2, tam):
    mesg  = tam.render(msg, True, color)
    screen.blit(mesg, [pos_1, pos_2])   #El primero es el ancho de [o-500] y el segundo el alto [0-300], las pos inicial es donde inicia el texto
    


def menu_inicio():
    click = False
    while True:
 
        screen.fill(grey)
        mensaje_def("SERPIENTE", green, 100,  100, title) 
       
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(100, 200, 100, 50)
        button_2 = pygame.Rect(300, 200, 100, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                menu_opciones()
        pygame.draw.rect(screen, (black), button_1)
        pygame.draw.rect(screen, (black), button_2)
        mensaje_def("JUGAR", white, 100,  212, large) 
        mensaje_def("DIF", white, 320,  212, large) 
 
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

def menu_opciones():
    running = True
    click = False
    global serp_speed
    while running:
        screen.fill(grey)
 
        mensaje_def("DIFICULTAD", black, 90,  100, title) 
        
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(50, 200, 100, 50)
        button_2 = pygame.Rect(200, 200, 100, 50)
        button_3 = pygame.Rect(350, 200, 100, 50)
        serp_speed = medium
        
        if button_1.collidepoint((mx, my)):
            if click:
                serp_speed =  easy
                running = False
        if button_2.collidepoint((mx, my)):
            if click:
                serp_speed =  mediumm
                running = False
        if button_3.collidepoint((mx, my)):
            if click:
                serp_speed =  hard
                running = False
        pygame.draw.rect(screen, (black), button_1)
        pygame.draw.rect(screen, (black), button_2)
        pygame.draw.rect(screen, (black), button_3)
        mensaje_def("FACIL", white, 60,  212, large) 
        mensaje_def("MEDIO", white, 205,  212, large) 
        mensaje_def("DIFICIL", white, 350,  212, large) 
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
      
            
        
        pygame.display.update()
    
              
    

def game():
    game_over = False
    game_close = False
    mensg_inicio = True
    opciones = False
    

    x1 = screen_ancho/2 
    y1 = screen_alto/2


    x1_change = 0
    y1_change = 0


    comidax = round(random.randrange(0, screen_ancho - serp_block)/10.0)*10.0
    comiday = round(random.randrange(0, screen_alto - serp_block)/10.0)*10.0


    cuerpo_serp = [ ]
    tamaño_serp = 1

    
    while not game_over:                            


        while game_close ==True:
            screen.fill(grey)
            mensaje_def("Perdiste!  Q / Salir   C / Continuar", red, 120,  100, small)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                        menu_inicio()
                    if event.key == pygame.K_c:
                        game()
                    

        for event in pygame.event.get():   
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True           
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -serp_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = serp_block
                    y1_change = 0
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = serp_block
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -serp_block

        if x1 >=screen_ancho or x1 < 0 or y1>=screen_alto or y1 < 0:
            game_close = True

        x1 +=x1_change
        y1 +=y1_change
        screen.fill(grey)

        comida = pygame.draw.rect(screen, black, [comidax, comiday, serp_block, serp_block])
        cabeza_serp = []
        cabeza_serp.append(x1)
        cabeza_serp.append(y1)
        cuerpo_serp.append(cabeza_serp)
        if len(cuerpo_serp) > tamaño_serp:
            del cuerpo_serp[0]

        for x in cuerpo_serp[:-1]:
            if x==cabeza_serp:
                game_close = True


        serp(serp_block, cuerpo_serp)
        score(tamaño_serp -1)
        pygame.display.update()

        if x1 == comidax and y1 == comiday:
            comidax = round(random.randrange(0, screen_ancho - serp_block)/10.0)*10.0
            comiday = round(random.randrange(0, screen_alto - serp_block)/10.0)*10.0
            tamaño_serp = tamaño_serp +1
            
        clock.tick(serp_speed)

    
    

    pygame.quit()
    quit()

menu_inicio()

