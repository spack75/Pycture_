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
  window = tk.Tk()                            # commande de creation d'application
  window.title("traitement image")            # titre de l'application
  window.geometry("300x140")                  # taille de la fenetre
  window.config(background='#42B79F')         # couleur de fond de la fenetre
  window.resizable(width=False,height=False)  # la fenetre a une taille fixe
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
    LARGEUR = 450                                                                  # largeur de la fenetre
    HAUTEUR = 600                                                                  # hauteur de la fenetre
    img     = Image.open('img/'+nomformat.get()+'.jpg')                            # chargement de l'image d'entrée
    im      = img.resize((450, 600))                                               # adaptation des dimensions de l'image à celles de la fenetre
    image   = tk.Toplevel(window)                                                  # creation de la fenetre de traitement de l'image
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
    surface_dessin = tk.Canvas(image, width = LARGEUR, height = HAUTEUR)           # création de la surface de l'image
    surface_dessin.image = ImageTk.PhotoImage(im)                                  # chargement de l'image
    surface_dessin.create_image(0, 0,  image=surface_dessin.image, anchor= tk.NW)  # affichage de l'image
    surface_dessin.pack(padx = 5, pady = 5)                                        # placement de l'image
    surface_dessin.bind('<Button-1>',clic)                                         # affectation du click à la fonction clic
    ##### surface de dessin #####


    ##### boutons #####
    tk.Button(image, text = 'Effacer', command = effacer).pack(side = tk.LEFT,padx = 5,pady = 5)          # Création d'un widget Button (bouton Effacer)
    tk.Button(image, text = 'Angle', command = angle_calc).pack(side = tk.LEFT,padx = 5,pady = 5)         # Création d'un widget Button (bouton Angle)
    tk.Button(image, text = 'Distance', command = distance_calc).pack(side = tk.LEFT,padx = 5,pady = 5)   # Création d'un widget Button (bouton Distance)
    tk.Button(image, text = 'Calibrer', command = calibrage_calc).pack(side = tk.LEFT,padx = 5,pady = 5)  # Création d'un widget Button (bouton Calibrage)
    tk.Button(image, text = 'Position', command = position_calc).pack(side = tk.LEFT,padx = 5,pady = 5)   # Création d'un widget Button (bouton Calibrage)
    tk.Button(image, text = 'Quitter', command = image.destroy).pack(side = tk.LEFT,padx = 5,pady = 5)    # Création d'un widget Button (bouton Quitter)
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