# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 09:57:19 2022

@author: kevinlepetit
"""
from math import sqrt, acos
import PIL.Image as im
import numpy as np


def produit_scalaire(A,B):
    xa, ya = A[0], A[1]
    xb, yb = B[0], B[1]
    return xa*xb+ya*yb


def norme(A,scale=1.):
    return sqrt(produit_scalaire(A,A))/scale


def calcul_angle(A,B):
    return 0.5*acos(produit_scalaire(A,B)/norme(A)/norme(B))


def gris(img_name_in, img_name_out):
    img = im.open(img_name_in)
    pix = np.array(img)
    out = np.array(img)
    for i in range(len(pix)):
        for j in range(len(pix[0])):
            moy = sum(pix[i][j])/3
            out[i][j] = [moy for k in range(3)]
    i = im.fromarray(out, "RGB")
    i.save(img_name_out)


def calcul_taux_pixel_blanc(img_name):

    img = im.open(img_name)
    pix = np.array(img)
    lx = len(pix)
    ly = len(pix[0])
    moy = 0
    for i in range(lx):
        for j in range(ly):
            moy = moy + pix[i][j][0]
    return moy/(lx*ly)/255

