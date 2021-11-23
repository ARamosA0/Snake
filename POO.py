import pygame
import random
import time

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

def main():
    pygame.init()
    screen_ancho = 600
    screen_alto = 400
    screen = pygame.display.set_mode((screen_ancho, screen_alto))
    pygame.display.set_caption("SNAKE")
    clock = pygame.time.Clock()
    screen.fill(white)
    

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
               
        ser = serpiente()
        ser.dibujar(screen)
        ser.mover()
        pygame.display.update()
        clock.tick(20)
        

class serpiente:
    def __init__(self):
        self.screen_ancho = 600
        self.screen_alto = 400
        self.x = self.screen_ancho/2 
        self.y = self.screen_alto/2
        self.x_change = 0
        self.y_change = 0
        self.black = black

    def dibujar(self, screen):
        pygame.draw.rect(screen, self.black, [self.x, self.y, 10, 10]) 

    def move_left(self):
        self.x_change = -10
        self.y_change = 0
    def move_right(self):
        self.x_change = 10
        self.y_change = 0
    def move_up(self):
        self.x_change = 0
        self.y_change = -10
    def move_down(self):
        self.x_change = 0
        self.y_change = 10

    def mover(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.serpiente.move_left()
                elif event.key == pygame.K_RIGHT:
                    self.serpiente.move_right()
                elif event.key == pygame.K_DOWN:
                    self.serpiente.move_down()
                elif event.key == pygame.K_UP:
                    self.serpiente.move_up()
        self.x +=self.x_change
        self.y +=self.y_change
        
        
        
       
        
            
class comida:
    pass

class juego(serpiente):
        main()
        

juego1 = juego()

        





    


    




    










