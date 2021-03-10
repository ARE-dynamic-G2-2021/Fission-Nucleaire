import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

from tkinter import *

LARGEUR = 1000
HAUTEUR = 850

RAYON = 10
n=50
SPEED=5
LARGEUR = 1000
HAUTEUR = 850

RAYON = 10
n=50
SPEED=5

# Creation de la fenetre principale
root = tk.Tk()
root.geometry("1500x900")
root.title("La magnifique fission nucleaire")
myframe = Frame(root)
myframe.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

leftframe = Frame(root)
leftframe.pack( side = LEFT )

rightframe = Frame(root)
rightframe.pack( side = RIGHT )

# Creation d'un widget Canvas
Canevas = tk.Canvas(leftframe,height=HAUTEUR,width=LARGEUR,bg='white')
Canevas.pack(padx=5,pady=5)

#creation des parametres

label = Label(rightframe, text = "Parametres") #label
label.pack(pady = 10, padx = 100)

#le button pour choisir le nombre des atomes initials
def sel():
    n = var.get()
    
    #LES CHOSES QUI SONT DANS LE CANEVAS
    # position initiale des balles
    X = []
    Y = []
    for i in range(n):
        X.append(LARGEUR*np.random.rand())
        Y.append(HAUTEUR*np.random.rand())

    # direction initiale des balles
    DX = []
    DY = []
    for i in range(n):
        angle = 2*np.pi*np.random.rand()
        DX.append(np.cos(angle))
        DY.append(np.sin(angle))

    # Creation d'un objet graphique
    Balle=[]
    for i in range(n):
        Balle.append(Canevas.create_oval(X[i]-RAYON,Y[i]-RAYON,X[i]+RAYON,Y[i]+RAYON,width=1,fill='coral4'))

#Création d'un widget vitesse
    speed = tk.StringVar()
    speed.set(SPEED)
    widget_speed = tk.Scale(rightframe,from_=0,to=30,resolution=1,orient=tk.HORIZONTAL,\
    length=300,width=20,label="Vitesse",tickinterval=0.2,variable=speed)#,command=maj)
    widget_speed.pack(padx=100,pady=10)

    def deplacement():
        """ Deplacement de la balle """
        for i in range(n):
            dx=DX[i]*float(speed.get())
            dy=DY[i]*float(speed.get())
        # rebond a droite
            if X[i]+RAYON+dx > LARGEUR:
                X[i] = 2*(LARGEUR-RAYON)-X[i]
                DX[i] = -DX[i]
        # rebond a gauche
            if X[i]-RAYON+dx < 0:
                X[i] = 2*RAYON-X[i]
                DX[i] = -DX[i]
        # rebond en bas
            if Y[i]+RAYON+dy > HAUTEUR:
                Y[i] = 2*(HAUTEUR-RAYON)-Y[i]
                DY[i] = -DY[i]
        # rebond en haut
            if Y[i]-RAYON+dy < 0:
                Y[i] = 2*RAYON-Y[i]
                DY[i] = -DY[i]
            X[i] = X[i]+DX[i]*float(speed.get())
            Y[i] = Y[i]+DY[i]*float(speed.get())
        # affichage
            Canevas.coords(Balle[i],X[i]-RAYON,Y[i]-RAYON,X[i]+RAYON,Y[i]+RAYON)
    # mise a jour toutes les 50 ms
        root.after(50,deplacement)

    deplacement()

var = IntVar()
scale = Scale(rightframe, from_=1,to=100, resolution=1, orient=tk.HORIZONTAL, length=300,width=20, \
              label="Number of atoms",tickinterval=0.2, variable = var)
scale.pack(padx=100, pady=10)

button = Button(rightframe, text="Set", command=sel)
button.pack(padx=100, pady=10)

def restart():
    n = 0
    X = []
    Y = []
    DX = []
    DY = []

button = Button(rightframe, text="Restart", command=restart)
button.pack(padx=100, pady=10)
#print(n)

mybutton = Button(rightframe, text = "LANCER DANGER", activebackground = "coral4", bg = "coral3") #button pour lancer le neutron
mybutton.pack(pady = 10, padx = 100)

root.mainloop()
