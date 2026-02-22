import cv2
import numpy as np

# Chargement de l'image en niveaux de gris
img = cv2.imread('route.png', cv2.IMREAD_GRAYSCALE)

# Vérification que l'image a été chargée correctement
if img is None:
    print("Erreur lors du chargement de l'image")
    exit()

# Définition des paramètres pour le seuillage adaptatif
valeur_max = 255
type_adaptatif = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
type_seuillage = cv2.THRESH_BINARY
taille_bloc = 11
constante_C = 2

# Application du seuillage adaptatif
img_seuillee = cv2.adaptiveThreshold(img, valeur_max, type_adaptatif, type_seuillage, taille_bloc, constante_C)

# Affichage de l'image résultante
cv2.imshow('Seuillage adaptatif', img_seuillee)
cv2.waitKey(0)
cv2.destroyAllWindows()