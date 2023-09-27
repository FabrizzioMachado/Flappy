import pygame
import random
import pygame.gfxdraw

# Dichiarando l'utilizzazione di pygame.
pygame.init()

# Poner gli immagini
sfondo = pygame.image.load('immagini\\sfondo.png') # Lo sfondo del gioco.
ucellini = pygame.image.load('immagini\\uccello.png') # L'ucello, il protagonista.
perduto = pygame.image.load('immagini\\gameover.png') # Lo schermo di gameover quando ci colpiamo il suolo.
tuboGiu = pygame.image.load('immagini\\tubo.png')
tuboGiu = pygame.transform.scale(tuboGiu, (67, 400))
tuboSu = pygame.transform.flip(tuboGiu, False, True) # Tubo guardando su.
base = pygame.image.load('immagini\\base.png') # Il suolo.

# Costanti
pygame.display.set_caption("Flappy bird")
loschermo = pygame.display.set_mode((1500, 700)) # Dichiarazione del tamagno dello schermo.
perduto = pygame.transform.scale(perduto, (768, 168)) # Lo stesso ma con l'immagine di game over, qui stiamo trasformandola.
gioco = True # Affermando se il gameplay entra.
FPS = 60 # Il numero di FPS, il nome di questa variabile è speciale.
avanzamento = 2 # Dichiarando un numero per l'avvanzamento della base: 2px.

#Il testo sopra
Font = pygame.font.SysFont('Boba Milky', 80, bold= True)
FontBold = pygame.font.SysFont('Boba Milky', 70, bold= True)


# Tutte le classi:
class Tubo:
    def __init__(self, y):
        self.x = 1500  # Posiziona il tubo inizialmente fuori dallo schermo a destra
        self.y = y  # Utilizza la posizione Y specifica passata come argomento
        self.velocita = avanzamento 
    def avanza(self):
        self.x -= avanzamento  # Quando ci troviamo a 298
        # Differenza tra i due tubi (spazio)
        loschermo.blit(tuboGiu, (self.x, self.y+350))
        loschermo.blit(tuboSu, (self.x, self.y-110))

# Tutte le definizioni delle funzioni
def aggiorna(): # Funzione per ponere le nuove funzioni.
    pygame.display.update() # Questi due sono delle principali che lo facciano.
    pygame.time.Clock().tick(FPS) 

def oggetti(): # Variabile.blit significa che stiamo sovrapponendo qualcosa nello schermo.
    loschermo.blit(sfondo, (0,0)) # Sfondo nella posizione predefinita.
    loschermo.blit(ucellini, (ucellinix,ucelliniy)) # L'ucello nella posizione dei valori che l'abbiamo posto.
    for t in tubi:
        t.avanza() 
    loschermo.blit(base, (basex,600)) # Lo stesso ma con la base, aggiungendo 600 px per basso


def inizializza():
    global ucellinix, ucelliniy, ucellini_vely, tubi, basex
    global punti
    ucellinix, ucelliniy = 60, 180
    ucellini_vely = 0
    basex = -100
    tubi = []
    # Il primo tubo:
    for _ in range(1):
        tubi.append(Tubo(random.randint(-40, 110)))   

def collisione(self, ucellinix, ucelliniy):
    global ucellodx, ucellosx, ucellogiu, ucellosu, tubidx, tubisx, tubigiu, tubisu 
    tolleranza = 5
    # Tutte le definizioni delle funzioni
    ucellodx = ucellinix + ucellini.get_width() - tolleranza
    ucellosx = ucellinix
    ucellogiu = ucelliniy
    ucellosu = ucelliniy + ucellini.get_height() - tolleranza

    # Tutte le definizioni delle funzioni
    tubidx = self.x + tuboGiu.get_width()
    tubisx = self.x
    tubigiu = self.y + 350
    tubisu = self.y - 10

    if ucellodx > tubisx and ucellosx < tubidx:
        if ucellosu < tubisu or ucellogiu > tubigiu:
            return True
    return False        
    
def perso():
    loschermo.blit(perduto, (380, 180))
    aggiorna()


inizializza()

while True: 
    if gioco:
        basex -= avanzamento
        if basex < -45: 
            basex = 0
        ucellini_vely += 0.1
        ucelliniy += ucellini_vely

        for tubo in tubi:
            tubo.x -= avanzamento
        
        # Nuovo tubo.
        if tubi[-1].x < 1250:
            tubi.append(Tubo(random.randint(-120, 115))) 

    # Controllo se il personaggio ha toccato il suolo
    if ucelliniy >= 590:
        perso()
        gioco = False
    
    else:
        oggetti()
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ucellini_vely += -2
            elif event.key == pygame.K_r and not gioco:
                inizializza()
                gioco = True
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    aggiorna()