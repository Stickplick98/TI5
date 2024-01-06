"""
import cv2 as cv
import numpy as np


img_tools = cv.imread("C:\\TraitementImages3eme\\Images\\tools.png",cv.IMREAD_GRAYSCALE)
hauteur, largeur = img_tools.shape[:2]

moitie_gauche = img_tools[:, :largeur//2]
moitie_droite = img_tools[:, largeur//2:]

img_mask_gauche = moitie_gauche.copy()
img_mask_droite = moitie_droite.copy()
ret,img_mask_gauche = cv.threshold(img_mask_gauche,136,255,cv.THRESH_BINARY)
ret,img_mask_droite = cv.threshold(img_mask_droite,120,255,cv.THRESH_BINARY)
image_fusionnee = np.concatenate((img_mask_gauche, img_mask_droite), axis=1)


cv.imshow("img_mask_gauche",img_mask_gauche)
cv.imshow("img_mask_droite",img_mask_droite)
cv.imshow("image_fusionnee",image_fusionnee)

cv.waitKey(0)
cv.destroyAllWindows()
"""

#bonne version

"""
import cv2 as cv
import numpy as np

img_tools = cv.imread("C:\\TraitementImages3eme\\Images\\tools.png", cv.IMREAD_GRAYSCALE)
hauteur, largeur = img_tools.shape[:2]

moitie_haut = img_tools[:hauteur//3, :]
moitie_bas = img_tools[hauteur//3:, :]

hauteur_bas, largeur_bas = moitie_bas.shape[:2]

moitie_gauche_bas = moitie_bas[:, :largeur_bas//2]
moitie_droite_bas = moitie_bas[:, largeur_bas//2:]



img_mask_haut = moitie_haut.copy()
img_mask_gauche_bas = moitie_gauche_bas.copy()
img_mask_droite_bas = moitie_droite_bas.copy()
ret, img_mask_haut = cv.threshold(img_mask_haut, 136, 255, cv.THRESH_BINARY)
ret, img_mask_gauche_bas = cv.threshold(img_mask_gauche_bas, 136, 255, cv.THRESH_BINARY)
ret, img_mask_droite_bas = cv.threshold(img_mask_droite_bas, 115, 255, cv.THRESH_BINARY)

image_fusionnee1 = np.concatenate((img_mask_gauche_bas, img_mask_droite_bas), axis=1)
image_fusionnee = np.concatenate((img_mask_haut, image_fusionnee1), axis=0)

cv.imshow("image de base", img_tools)
cv.imshow("img_mask_haut", img_mask_haut)
cv.imshow("img_mask_gauche_bas", img_mask_gauche_bas)
cv.imshow("img_mask_droite_bas", img_mask_droite_bas)
cv.imshow("image_fusionnee", image_fusionnee)

cv.waitKey(0)
cv.destroyAllWindows()
"""

import cv2 as cv
import numpy as np

img_tools = cv.imread("C:\\TraitementImages3eme\\Images\\tools.png", cv.IMREAD_GRAYSCALE)
hauteur, largeur = img_tools.shape[:2]

moitie_haut = img_tools[:hauteur//3, :]
moitie_bas = img_tools[hauteur//3:, :]

hauteur_bas, largeur_bas = moitie_bas.shape[:2]

moitie_gauche_bas = moitie_bas[:, :largeur_bas//2]
moitie_droite_bas = moitie_bas[:, largeur_bas//2:]

# Seconde division sur la largeur
hauteur_droite_bas, largeur_droite_bas = moitie_droite_bas.shape[:2]
moitie_gauche_droite_bas = moitie_droite_bas[:, :largeur_droite_bas//2]
moitie_droite_droite_bas = moitie_droite_bas[:, largeur_droite_bas//2:]

hauteur_droite_bas_haut, largeur_droite_bas_haut = moitie_gauche_droite_bas.shape[:2]
moitie_gauche_droite_bas_haut = moitie_gauche_droite_bas[:hauteur_droite_bas_haut//2, :]
moitie_droite_droite_bas_bas = moitie_gauche_droite_bas[hauteur_droite_bas_haut//2:, :]

cv.imshow("image de base3", moitie_gauche_droite_bas_haut)
cv.imshow("image de base2", moitie_droite_droite_bas_bas)

img_mask_haut = moitie_haut.copy()
ret, img_mask_haut = cv.threshold(img_mask_haut, 136, 255, cv.THRESH_BINARY)

img_mask_gauche_bas = moitie_gauche_bas.copy()
ret, img_mask_gauche_bas = cv.threshold(img_mask_gauche_bas, 136, 255, cv.THRESH_BINARY)


img_mask_droite_droite_bas = moitie_droite_droite_bas.copy()
ret, img_mask_droite_droite_bas = cv.threshold(img_mask_droite_droite_bas, 110, 255, cv.THRESH_BINARY)

img_mask_moitie_gauche_droite_bas_haut = moitie_gauche_droite_bas_haut.copy()
ret, img_mask_moitie_gauche_droite_bas_haut = cv.threshold(img_mask_moitie_gauche_droite_bas_haut, 130, 255, cv.THRESH_BINARY)

img_mask_moitie_droite_droite_bas_bas = moitie_droite_droite_bas_bas.copy()
ret, img_mask_moitie_droite_droite_bas_bas = cv.threshold(img_mask_moitie_droite_droite_bas_bas, 113, 255, cv.THRESH_BINARY)


image_fusionnee3 = np.concatenate((img_mask_moitie_gauche_droite_bas_haut, img_mask_moitie_droite_droite_bas_bas), axis=0)
image_fusionnee2 = np.concatenate((image_fusionnee3, img_mask_droite_droite_bas), axis=1)
image_fusionnee1 = np.concatenate((img_mask_gauche_bas, image_fusionnee2), axis=1)
image_fusionnee = np.concatenate((img_mask_haut, image_fusionnee1), axis=0)

cv.imshow("image de base", img_tools)
cv.imshow("img_mask_haut", img_mask_haut)
cv.imshow("img_mask_gauche_bas", img_mask_gauche_bas)
cv.imshow("moitie_gauche_droite_bas", moitie_gauche_droite_bas)
cv.imshow("moitie_droite_droite_bas", moitie_droite_droite_bas)
cv.imshow("image_fusionnee", image_fusionnee)

cv.waitKey(0)
cv.destroyAllWindows()

"""
import cv2 as cv
import numpy as np

img = cv.imread("C:\\TraitementImages3eme\\Images\\tools.png", cv.IMREAD_GRAYSCALE)

#Paramètres pour les contours
edges = cv.Canny(img, 0, 210)

#dilater les contours
kernel = np.ones((3, 3), np.uint8)
dilatededges = cv.dilate(edges, kernel, iterations=1)

#Trouver les contours dans l'image
contours,_ = cv.findContours(dilatededges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

#Créer une image noire
img_noir = np.zeros_like(img)

#Dessiner en blanc les "tools" sur l'image noire
cv.drawContours(img_noir, contours, -1, (255, 255, 255), thickness=cv.FILLED)

cv.imshow('img_noir', img_noir)
cv.imwrite("img_noir.png", img_noir)
#Remmetre la "couleur"
tools_with_color = cv.bitwise_and(img_noir, img)

#Seuillage pour "voir" enlevé les trous
_,tools_blanc = cv.threshold(tools_with_color, 112, 255, cv.THRESH_BINARY)

cv.imshow('Original', img)
cv.imshow('tools_blanc', tools_blanc)


cv.waitKey(0)
cv.destroyAllWindows()
"""