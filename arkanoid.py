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
            almacen.destruir(self.rect.x,self.rect.y) #si ya se acabaron las vidas del bloque, se destruye

class Almacen(Bloque):
    def __init__(self,puntaje):
        self.matriz = Bloque[10][3]
        self.puntaje = 0
    
    def generar(self): #generacion de bloques
        for j in range(3):
            for i in range(10):
                bloque = Bloque(i*80,j*20,random.randint(0,2))
                self.matriz[i][j] = bloque
                
    def destruir(self,x,y):
        self.matriz[x/10][y/10] = None #eliminacion del bloque en la matriz
        self.puntaje = self.puntaje+1
        

class Pelota(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #llamada al constructor de la clase padre
        self.img = pygame.image.load() #se carga la imagen de la pelota
        self.rect = self.img.get_rect() #se recrea su hitbox
        self.rect.x = 400-self.rect.width #posicionamiento en x
        self.rect.y = 600-self.rect.height-20 #posicionamiento en y
    
    def chocar(self,bloque):
        if (bloque != None):
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
    
    velocidad = [7,-7]
    
    ejecutando = True
    
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        pelota.rect.move(velocidad) #movimiento normal de la pelota
        
        if (pelota.rect.y + pelota.rect.width == 582): #logica de cambio de direccion si choca con barra
            if (pelota.rect.colliderect(barra.rect)):
                if (velocidad[0] == -7):
                    velocidad[0] = -1*velocidad[0]
                velocidad[1] = -1*velocidad[1]
        elif (): #logica de cuando choca con un bloque y determinacion de dicho bloque
            rnd = random.randint(0,1)
            if (rnd ==0):
                velocidad[0] = -1*velocidad[0]
            velocidad[1] = -1*velocidad[1]
            todo pelota.chocar() #arreglar
            if (almacen.puntaje ==30):
                print("Felicitaciones, a ganado")
                ejecutando = False
            
        
        if ((pelota.rect.x > (800 - pelota.rect.width)) or (pelota.rect.x < 0)):
            velocidad[0] = -1*velocidad[0]
        if (pelota.rect.y < 0):
            velocidad[1] = -1*velocidad[1]
        
        if (pelota,rect.colliderect()):
            pelota.chocar()
    
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]: #si se presiona la tecla derecha o izquierda se mueve la barra
            barra.mover(-10)
        if keys[pygame.K_RIGHT]:
            barra.mover(10)
        
        pantalla.fill(0,0,0)
        
        pantalla.blit(pelota.img, pelota.rect)
        pantalla.blit(barra.img,barra.rect)
        
        for j in range(3):
            for i in range(10):
                if (almacen[i][j] != None):
                    pantalla.blit(almacen[i][j].img, almacen[i][j].rect)
                    
        pygame.display.flip()
        
        reloj.tick(60)
        
if __name__ == "__main__":
    main()
