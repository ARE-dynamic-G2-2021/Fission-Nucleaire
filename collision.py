import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

LARGEUR, HAUTEUR = 1000,850

RAYON, NRAYON = 20, 5 #rayon de l'atome et du neutron
CLICK = 0 #variable pour restart
MOVE = 0 #variable pour bouger le neutron
n, nn = 0, 1 #nombre des atoms et des neutrons
SPEED, NSPEED = 5, 15 #okay this is easy to guess

X,Y = [],[]
DX,DY = [],[] 
NX, NY = [], []
NDX, NDY = [], []
Balle, Neutron = [], []


COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
    'indian red', 'saddle brown', 'sandy brown',
    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
    'pale violet red', 'maroon', 'medium violet red', 'violet red',
    'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
    'thistle', 'snow2', 'snow3',
    'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
    'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
    'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
    'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
    'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
    'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
    'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
    'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
    'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
    'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
    'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
    'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
    'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']
# Creation de la fenetre principale
root = Tk()
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
Canevas = Canvas(leftframe,height=HAUTEUR,width=LARGEUR,bg='white')
Canevas.pack(padx=5,pady=5)

def estDansAtome(ax, ay, nx, ny):
    if(nx >= ax-RAYON and nx<= ax+RAYON and ny >= ay-RAYON and ny<= ay+RAYON):
        return True
    return False

def actualiserCollision():
    global X, Y, DX, DY, n, NX, NY, NDX, NDY, nn, Neutron, Balle, Canevas
    #return 
    i = 0
    j = 0
    
    while(i<nn):
        while(j<n):
            if estDansAtome(X[j], Y[j], NX[i], NY[i]):
                nn += 2
                for l in range(2):
                    NX.append(X[j])
                    NY.append(Y[j])
                    angle = 2*np.pi*np.random.rand()
                    NDX.append(np.cos(angle))
                    NDY.append(np.sin(angle))
                    col = COLORS[np.random.randint(1, len(COLORS))-1]
                    k=len(NX)-1
                    Neutron.append(Canevas.create_oval(NX[k]-NRAYON,NY[k]-NRAYON,NX[k]+NRAYON,NY[k]+NRAYON,width=1,fill=col))
                    
                  
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
        global root, X, Y, DX, DY, n, NX, NY, NDX, NDY, nn, Neutron, Balle, Canevas, CLICK, MOVE
        #restart the simulation and exit the function
        if CLICK == 1: 
            Canevas.delete("all")
            MOVE = 0
            CLICK = 0
            n, nn = 0, 1
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
 
            #actualiserCollision()
        # affichage des atomes
        for i in range(n):
            Canevas.coords(Balle[i],X[i]-RAYON,Y[i]-RAYON,X[i]+RAYON,Y[i]+RAYON)
        
        # affichage des neutrons
        #if(MOVE == 1):
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
label = Label(rightframe, text = "Parametres") #label
label.pack(pady = 10, padx = 100)

#le button pour choisir le nombre des atomes initials
var = IntVar()
scale = Scale(rightframe, from_=1,to=100, resolution=1, orient=HORIZONTAL, length=300,width=20, label="Number of atoms",tickinterval=0.2, variable = var)
scale.pack(padx=100, pady=10)

button1 = Button(rightframe, text="Set", command=sel) #pour commencer le simulation
button1.pack(padx=100, pady=10)

button3 = Button(rightframe, text = "LANCER DANGER", activebackground = "coral4", bg = "coral3", command=clicked) #button pour lancer le neutron
button3.pack(pady = 10, padx = 100)

button2 = Button(rightframe, text="Restart", command=restart) #pour effacer tout 
button2.pack(padx=100, pady=10)



root.mainloop()
