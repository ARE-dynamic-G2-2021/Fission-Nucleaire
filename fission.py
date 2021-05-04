import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import threading

LARGEUR, HAUTEUR = 1000,850

RAYON, NRAYON = 7, 2 #rayon de l'atome et du neutron
CLICK = 0 #variable pour restart
MOVE = 0 #variable pour bouger le neutron
n, nn = 0, 1 #nombre des atoms et des neutrons
SPEED, NSPEED = 5, 15 #okay this is easy to guess

X,Y = [],[]
DX,DY = [],[] 
NX, NY = [], []
NDX, NDY = [], []
Balle, Neutron = [], []

energie = 0

# Creation de la fenetre principale
root = Tk()
root.geometry("1500x900")
root.title("Nuclear fission")
myframe = Frame(root)
myframe.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

leftframe = Frame(root)
leftframe.pack( side = LEFT )

rightframe = Frame(root)
rightframe.pack( side = RIGHT )

# Creation d'un widget Canvas
Canevas = Canvas(leftframe,height=HAUTEUR,width=LARGEUR,bg='white')
Canevas.pack(padx=5,pady=5)

def estDansAtome(ax, ay, nx, ny):
    if(nx >= ax-RAYON and nx<= ax+RAYON and ny >= ay-RAYON and ny<= ay+RAYON):
        return True
    return False

def actualiserCollision():
    global X, Y, DX, DY, n, NX, NY, NDX, NDY, nn, Neutron, Balle, Canevas, energie, texte
    #return 
    i = 0
    j = 0
    
    while(i<nn):
        while(j<n):
            if estDansAtome(X[j], Y[j], NX[i], NY[i]):
                nn += 2
                energie = energie + 193
                texte.configure(text="Compteur : "+ str(energie) + "MeV")
                texte.update()
                for l in range(2):
                    NX.append(X[j])
                    NY.append(Y[j])
                    angle = 2*np.pi*np.random.rand()
                    NDX.append(np.cos(angle))
                    NDY.append(np.sin(angle))
                    k=len(NX)-1
                    Neutron.append(Canevas.create_oval(NX[k]-NRAYON,NY[k]-NRAYON,NX[k]+NRAYON,NY[k]+NRAYON,width=1,fill='yellow'))
                    
                X.pop(j)
                Y.pop(j)
                DX.pop(j)
                DY.pop(j)
                Canevas.delete(Balle[j])
                Balle.pop(j)
                
                n-=1         
            j+=1

        i+=1
        j=0
    return
    
def deplacement():
        global root, X, Y, DX, DY, n, NX, NY, NDX, NDY, nn, Neutron, Balle, Canevas, CLICK, MOVE, energie
        #restart the simulation and exit the function
        if CLICK == 1: 
            Canevas.delete("all")
            MOVE = 0
            CLICK = 0
            n, nn = 0, 1
            energie = 0
            texte.configure(text="Compteur : "+ str(energie) + "MeV")
            texte.update()
            return
    
        """ Deplacement des atoms"""
        for i in range(n):
            dx=DX[i]*float(SPEED)
            dy=DY[i]*float(SPEED)
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
            X[i] = X[i]+DX[i]*float(SPEED)
            Y[i] = Y[i]+DY[i]*float(SPEED)
        
        """Deplacement du neutron si le button est appuye"""
        if MOVE == 1:
            for i in range(nn):
                dx=NDX[i]*float(NSPEED)
                dy=NDY[i]*float(NSPEED)
            # rebond a droite
                if NX[i]+NRAYON+dx > LARGEUR:
                    NX[i] = 2*(LARGEUR-NRAYON)-NX[i]
                    NDX[i] = -NDX[i]
            # rebond a gauche
                if NX[i]-NRAYON+dx < 0:
                    NX[i] = 2*NRAYON-NX[i]
                    NDX[i] = -NDX[i]
            # rebond en bas
                if NY[i]+NRAYON+dy > HAUTEUR:
                    NY[i] = 2*(HAUTEUR-NRAYON)-NY[i]
                    NDY[i] = -NDY[i]
            # rebond en haut
                if NY[i]-NRAYON+dy < 0:
                    NY[i] = 2*NRAYON-NY[i]
                    NDY[i] = -NDY[i]
                NX[i] = NX[i]+NDX[i]*float(NSPEED)
                NY[i] = NY[i]+NDY[i]*float(NSPEED)
            
            actualiserCollision()
            for i in range(nn):
                Canevas.coords(Neutron[i],NX[i]-NRAYON,NY[i]-NRAYON,NX[i]+NRAYON,NY[i]+NRAYON)
 
            
        # affichage des atomes
        for i in range(n):
            Canevas.coords(Balle[i],X[i]-RAYON,Y[i]-RAYON,X[i]+RAYON,Y[i]+RAYON)
        
        # mise a jour toutes les 50 ms
        root.after(50,deplacement)



def sel():
    global X, Y, DX, DY, n, Canevas, Balle, CLICK, MOVE, Neutron, nn, NX, NY, NDX, NDY
    
    CLICK = 0 
    MOVE = 0
    n = var.get() #get the number of atoms from the user
    #LES CHOSES QUI SONT DANS LE CANEVAS
    # position initiale des atomes
    X = []
    Y = []
    for i in range(n):
        X.append(LARGEUR*np.random.rand())
        Y.append(HAUTEUR*np.random.rand())
    
    # direction initiale des atomes
    DX = []
    DY = []
    for i in range(n):
        angle = 2*np.pi*np.random.rand()
        DX.append(np.cos(angle))
        DY.append(np.sin(angle))
        
    # Creation de n atomes
    Balle=[]
    for i in range(n):
        Balle.append(Canevas.create_oval(X[i]-RAYON,Y[i]-RAYON,X[i]+RAYON,Y[i]+RAYON,width=1,fill='coral4'))
 
    # position initiale du neutron
    NX = []
    NY = []
    
    NX.append(LARGEUR-5)
    NY.append(HAUTEUR*np.random.rand())
    
    # direction initiale du neutron
    NDX = []
    NDY = []
    
    angle = 2*np.pi*np.random.rand()
    NDX.append(np.cos(angle))
    NDY.append(np.sin(angle))
    
    # Creation d'un neutron
    Neutron=[]
    Neutron.append(Canevas.create_oval(NX[0]-NRAYON,NY[0]-NRAYON,NX[0]+NRAYON,NY[0]+NRAYON,width=1,fill='yellow'))
    
    deplacement()

def restart():
    global CLICK
    CLICK = 1
    
def clicked():
    global MOVE
    MOVE = 1
   
""" creation des parametres """
label = Label(rightframe, text = "Parametres", bg = "white", bd = 5) #label
label.config( width = 35 )
label.pack(pady = 10, padx = 100)

#le button pour choisir le nombre des atomes initials
var = IntVar()
scale = Scale(rightframe, from_=1,to=250, resolution=1, orient=HORIZONTAL, length=300,width=20, label="Number of atoms", highlightbackground = "white", highlightcolor = "black", bd = 3, tickinterval=0.2, variable = var)
scale.pack(padx=100, pady=10)

button1 = Button(rightframe, text="Set", activebackground = "black", activeforeground="white", bg = "white", fg = "black", command=sel) #pour commencer le simulation
button1.config( width = 35 )
button1.pack(padx=100, pady=10)

button3 = Button(rightframe, text = "Launch the neutron", activebackground = "black", activeforeground="white", bg = "white", fg = "black", command=clicked) #button pour lancer le neutron
button3.config( width = 35 )
button3.pack(padx = 100, pady = 10)

button2 = Button(rightframe, text="Restart", activebackground = "black", activeforeground="white", bg = "white", fg = "black",  command=restart) #pour effacer tout 
button2.config( width = 35 )
button2.pack(padx=100, pady=10)

# compteur d'energie
texte=Label(rightframe,text="Compteur : " + str(energie) + "MeV", bg = "white", bd = 5) 
texte.config( width = 35 )
texte.pack(padx=100, pady=10)


root.mainloop()
