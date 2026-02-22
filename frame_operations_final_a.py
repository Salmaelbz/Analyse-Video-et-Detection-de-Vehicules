import cv2
import numpy as np

# Chargement de l'image en niveaux de gris
img = cv2.imread('route.png', cv2.IMREAD_GRAYSCALE)

# Vérification que l'image a été chargée correctement
if img is None:
    print("Erreur lors du chargement de l'image")
    exit()

# Création d'un noyau ou élément structurant pour l'érosion
taille_noyau = 3  # Taille du noyau, peut être ajustée selon les besoins
noyau = np.ones((taille_noyau, taille_noyau), np.uint8)

# Application de l'érosion
img_erodee = cv2.erode(img, noyau, iterations=1)

# Affichage de l'image résultante
cv2.imshow('Image erodee', img_erodee)
cv2.waitKey(0)
cv2.destroyAllWindows()