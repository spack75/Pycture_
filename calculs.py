# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 09:57:19 2022

@author: kevinlepetit
"""
from math import sqrt, acos
import PIL.Image as im
import numpy as np


def produit_scalaire(A,B):
    """
    Calcule un produit scalaire
    -----
    entrée :
    A :: list /// Liste de deux élèments, mathématiquement un vecteur 
    B :: list /// Liste de deux élèments, mathématiquement un vecteur
    -----
    retour :
    1 :: float /// Le produit scalaire des deux vecteurs
    """
    return A[0]*B[0]+A[1]*B[1]  # utilisation de la formule euclidienne du produit scalaire sur l'ensemble des vecteurs de R²


def norme(A,scale=1.):
    """
    Calcule une norme définie à partir du produit scalaire
    -----
    entrée :
    A :: list /// Liste de deux élèments, mathématiquement un vecteur 
    scale :: float :: par défaut : 1 /// réel, mathématiqement une echelle issue d'un éventuel calibrage 
    -----
    retour :
    1 :: float /// La norme du vecteur en entrée
    """
    return sqrt(produit_scalaire(A,A))/scale  # utilisation de la formule usuelle de la norme euclidienne


def calcul_angle(A,B):
    """
    Calcule un demi-angle à partir du produit scalaire
    -----
    entrée :
    A :: list /// Liste de deux élèments, mathématiquement un vecteur 
    B :: list /// Liste de deux élèments, mathématiquement un vecteur
    -----
    retour :
    1 :: float /// Le demi-angle non orienté des deux vecteurs
    """
    return 0.5*acos(produit_scalaire(A,B)/norme(A)/norme(B))  # inversion au sens de l'angle de la formule géomètrique du produit scalaire


def gris(img_name_in, img_name_out):
    """
    Transforme une image couleur en image de nuance de gris par la moyenne
    -----
    entrée :
    img_name_in :: str /// L'image de couleur à convertir
    img_name_out :: str /// L'image d'entrée en nucances de gris
    -----
    retour :
    img_name_out :: str /// L'image d'entrée en nucances de gris
    """
    img = im.open(img_name_in)                   # ouverture de l'image d'entrée
    pix = np.array(img)                          # conversion de l'image en tableau numpy POUR REFERENCE
    out = np.array(img)                          # conversion de l'image en tableau numpy POUR LA SORTIE (on aurait aussi pu créer une image vide aux mêmes dimensions)
    for i in range(len(pix)):                    # double boucle for car les tableaux crées sont 2D
        for j in range(len(pix[0])):
            moy = sum(pix[i][j])/3               # calcul de la moyenne RGB pour chacun des pixels
            out[i][j] = [moy for k in range(3)]  # remplissage du tableau de l'image de sortie pour chacun des pixels
    i = im.fromarray(out, "RGB")                 # conversion tableau -> image
    i.save(img_name_out)                         # sauvegarde de l'image


def calcul_taux_pixel_blanc(img_name):
    """
    Calcule le taux de gris d'une image en nuance de gris
    -----
    entrée :
    img_name:: str  /// L'image en nuance de gris à traiter
    -----
    retour :
    1 :: float  /// Le taux de gris
    """
    img = im.open(img_name)           # ouverture de l'image d'entrée
    pix = np.array(img)               # conversion de l'image en tableau numpy POUR REFERENCE
    lx = len(pix)                     # obtention de la première dimension du tableau pix
    ly = len(pix[0])                  # obtention de la deuxième dimension du tableau pix
    moy = 0.                          # initialisation du taux de gris
    for i in range(lx):               # double boucle for car le tableaux crée est à deux dimensions
        for j in range(ly):
            moy = moy + pix[i][j][0]  # sommation de la moyenne
    return moy/(lx*ly)/255            # normalisation de la somme pour obtenir le taux

