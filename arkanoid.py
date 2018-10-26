import pygame

class Bloque:
    def __init__(self):
        pass
    pass

class Pelota:
    def __init__(self):
        self.imagen = pygame.colo
    
    def chocar(self):
        

class Barra:
    def __init__(self):
        self.img = pygame.image.load() #se carga la imagen de la barra
        self.rect = img.get_rect() #se recrea su hitbox
        self.rect.x = 400-self.rect.width #posicionamiento en x
        self.rect.y = 600-self.rect.height #posicionamiento en y
    
    def mover(self,direc):
        self.rect.x = self.rect.x + direc #cambiar la posicion de la barra
        
            
def main():
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    reloj = pygame.time.Clock()
    
    # Preparar el inicio del juego
    
    ejecutando = True
    
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
    
        keys = pygame.key.get_pressed()
        
        if (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]) #si se presiona la tecla derecha o izquierda se mueve la barra
            barra.mover()
            if not (barra.rect.x > (800-barra.rect.width) or barra.rect.x < 0):
                if (keys[pygame.K_LEFT]):
                    barra.mover(-1) #mueve a la izquierda
                elif (keys[pygame.K_RIGHT]):
                    barra.mover(1) #mueve a la derecha
