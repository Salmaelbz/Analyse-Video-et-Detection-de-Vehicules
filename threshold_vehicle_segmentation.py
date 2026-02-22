import cv2
import numpy as np

# Chemin vers l'image de la route
image_path = 'route.png'

# Lecture de l'image en niveaux de gris
image_route = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Vérification que l'image a été chargée
if image_route is None:
    print("Erreur lors de la lecture de l'image")
    exit()

# Seuillage pour isoler les pixels de la route
seuil_bas = 120
seuil_haut = 185
masque_route = cv2.inRange(image_route, seuil_bas, seuil_haut)

# Inversion du masque pour obtenir les voitures
masque_voitures = cv2.bitwise_not(masque_route)

# Application du masque pour isoler les voitures
voitures = cv2.bitwise_and(image_route, image_route, mask=masque_voitures)

# Affichage des voitures isolées
cv2.imshow('Voitures', voitures)
cv2.waitKey(0)
cv2.destroyAllWindows()