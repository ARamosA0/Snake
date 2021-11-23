#poner un menu para velocidad de la serpiente
#poner un menu para cambiar color


import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 255, 0)
green = (0, 0, 255)

screen_ancho = 500
screen_alto = 300

serp_block = 10
serp_speed = 20

screen = pygame.display.set_mode((screen_ancho, screen_alto))
pygame.display.update()
pygame.display.set_caption("Snake")



clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None , 25)
score_style = pygame.font.SysFont(None, 30)
msg_font_style = pygame.font.SysFont(None, 40)

def score(score):
    numero = score_style.render(str(score), True, black)
    screen.blit(numero, [0, 0])

def serp(serp_block, cuerpo_serp):
    for x in cuerpo_serp:
        pygame.draw.rect(screen, black, [x[0], x[1], serp_block, serp_block]) 
        
        
def mensage(msg, color):
    mensg = font_style.render(msg, True, color)
    screen.blit(mensg, [screen_ancho /4, screen_alto/3])

def mensage_para_inicio(color):
    mensg = msg_font_style.render("SERPIENTE", True, color )
    mensgg = msg_font_style.render("A / Continuar", True, color )
    screen.blit(mensg, [screen_ancho /3, screen_alto/3]) 
    screen.blit(mensgg, [screen_ancho /3.2, screen_alto/2])  

def gameLoop():
    game_over = False
    game_close = False
    mensg_inicio = True

    x1 = screen_ancho/2 
    y1 = screen_alto/2

    x1_change = 0
    y1_change = 0

    comidax = round(random.randrange(0, screen_ancho - serp_block)/10.0)*10.0
    comiday = round(random.randrange(0, screen_alto - serp_block)/10.0)*10.0

    cuerpo_serp = [ ]
    tamaño_serp = 1

    

    while not game_over:
        
        while mensg_inicio == True:
            screen.fill(white)
            mensage_para_inicio( black)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        mensg_inicio = False
                        
        
        while game_close ==True:
            screen.fill(white)
            mensage("Perdiste!  Q / Salir   C / Continuar", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                    
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
        screen.fill(white)

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

gameLoop()
