import pygame,random,sys

class Bloque(pygame.sprite.Sprite):
    def __init__(self,x,y,hp,color):
        pygame.sprite.Sprite.__init__(self) #llamada al constructor de la clase padre
        self.image = pygame.Surface((80,30)) #creacion del sprite
        self.image.fill(color) #da color
        self.rect = self.image.get_rect() #se le da hitbox
        self.rect.x = x #posicionamiento
        self.rect.y = y #posicionamiento
        self.hp = hp #numero de vidas del bloque
        
    def colorear(self,almacen):
        self.hp -=1
        if (self.hp == 1):
            self.image.fill((0,255,0))
        elif (self.hp == 0):
            self.image.fill((255,0,0))
        else:
            pygame.sprite.Sprite.kill(self) #si ya se acabaron las vidas del bloque, se destruye
            almacen.puntaje += 1

class Almacen(Bloque):
    def __init__(self):
        self.puntaje = 0
    
    def generar(self,bloques): #generacion de bloques y coloreado inicial
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

class Pelota(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #llamada al constructor de la clase padre
        self.image = pygame.Surface((25,25)) #creacion del sprite
        self.rect = self.image.get_rect() #se recrea su hitbox
        self.rect.x = 400-self.rect.width #posicionamiento en x
        self.rect.y = 600-self.rect.height-20 #posicionamiento en y
        
    def mover(self,velocidad): #movimiento de la pelota
        self.rect.x += velocidad[0]
        self.rect.y += velocidad[1]
    
    def chocar(self,bloque):
        if (bloque != None):
            bloque.colorear() #efecto del choque

class Barra(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #llamada al constructor de la clase padre
        self.img = pygame.Surface((100,20)) #creacion del sprite
        self.img.fill((100,100,100)) #da color
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
    
    bloques = pygame.sprite.Group() #crea un grupo de Sprites para los bloques
    
    almacen = Almacen()
    almacen.generar(bloques)
    barra = Barra()
    pelota = Pelota()
    
    velocidad = [7,-7]
    
    "vidas = 3"
    
    ejecutando = True
    
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        pelota.mover(velocidad) #movimiento normal de la pelota
        cont=1
        colisiones = pygame.sprite.spritecollide(pelota, bloques, False) #devuelve una lista de colisiones entre la pelota y los bloques
        
        if (pelota.rect.y + pelota.rect.height >= 581): #logica de cambio de direccion si choca con barra
            if (pelota.rect.colliderect(barra.rect)):
                velocidad[1] = -1*velocidad[1]
            else:
                ejecutando = False #si no ha chocado con la barra es porque ya se le fue la bola y ha perdido
                """vidas -= 1
                if (vidas > 0):
                    print("Le quedan " + vidas + ". Presione space para continuar")
                else:"""
                print("Game Over") #convertilo en un mensaje visible en la pantalla
        elif (len(colisiones) >= cont): #si la lista no esta vacia es porq la pelota ha chocado con un bloque
            rnd = random.randint(0,1)
            if (rnd ==0):
                velocidad[0] = -1*velocidad[0]
            velocidad[1] = -1*velocidad[1]
            colisiones[0].colorear(almacen)
            if (almacen.puntaje == 30):
                print("You WIN!!!") #convertilo en un mensaje visible en la pantalla
                ejecutando = False
        
        if ((pelota.rect.x > (800 - pelota.rect.width)) or (pelota.rect.x < 0)):
            velocidad[0] = -1*velocidad[0]
        if (pelota.rect.y < 0):
            velocidad[1] = -1*velocidad[1]
    
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]: #si se presiona la tecla derecha o izquierda se mueve la barra
            barra.mover(-10)
        if keys[pygame.K_RIGHT]:
            barra.mover(10)
            
        """if (vidas > 0) and (keys[pygame.K_SPACE]):
            pelota.rect.x = 400-pelota.rect.width #devolver la pelota a su posicion original en x
            pelota.rect.y = 600-pelota.rect.height-20 #devolver la pelota a su posicion original en y
            barra.rect.x = 400-barra.rect.width #devolver la barra a su posicion original en x
            barra.rect.y = 600-barra.rect.height #devolver la barra a su posicion original en y
            ejecutando = True"""
        
        pantalla.fill((70, 242, 216))
        
        pantalla.blit(barra.img,barra.rect)
        
        pygame.draw.circle(pantalla,(100,100,100),(int(pelota.rect.x + pelota.rect.width/2), int(pelota.rect.y + pelota.rect.height/2)), 20)
        
        bloques.draw(pantalla)
                    
        pygame.display.flip()
        
        reloj.tick(60)
        
if __name__ == "__main__":
    main()
