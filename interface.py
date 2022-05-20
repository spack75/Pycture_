# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 10:40:24 2022

@author: kevinlepetit
"""

import tkinter as tk
from PIL import ImageTk, Image
import calculs as c
def execution():
  #### Configuration
  window = tk.Tk()
  window.title("traitement image")
  window.geometry("300x140")
  window.config(background='#42B79F')
  window.resizable(width=False,height=False)
  #### Configuration
  
  
  
  
  
  
  #### bouton lancer ####
  def lancer(*args):
      
      posx    = []
      posy    = []
      LARGEUR = 450
      HAUTEUR = 600      
      img     = Image.open('img/'+nomformat.get()+'.jpg')
      im      = img.resize((450, 600))
      image   = tk.Toplevel(window)
      def clic(event):
          X = event.x
          Y = event.y
          posx.append(X)
          posy.append(Y)
          r = 3
          surface_dessin.create_rectangle(X-r, Y-r, X+r, Y+r, outline = 'black',fill = 'green')
          
      def effacer():
          posx.clear()
          posy.clear()
          surface_dessin.delete(tk.ALL)
          surface_dessin.image = ImageTk.PhotoImage(im)
          surface_dessin.create_image(0, 0,  image=surface_dessin.image, anchor= tk.NW)
      def angle_calc():
          Origine = [posx[1],posy[1]]
          A = [posx[0]-Origine[0],posy[0]-Origine[1]]
          B = [posx[2]-Origine[0],posy[2]-Origine[1]]
          angle.set(str(c.calcul_angle(A,B)*180/3.1415))
      def distance_calc():
          A = [posx[1]-posx[0],posy[-1]-posy[0]]
          angle.set(str(c.norme(A,float(echelle.get()))))
      def calibrage_calc():
          A = [posx[1]-posx[0],posy[-1]-posy[0]]
          echelle.set(str(c.norme(A)))
      def position_calc():
          f = open("coord","w")
          for i in range(len(posx)):
            f.write(str(posx[i]/float(echelle.get()))+" "+str(posy[i]/float(echelle.get()))+"\n")
          f.close()
      surface_dessin = tk.Canvas(image, width = LARGEUR, height = HAUTEUR)
      surface_dessin.image = ImageTk.PhotoImage(im)
      surface_dessin.create_image(0, 0,  image=surface_dessin.image, anchor= tk.NW)
      surface_dessin.pack(padx = 5, pady = 5)
      
      surface_dessin.bind('<Button-1>',clic)
      surface_dessin.pack(padx =5, pady =5)
      
      # Création d'un widget Button (bouton Effacer)
      tk.Button(image, text = 'Effacer', command = effacer).pack(side = tk.LEFT,padx = 5,pady = 5)
      # Création d'un widget Button (bouton Angle)
      tk.Button(image, text = 'Angle', command = angle_calc).pack(side = tk.LEFT,padx = 5,pady = 5)
    # Création d'un widget Button (bouton Distance)
      tk.Button(image, text = 'Distance', command = distance_calc).pack(side = tk.LEFT,padx = 5,pady = 5)
    # Création d'un widget Button (bouton Calibrage)
      tk.Button(image, text = 'Calibrer', command = calibrage_calc).pack(side = tk.LEFT,padx = 5,pady = 5)
    # Création d'un widget Button (bouton Calibrage)
      tk.Button(image, text = 'Position', command = position_calc).pack(side = tk.LEFT,padx = 5,pady = 5)
      # Création d'un widget Button (bouton Quitter)
      tk.Button(image, text = 'Quitter', command = image.destroy).pack(side = tk.LEFT,padx = 5,pady = 5)   
  
  
  bpushaxe = tk.Button(window,text="OUVRIR",command=lancer,bg='#72aaab',width=40,height=4)
  bpushaxe.place(x=5,y=35)
  #### bouton lancer ####
  
  #### affichage angle ####
  angle = tk.StringVar()
  angle.set(" ")
  
  anglelabel1 = tk.Label(window,text="grandeur calculée:",bg='#42B79F')
  anglelabel1.place(x=10,y=113)
  
  anglelabel2 = tk.Label(window,textvariable=angle,bg='#42B79F')
  anglelabel2.place(x=135,y=113)
  #### affichage angle ####
  
  
  #### calibrage ####
  echelle = tk.StringVar()
  echelle.set("1")
  #### calibrage ####
  
  
  #### nom image ####
  def update_nomformat(*args):
      pass
  nomformat = tk.StringVar()
  nomformat.trace("w", update_nomformat)
  nomformat.set("insérer nom de l'image")
  
  lnomformat = tk.Label(window,text="Nom de l'image:",bg='#42B79F')
  lnomformat.place(x=10,y=10)
  
  bnomformat = tk.Entry(window,textvariable=nomformat, width=28)
  bnomformat.place(x=115,y=10)
  #### nom image ####
  
  window.mainloop()