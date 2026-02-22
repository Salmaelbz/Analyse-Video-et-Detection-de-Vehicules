import cv2
import numpy as np

#Chargement de l'image existante en utilisant OpenCV
img_originale = cv2.imread('route.png')

# Conversion de l'image en type uint8
img = img_originale.astype('uint8')

# Affichage de  l'image résultante pour vérifier qu'elle a été remise à zéro (elle devrait être complètement noire) :
cv2.imshow('Image converti en type uint8', img)
cv2.waitKey(0)
cv2.destroyAllWindows()