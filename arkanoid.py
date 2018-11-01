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
        
    def colorear(self,pelota):
        self.hp -=1
        if (self.hp == 1):
            self.image.fill((0,255,0))
        elif (self.hp == 0):
            self.image.fill((255,0,0))
        else:
            pygame.sprite.Sprite.kill(self) #si ya se acabaron las vidas del bloque, se destruye
            pelota.puntaje += 1

class Almacen(Bloque):
    def __init__(self):
        pass
    
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
        self.velocidad = [7,-7]
        self.vidas = 3
        self.ejecutando = True
        self.puntaje = 0
        
    def posicionar(self):
        self.rect.x = 400-self.rect.width #posicionamiento en x
        self.rect.y = 600-self.rect.height-20 #posicionamiento en y
        
    def mover(self,barraRect): #movimiento de la pelota
        self.rect.x += self.velocidad[0]
        self.rect.y += self.velocidad[1]
        
        if (self.rect.y + self.rect.height >= 581): #logica de cambio de direccion si choca con barra
            if (self.rect.colliderect(barraRect)):
                self.velocidad[1] = -1*self.velocidad[1]
            else:
                self.ejecutando = False #si no ha chocado con la barra es porque ya se le fue la bola y ha perdido
                self.vidas -= 1
                if (self.vidas > 0):
                    """texto = "Le quedan " + str(vidas) + ". Presione space para continuar"
                    texto = fuente.render(texto, True, (0,0,0))
                    pantalla.blit(texto, (400,300))"""
                    print("Le quedan " + str(self.vidas) + ". Presione space para continuar")
                else:
                    print("Game Over") #convertilo en un mensaje visible en la pantalla
        
        if ((self.rect.x >= (800 - self.rect.width)) or (self.rect.x <= 0)): #si la pelota se trata de salir por un costado, se le cambia la direccion de movimiento
            self.velocidad[0] = -1*self.velocidad[0]
        if (self.rect.y < 0):
            self.velocidad[1] = -1*self.velocidad[1]
        
    def chocar(self,colisiones):
            rnd = random.randint(0,1)
            if (rnd ==0):
                self.velocidad[0] = -1*self.velocidad[0]
            self.velocidad[1] = -1*self.velocidad[1]
            colisiones[0].colorear(self)
            if (self.puntaje == 30):
                """texto = fuente.render("You WIN!!!", False, (255,0,0))
                pantalla.blit(texto, (400,300)) #arreglar """
                print("You WIN!!!") #convertilo en un mensaje visible en la pantalla
                #ejecutando = False

class Barra(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #llamada al constructor de la clase padre
        self.img = pygame.Surface((100,20)) #creacion del sprite
        self.img.fill((100,100,100)) #da color
        self.rect = self.img.get_rect() #se le da hitbox
        
    def posicionar(self):
        self.rect.x = 400-self.rect.width #posicionamiento en x
        self.rect.y = 600-self.rect.height #posicionamiento en y
    
    def mover(self,direc):
        if (not (self.rect.x > (800-self.rect.width) and (direc == 10))) and (not((self.rect.x < 0) and (direc ==-10))):
            self.rect.x = self.rect.x + direc #mover la barra
            
            
def main():
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    reloj = pygame.time.Clock()
    fuente = pygame.font.SysFont('Comic Sans MS', 200)
    
    bloques = pygame.sprite.Group() #crea un grupo de Sprites para los bloques
    
    almacen = Almacen()
    almacen.generar(bloques)
    barra = Barra()
    pelota = Pelota()
    
    while (pelota.vidas >= 1) and (pelota.puntaje != 30):
        pelota.ejecutando = True
        pelota.posicionar() #iniciar la posicion de la pelota
        barra.posicionar() #iniciar la posicion de la barra
        
        while pelota.ejecutando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            pelota.mover(barra.rect) #movimiento normal de la pelota
            colisiones = pygame.sprite.spritecollide(pelota, bloques, False) #devuelve una lista de colisiones entre la pelota y los bloques
            
            if (len(colisiones) >= 1): #si la lista no esta vacia es porq la pelota ha chocado con un bloque
                pelota.chocar(colisiones)
            
            """
            if (pelota.rect.y + pelota.rect.height >= 581): #logica de cambio de direccion si choca con barra
                if (pelota.rect.colliderect(barra.rect)):
                    pelota.velocidad[1] = -1*pelota.velocidad[1]
                else:
                    ejecutando = False #si no ha chocado con la barra es porque ya se le fue la bola y ha perdido
                    vidas -= 1
                    if (vidas > 0):
                        texto = "Le quedan " + str(vidas) + ". Presione space para continuar"
                        texto = fuente.render(texto, True, (0,0,0))
                        pantalla.blit(texto, (400,300))
                        print("Le quedan " + str(vidas) + ". Presione space para continuar")
                    else:
                        print("Game Over") #convertilo en un mensaje visible en la pantalla
            elif (len(colisiones) >= 1): #si la lista no esta vacia es porq la pelota ha chocado con un bloque
                rnd = random.randint(0,1)
                if (rnd ==0):
                    pelota.velocidad[0] = -1*pelota.velocidad[0]
                pelota.velocidad[1] = -1*pelota.velocidad[1]
                colisiones[0].colorear(almacen)
                if (almacen.puntaje == 30):
                    texto = fuente.render("You WIN!!!", False, (255,0,0))
                    pantalla.blit(texto, (400,300)) #arreglar
                    print("You WIN!!!") #convertilo en un mensaje visible en la pantalla
                    #ejecutando = False
            
            
            if ((pelota.rect.x >= (800 - pelota.rect.width)) or (pelota.rect.x <= 0)): #si la pelota se trata de salir por un costado, se le cambia la direccion de movimiento
                pelota.velocidad[0] = -1*pelota.velocidad[0]
            if (pelota.rect.y < 0):
                pelota.velocidad[1] = -1*pelota.velocidad[1]
            """
        
            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_LEFT]: #si se presiona la tecla derecha o izquierda se mueve la barra
                barra.mover(-10)
            if keys[pygame.K_RIGHT]:
                barra.mover(10)
            
            pantalla.fill((70, 242, 216))
            
            pantalla.blit(barra.img,barra.rect)
            
            pygame.draw.circle(pantalla,(100,100,100),(int(pelota.rect.x + pelota.rect.width/2), int(pelota.rect.y + pelota.rect.height/2)), 15)
            
            bloques.draw(pantalla)
                        
            pygame.display.flip()
            
            reloj.tick(60)
        
if __name__ == "__main__":
    main()
