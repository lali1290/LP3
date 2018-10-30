import pygame,random,sys

class Bloque(pygame.sprite.Sprite):
    def __init__(self,x,y,hp,color):
        pygame.sprite.Sprite.__init__(self) #llamada al constructor de la clase padre
        self.image = pygame.Surface((80,30)) #creacion del sprite
        self.image.fill(color)
        self.rect = self.image.get_rect() #se le da hitbox
        self.rect.x = x #posicionamiento
        self.rect.y = y #posicionamiento
        self.hp = hp #numero de vidas del bloque
        
    def colorear(self, almacen):
        self.hp -=1
        if (self.hp == 1):
            self.img.fill((0,255,0))
        elif (self.hp == 0):
            self.img.fill((255,0,0))
        else:
            almacen.destruir(self.rect.x,self.rect.y) #si ya se acabaron las vidas del bloque, se destruye

class Almacen(Bloque):
    def __init__(self):
        self.puntaje = 0
    
    def generar(self,bloques): #generacion de bloques
        for j in range(3):
            for i in range(10):
                rnd = random.randint(0,2)
                if (rnd == 2):
                    color = (0,0,255) 
                elif (rnd == 1):
                    color = (0,255,0)
                elif (rnd == 0):
                    color = (255,0,0)
                bloque = Bloque(i*80,j*30,rnd,color)
                bloques.add(bloque)
                
    def destruir(self,x,y):
        self.matriz[x/10][y/10] = None #eliminacion del bloque en la matriz
        self.puntaje = self.puntaje+1
        

class Pelota(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #llamada al constructor de la clase padre
        self.image = pygame.Surface((45,30)) #creacion del sprite
        self.image.fill((100,100,100))
        self.rect = self.image.get_rect() #se recrea su hitbox
        self.rect.x = 400-self.rect.width #posicionamiento en x
        self.rect.y = 600-self.rect.height-20 #posicionamiento en y
        
    def mover(self,velocidad):
        self.rect.x += velocidad[0]
        self.rect.y += velocidad[1]
    
    def chocar(self,bloque):
        if (bloque != None):
            bloque.colorear() #efecto del choque

class Barra(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #llamada al constructor de la clase padre
        self.img = pygame.Surface((100,20)) #creacion del sprite
        self.img.fill((100,100,100))
        self.rect = self.img.get_rect() #se le da hitbox
        self.rect.x = 400-self.rect.width #posicionamiento en x
        self.rect.y = 600-self.rect.height #posicionamiento en y
    
    def mover(self,direc):
        if (not (self.rect.x > (800-self.rect.width) and (direc == 10))) and (not((self.rect.x < 0) and (direc ==-10))):
            self.rect.x = self.rect.x + direc #mover la barra
            
            
def main():
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    reloj = pygame.time.Clock()
    
    bloques = pygame.sprite.Group()
    
    almacen = Almacen()
    almacen.generar(bloques)
    barra = Barra()
    pelota = Pelota()
    
    bloques.add(pelota)
    
    velocidad = [7,-7]
    
    ejecutando = True
    
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        pelota.mover(velocidad) #movimiento normal de la pelota
        
        if (pelota.rect.y + pelota.rect.width == 580): #logica de cambio de direccion si choca con barra
            if (pelota.rect.colliderect(barra.rect)):
                if (velocidad[0] == -7):
                    velocidad[0] = -1*velocidad[0]
                velocidad[1] = -1*velocidad[1]
            else:
                ejecutando = False #si no ha chocado con la barra es porque ya se le fue la bola y ha perdido
                print("Has perdido")
        elif (): #logica de cuando choca con un bloque y determinacion de dicho bloque
            rnd = random.randint(0,1)
            if (rnd ==0):
                velocidad[0] = -1*velocidad[0]
            velocidad[1] = -1*velocidad[1]
            #todo pelota.chocar() #arreglar
            if (almacen.puntaje ==30):
                print("Felicitaciones, a ganado")
                ejecutando = False
        
        if ((pelota.rect.x > (800 - pelota.rect.width)) or (pelota.rect.x < 0)):
            velocidad[0] = -1*velocidad[0]
        if (pelota.rect.y < 0):
            velocidad[1] = -1*velocidad[1]
        
        """if (pelota.rect.colliderect()):
            pelota.chocar() """
    
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]: #si se presiona la tecla derecha o izquierda se mueve la barra
            barra.mover(-10)
        if keys[pygame.K_RIGHT]:
            barra.mover(10)
        
        pantalla.fill((70, 242, 216))
        
        pantalla.blit(barra.img,barra.rect)
        
        bloques.draw(pantalla)
                    
        pygame.display.flip()
        
        reloj.tick(60)
        
if __name__ == "__main__":
    main()
