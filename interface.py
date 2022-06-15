# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 10:40:24 2022

@author: kevinlepetit
"""

import tkinter as tk
from PIL import ImageTk, Image
import calculs as c


def execution():
  """
  Lance la fenetre principale
  -----
  entrée :
  Rien
  -----
  retour :
  Rien
  """
  ##### Configuration #####

  window = tk.Tk()                                 # commande de creation d'application
  xscreen = int(window.winfo_screenwidth())   # obtention de la longueur de l'écran
  yscreen = int(window.winfo_screenheight())  # obtention de la largeur de l'écran
  window.title("traitement image")                 # titre de l'application
  window.geometry("300x140")                       # taille de la fenetre
  window.config(background='#42B79F')              # couleur de fond de la fenetre
  window.resizable(width=False,height=False)       # la fenetre a une taille fixe
  ##### Configuration #####
  
  
  
  
  
  
  ##### fonction associee au bouton lancer #####
  def lancer(*args):
    """
    Lance la fenetre de traitement de l'image
    -----
    entrée :
    Rien
    -----
    retour :
    Rien
    """

    ##### déclaration des variables #####
    posx    = []                                                                   # liste des positions x des clicks
    posy    = []                                                                   # liste des positions y des clicks 
    img     = Image.open('img/'+nomformat.get())                                   # chargement de l'image d'entrée
    xphoto = img.size[0]                                                           # longueur de la photo
    yphoto = img.size[1]                                                           # largeur de la photo
    xratio = xphoto/xscreen                                                        # rapport d'aspect selon x
    yratio = yphoto/yscreen                                                        # rapport d'aspect selon y
    if (xphoto > xscreen) and (yphoto > yscreen): # s'il y aurait un dépassement (selon x ET y) de l'écran dans le cas où on afficherait la photo sans modification des dimensions

      if xratio > yratio: # si ce dépassement est le plus important selon x
        LONGUEUR = xscreen               # plus grande longueur possible telle que l'on ne retrouve pas de dépassement lors du chargement de la photo
        LARGEUR  = int(yphoto / xratio)  # plus grande largeur possible telle que l'on ne retrouve pas de dépassement lors du chargement de la photo

      else: # si ce dépassement est le plus important selon y
        LONGUEUR = int(xphoto / yratio)  # plus grande longueur possible telle que l'on ne retrouve pas de dépassement lors du chargement de la photo
        LARGEUR  = yscreen               # plus grande largeur possible telle que l'on ne retrouve pas de dépassement lors du chargement de la photo

    elif (xphoto > xscreen): # s'il y aurait un dépassement seulement selon x de l'écran dans le cas où on afficherait la photo sans modification des dimensions

        LONGUEUR = xscreen               # plus grande longueur possible telle que l'on ne retrouve pas de dépassement lors du chargement de la photo
        LARGEUR  = int(yphoto / xratio)  # plus grande largeur possible telle que l'on ne retrouve pas de dépassement lors du chargement de la photo

    elif (yphoto > yscreen): # s'il y aurait un dépassement seulement selon y de l'écran dans le cas où on afficherait la photo sans modification des dimensions

        LONGUEUR = int(xphoto / yratio)  # plus grande longueur possible telle que l'on ne retrouve pas de dépassement lors du chargement de la photo
        LARGEUR  = yscreen               # plus grande largeur possible telle que l'on ne retrouve pas de dépassement lors du chargement de la photo

    else: # s'il n'y aurait aucun dépassement de l'écran dans le cas où on afficherait la photo sans modification des dimensions (et que l'on veut rendre l'image la plus grande possible)

      if xphoto > yphoto: # si l'aspect le plus grand est selon x

        LONGUEUR = xscreen               # plus grande longueur possible telle que l'on ne retrouve pas de dépassement lors du chargement de la photo
        LARGEUR  = int(yphoto / xratio)  # plus grande largeur possible telle que l'on ne retrouve pas de dépassement lors du chargement de la photo

      else: # si l'aspect le plus grand est selon y

        LONGUEUR = int(xphoto / yratio)  # plus grande longueur possible telle que l'on ne retrouve pas de dépassement lors du chargement de la photo
        LARGEUR  = yscreen               # plus grande largeur possible telle que l'on ne retrouve pas de dépassement lors du chargement de la photo

    im      = img.resize((int(LONGUEUR*0.9), int(LARGEUR*0.9))) # adaptation des dimensions de l'image à celles de la fenetre
    im.save("test.jpg")
    image   = tk.Toplevel(window)             # creation de la fenetre de traitement de l'image
    image.geometry(f"{xscreen}x{yscreen}")
    ##### déclaration des variables #####


    ##### fonctions #####
    def clic(event):
      """
      enregistre la position du curseur lors d'un click et affiche un rectangle sur l'image à l'endroit du click
      -----
      entrée :
      event :: list /// liste contenant la position du curseur au moment du clic
      -----
      retour :
      Rien
      """
      X = event.x                                                                            # enregistrement de la position x du curseur
      Y = event.y                                                                            # enregistrement de la position y du curseur
      posx.append(X)                                                                         # ajout de la position y du curseur dans la liste des positions X des clicks
      posy.append(Y)                                                                         # ajout de la position y du curseur dans la liste des positions y des clicks
      r = 3                                                                                  # taille du rectangle
      surface_dessin.create_rectangle(X-r, Y-r, X+r, Y+r, outline = 'black',fill = 'green')  # creation du point placé sur la position où le click a été fait
        

    def effacer():
      """
      efface le contenu des listes des positions x et y des clicks ainsi que les rectangles placés lors des clicks
      -----
      entrée :
      rien
      -----
      retour :
      Rien
      """
      posx.clear()                                                                   # suppression de la liste des positions x des clicks
      posy.clear()                                                                   # suppression de la liste des positions y des clicks
      surface_dessin.delete(tk.ALL)                                                  # les rectangles sont effacés en réinitialisant l'image
      surface_dessin.image = ImageTk.PhotoImage(im)                                  # rechargement de l'image
      surface_dessin.create_image(0, 0,  image=surface_dessin.image, anchor= tk.NW)  # actualisation de l'image


    def angle_calc():
      """
      calcule un angle à partir de trois points
      -----
      entrée :
      rien
      -----
      retour :
      Rien
      """
      Origine = [posx[1],posy[1]]                     # calcul de l'intersection des deux vecteurs
      A = [posx[0]-Origine[0],posy[0]-Origine[1]]     # creation du premier vecteur 
      B = [posx[2]-Origine[0],posy[2]-Origine[1]]     # creation du deuxiemme vecteur 
      var_calc.set(str(c.calcul_angle(A,B)*180/3.1415))  # calcul de l'angle grace à la fonction calcul_angle du module calculs.py


    def distance_calc():
      """
      calcule la distance entre deux points 
      -----
      entrée :
      rien
      -----
      retour :
      Rien
      """
      A = [posx[1]-posx[0],posy[-1]-posy[0]]           # creation du vecteur compatible avec l'appel de la fonction norme de calculs.py
      var_calc.set(str(c.norme(A,float(echelle.get()))))  # calcul de l'angle avec l'appel de la fonction norme de calculs.py


    def calibrage_calc():
      """
      normalise la distance entre deux pixels à partir de deux points de référence
      -----
      entrée :
      rien
      -----
      retour :
      Rien
      """
      A = [posx[1]-posx[0],posy[-1]-posy[0]]  # creation du vecteur compatible avec l'appel de la fonction norme de calculs.py
      echelle.set(str(c.norme(A)))            # normalisation avec l'appel de la fonction norme de calculs.py


    def position_calc():
      """
      enregistre les positions de tous les clicks dans un fichier texte
      -----
      entrée :
      rien
      -----
      retour :
      1 :: fichier texte /// le fichier dans lequel est enregistré la position de tous les points
      """
      f = open("coord","w")                                                                    # ouverture du fichier
      for i in range(len(posx)):                                                               # pour chaque click réalisé
        f.write(str(posx[i]/float(echelle.get()))+" "+str(posy[i]/float(echelle.get()))+"\n")  # écriture dans le fichier texte au format "posx_point posy_point"
      f.close()                                                                                # fermeture du fichier 
    ##### fonctions #####


    ##### surface de dessin #####
    surface_dessin = tk.Canvas(image, width = LONGUEUR*0.9, height = LARGEUR*0.9)          # création de la surface de l'image
    surface_dessin.image = ImageTk.PhotoImage(im)                                  # chargement de l'image
    surface_dessin.create_image(0, 0,  image=surface_dessin.image, anchor= tk.NW)  # affichage de l'image
    surface_dessin.pack()#padx = 5, pady = 5)                                        # placement de l'image
    surface_dessin.bind('<Button-1>',clic)                                         # affectation du click à la fonction clic
    ##### surface de dessin #####

    def rien():
      print("je fais pas grand chose")
    ##### boutons #####
    menubar = tk.Menu(image)
    sysmenu = tk.Menu(menubar, tearoff=0)
    sysmenu.add_command(label="Changer d'image", command=image.destroy)
    sysmenu.add_command(label="Quitter", command=window.destroy)
    sysmenu.add_separator()
    sysmenu.add_command(label="Effacer les points placés", command=effacer)
    sysmenu.add_command(label="Sauvegarder les positions des points placés", command=position_calc)
    menubar.add_cascade(label="Fichier", menu=sysmenu)

    calcmenu = tk.Menu(menubar, tearoff=0)
    calcmenu.add_command(label="Calibrer l'échelle de longueur", command=calibrage_calc)
    calcmenu.add_separator()
    calcmenu.add_command(label="Calculer une distance", command=distance_calc)
    calcmenu.add_command(label="Calculer un angle", command=angle_calc)
    menubar.add_cascade(label="Fichier", menu=calcmenu)


    image.config(menu=menubar)
  ##### fonction associee au bouton lancer #####

  ##### boutons #####

  ##### bouton lancer #####
  bpushaxe = tk.Button(window,text="OUVRIR",command=lancer,bg='#72aaab',width=40,height=4)
  bpushaxe.place(x=5,y=35)
  ##### bouton lancer #####
  
  ##### affichage var_calc #####
  var_calc = tk.StringVar()
  var_calc.set(" ")

  var_calclabel1 = tk.Label(window,text="grandeur calculée:",bg='#42B79F')
  var_calclabel1.place(x=10,y=113)
  
  var_calclabel2 = tk.Label(window,textvariable=var_calc,bg='#42B79F')
  var_calclabel2.place(x=135,y=113)
  ##### affichage var_calc #####
  
  
  ##### calibrage #####
  echelle = tk.StringVar()
  echelle.set("1")
  ##### calibrage #####
  
  
  ##### nom image #####
  def update_nomformat(*args):
      pass
  nomformat = tk.StringVar()
  nomformat.trace("w", update_nomformat)
  nomformat.set("insérer nom de l'image")
  
  lnomformat = tk.Label(window,text="Nom de l'image:",bg='#42B79F')
  lnomformat.place(x=10,y=10)
  
  bnomformat = tk.Entry(window,textvariable=nomformat, width=28)
  bnomformat.place(x=115,y=10)
  ##### nom image #####
  
  window.mainloop()