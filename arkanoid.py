import pygame

class Bloque:
    def __init__(self):
        pass
    pass

class Pelota:
    def __init__(self):
        self.img = pygame.image.load() #se carga la imagen de la pelota
        self.rect = self.img.get_rect() #se recrea su hitbox
        self.rect.x = 400-self.rect.width #posicionamiento en x
        self.rect.y = 600-self.rect.height-20 #posicionamiento en y
    
    def chocar(self):
        pass

class Barra:
    def __init__(self):
        self.img = pygame.image.load("C:/Users/RoniD/Downloads/barra.png") #se carga la imagen de la barra
        self.rect = self.img.get_rect() #se recrea su hitbox
        self.rect.x = 400-self.rect.width #posicionamiento en x
        self.rect.y = 600-self.rect.height #posicionamiento en y
    
    def mover(self,direc):
        if (not (self.rect.x > (800-self.rect.width) and (direc == 10))) or (not((self.rect.x < 0) and (direc ==-10))):
            self.rect.x = self.rect.x + direc #mover la barra
            
            
def main():
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    reloj = pygame.time.Clock()
    
    barra = Barra()
    
    # Preparar el inicio del juego
    
    ejecutando = True
    
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
    
        keys = pygame.key.get_pressed() 
        
        if keys[pygame.K_LEFT]: #si se presiona la tecla derecha o izquierda se mueve la barra
            barra.mover(-10)
        if keys[pygame.K_RIGHT]:
            barra.mover(10)
        
        pantalla.fill(0,0,0)
        pantalla.blit(barra.img,barra.rect)
        pygame.display.flip()
        
        reloj.tick(60)
        
if __name__ == "__main__":
    main()
