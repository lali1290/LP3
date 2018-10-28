import pygame,random,sys

class Bloque(pygame.sprite.Sprite):
    def __init__(self,x,y,cont):
        pygame.sprite.Sprite.__init__(self) #llamada al constructor de la clase padre
        self.img = pygame.Surface([80,20]) #creacion del sprite
        self.rect = self.img.get_rect() #se le da hitbox
        self.rect.x = x #posicionamiento
        self.rect.y = y #posicionamiento
        self.cont = cont #numero de vidas del bloque
        
    def colorear(self, almacen):
        self.cont -=1
        if (self.cont == 2):
            self.img.fill(0,0,255) 
        elif (self.cont == 1):
            self.img.fill(0,255,0)
        elif (self.cont == 0):
            self.img.fill(255,0,0)
        else:
            almacen.destruir(self.rect.x,self.rect.y)
        

class Almacen(Bloque):
    def __init__(self):
        self.matriz = Bloque[10][3]
    
    def generar(self): #generacion de bloques
        for j in range(3):
            for i in range(10):
                bloque = Bloque(i*80,j*20,random.randint(0,2))
                self.matriz[i][j] = bloque
                
    def destruir(self,x,y):
        self.matriz[x/10][y/10] = None #eliminacion del bloque en la matriz
        

class Pelota(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #llamada al constructor de la clase padre
        self.img = pygame.image.load() #se carga la imagen de la pelota
        self.rect = self.img.get_rect() #se recrea su hitbox
        self.rect.x = 400-self.rect.width #posicionamiento en x
        self.rect.y = 600-self.rect.height-20 #posicionamiento en y
    
    def chocar(self,bloque):
        #logica para q cambie de direccion
        bloque.colorear() #efecto del choque

class Barra(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #llamada al constructor de la clase padre
        self.img = pygame.Surface([45,20]) #creacion del sprite
        self.rect = self.img.get_rect() #se le da hitbox
        self.rect.x = 400-self.rect.width #posicionamiento en x
        self.rect.y = 600-self.rect.height #posicionamiento en y
    
    def mover(self,direc):
        if (not (self.rect.x > (800-self.rect.width) and (direc == 10))) or (not((self.rect.x < 0) and (direc ==-10))):
            self.rect.x = self.rect.x + direc #mover la barra
            
            
def main():
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    reloj = pygame.time.Clock()
    
    almacen = Almacen()
    almacen.generar()
    barra = Barra()
    pelota = Pelota()
    
    # Preparar el inicio del juego
    
    ejecutando = True
    
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if () #hacer un collision detect 
    
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
