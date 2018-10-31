import pygame, random
from pygame.locals import *

HEIGHT = 600 
WIDTH = 800
FPS = 60

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Arkanoid")
    reloj = pygame.time.Clock()
    barra = Barra(pantalla, (0, 0, 0))
    pelota = Bola(pantalla, 100, 100, 20, (255, 0, 0))
    almacen = Almacen(pantalla)
    almacen.generacion()

    #ejecutando = True
    while True:
        #Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #ejecutando = False
                pygame.quit()
                sys.exit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            barra.cambio(-10)
        if keys[pygame.K_RIGHT]:
            barra.cambio(10)
        #Updates

        #Renderizado
        pantalla.fill((93, 97, 104))
        almacen.generacion()
        pelota.cambio(barra.rect, True)
        barra.cambio(0)
        pygame.display.flip()
        reloj.tick(FPS)

class Bola:
    def __init__(self, pantalla, x, y, ancho, color):
        self.pantalla = pantalla
        self.x = x
        self.y = y
        self.color = color
        self.ancho = ancho
        self.rect = Rect(x, y, ancho, ancho)
        self.velx = 5
        self.vely = 5
    
    def cambio(self, rectObj, bool):
        self.x += self.velx
        self.y += self.vely
        self.rect = Rect(self.x, self.y, self.ancho, self.ancho)
        pygame.draw.circle(self.pantalla, self.color, (int(self.x), int(self.y)), int(self.ancho/2))
        if self.x < 0 or self.x > WIDTH-self.ancho:    #En caso colisione en algún lado 
            self.velx *= -1
        if self.y < 0:                      #En caso colisione con el borde superior
            self.vely *= -1
        if self.rect.colliderect(rectObj) and bool == True:
            self.vely *= -1
        if self.y > HEIGHT:                 #En caso caiga la bola
            return False

class Bloque:
    def __init__(self, pantalla, x, y, ancho, altura, color):
        self.pantalla = pantalla
        self.x = x
        self.y = y
        self.color = color
        self.ancho = ancho
        self.altura = altura
        self.rect = Rect(x, y, ancho, altura)
    
    def vmBloque(self):
        pygame.draw.rect(self.pantalla, self.color, self.rect)
        

class Almacen(Bloque):
    def __init__(self, pantalla):
        self.pantalla = pantalla
        #self.matriz = Bloque[10][3]

    def generacion(self):                   #Generación de bloques
        for i in range(3):
            for j in range(10):
                bloque = Bloque(self.pantalla, j*80, i*30, 80, 30, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
                bloque.vmBloque()
                #self.matriz[i][j] = bloque

class Barra:
    def __init__(self, pantalla, color):
        self.pantalla = pantalla
        self.ancho = 100
        self.altura = 15
        self.x = 400 - self.ancho
        self.y = 600 - self.altura
        self.color = color
        self.rect = Rect(self.x, self.y, self.ancho, self.altura)
        self.velx = 0

    def cambio(self, velx):
        self.rect = Rect(self.x, self.y, self.ancho, self.altura)
        pygame.draw.rect(self.pantalla, self.color, self.rect)
        if (not (self.x > (800-self.ancho) and (velx == 10))) and (not((self.x < 0) and (velx == -10))):
            self.x += velx          #Variación de la posición


if __name__ == "__main__":
    main()
