import cv2
import numpy as np

#Chargement de l'image existante en utilisant OpenCV
img_originale = cv2.imread('route.png')

# Remise à zéro de l'image
img = np.zeros((img_originale.shape[0], img_originale.shape[1], 3), dtype=np.uint8)

# Affichage de  l'image résultante pour vérifier qu'elle a été remise à zéro (elle devrait être complètement noire) :
cv2.imshow('Image remise a zero', img)
cv2.waitKey(0)
cv2.destroyAllWindows()