from tkinter import *
largeur = 1000      #largeur de la fenetre
hauteur = 400       #hauteur de la fenetre
Taille_de_la_balle = 10
rfb = 20   #Écart par rapport au mur
rs = 100    #Taille racket
rspeed = 30 #Vitesse de la balle
lplayer = rplayer = 0       #lplayer = Left Player & rplayer = Right Player
x1, y1 = rfb, (hauteur-Taille_de_la_balle)/2
lpos = rpos = (hauteur-rs)/2    #Position racket
nextplayer = 0
playing = 0         #Si playing=0 le jeu est en pause mais si playing=1 la partie/manche commence
compteur = 0

def move():
    global x1, y1, dx, dy, hauteur, largeur, Taille_de_la_balle, rfb, playing
    global rpos, lpos, rs, nextplayer, lplayer, rplayer,compteur
    x1 = x1 + 1 + dx
    y1 = y1 + 1 + dy
    if playing > 0:
        x1, y1 = x1 + dx, (y1 + dy)
    elif nextplayer == 0:
        x1, y1, dx = rfb + 10, lpos + (rs - Taille_de_la_balle) / 2, abs(dx)
    else:
        x1, y1, dx = largeur - rfb - 10, rpos + (rs-Taille_de_la_balle) / 2, -abs(dx)
   #Rebondissement de la balle sur le haut et bas de la fenêtre
    if y1 > hauteur - Taille_de_la_balle:
        y1 = hauteur - Taille_de_la_balle
        dy = -dy
    #Ajoute les points gagnants
    if x1 > (largeur - Taille_de_la_balle):
        lplayer += 1
        x1 = largeur - Taille_de_la_balle
        dx = -dx
        nextplayer = 1
        playing = 0
    #Ajoute les points du joueurs de droite
    if x1 < 0:
        rplayer += 1    #Les points vont de "1" en "1" (si on met "-=1" les scores seront négatifs)
        x1 = 0
        dx = -dx
        nextplayer = 1
        playing = 0
    if y1 < 0:
        y1 = 0
        dy = -dy
    if x1 > largeur - Taille_de_la_balle:
        x1, y1 = rfb, (hauteur / 2)
    if x1 < 0:
        x1, y1 = largeur - rfb, (hauteur / 2)
    if x1 <= rfb and y1 > lpos and y1 < (lpos + rs):
        x1, dx = rfb + 5, -dx
    if x1 >= largeur - rfb - Taille_de_la_balle:
        x1, dx = (largeur - rfb - Taille_de_la_balle - 5), -dx
    can.coords(ovall, x1, y1, x1 + 30, y1 + 30)
    score = f"{str(lplayer)}:{str(rplayer)}"
    can.itemconfigure(compteur, text=f"Joueur 1      {score}       Joueur2")
    can.coords(rracket, largeur - rfb, rpos, largeur - rfb, rpos + rs)      #Taille racket gauche
    can.coords(lracket, rfb, lpos, rfb, lpos + rs)

    win.after(50, move)

def rup(event):         #Mouvement vers le haut de la racket droite ("r" pour Right)
    global rpos, rspeed
    if rpos > rspeed:
        rpos -= rspeed
def rdown(event):       #Mouvement vers le bas de la racket droite
    global rpos, rspeed, hauteur, rs
    if rpos < (hauteur - rs - rspeed):
        rpos += rspeed

def lup(event):         #Mouvement vers le haut de la racket gauche ("l" pour Left)
    global lpos, rspeed
    if lpos > rspeed:
        lpos -= rspeed
def ldown(event):       #Mouvement vers le bas de la racket gauche
    global lpos, rspeed, hauteur, rs
    if lpos < (hauteur - rs - rspeed):
        lpos += rspeed
def rmove(event):       #Restart
    global rpos, hauteur, rs
    ypos = event.y
    if ypos > 0 and ypos < (hauteur - rs):
        rpos = ypos
def startit(event):     #Lancer la partie/la balle
    global playing
    playing = 1
x1 = 0; y1 = 0
dx = 10; dy = 12
win = Tk()      #win = window
win.wm_resizable(0,0) #Bloque la possibilité d'agrandir la fenetre
label = Label(win, text="Bienvenue sur le jeu de Ping Pong (made by Giovannangeli Julien)", fg='black', font="Arial")   #Affiche un text au-dessus du jeu (peut-être changer ça par le score des joueurs)
label.pack()
win.title("Ping & Pong")        #Titre de la fenetre
can = Canvas(win,bg='black',height=hauteur,width=largeur)


can.pack(side = LEFT)
ovall = can.create_oval(x1, y1, x1 + Taille_de_la_balle, y1 + Taille_de_la_balle, width=2, fill='white', outline='red') #Balle
line = can.create_line(largeur/2, 0, largeur/2, hauteur, width=2, fill="white", dash=(4,8))     #Séparation des 2 camps
lracket = can.create_line(rfb, lpos, rfb, lpos + rs, width=10, fill="white")        #Racket Gauche
rracket = can.create_line(largeur - rfb, rpos, largeur - rfb, rpos + rs, width=10, fill="white")        #Racket Droite
font = ('courier', 20)
compteur = can.create_text(largeur / 2, 20, text='0:0' , font="Arial", fill="white")
win.bind('w', lup)      #Bouton pour utiliser la fonction associé (exemple: Appuyer sur la touche "w" pour faire monter la racket gauche vers le haut)
win.bind('s', ldown)    #Idem
win.bind('o', rup)      #Idem
win.bind('l', rdown)    #Idem


win.bind('<B1-Motion>', rmove)  #Restart (la touche assoccié permet de réaliser l'action)           {B1-Motion correspond au mouvement de la souris avec le bouton gauche appuyé}
win.bind('<space>', startit)    #Commencer le jeu (la touche associé permet de réaliser l'action {exemple: Appuyer sur la touche "Espace" pour lancer la balle vers l'adversaire})
move()
win.mainloop()