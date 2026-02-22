import cv2
import numpy as np

#Chargement de l'image existante en utilisant OpenCV
img_originale = cv2.imread('route.png')

# Définition des paramètres pour le seuillage
seuil = 127  # Exemple de valeur de seuil
valeur_max = 255  # La valeur à attribuer si la condition de seuillage est remplie
type_seuillage = cv2.THRESH_BINARY  # Type de seuillage, ici binaire

# Seuillage simple
_, img_seuillee = cv2.threshold(img_originale, seuil, valeur_max, type_seuillage)

# Affichage de l'image résultante pour vérifier le seuillage
cv2.imshow('Seuillage simple', img_seuillee)
cv2.waitKey(0)
cv2.destroyAllWindows()
