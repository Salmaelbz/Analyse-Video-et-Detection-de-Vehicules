import cv2
import numpy as np

# Chemin vers le fichier vidéo
video_path = 'video.avi'

# Création d'un objet VideoCapture
cap = cv2.VideoCapture(video_path)

# Vérification de l'ouverture du flux vidéo
if not cap.isOpened():
    print("Erreur lors de l'ouverture de la vidéo")
    exit()

# Initialisation de la structure pour calculer la moyenne
accumulateur = None
M = 200 # Nombre d'images pour calculer la moyenne

# Lecture des M premières images pour calculer le fond
for i in range(M):
    ret, frame = cap.read()
    if not ret:
        break
    # Conversion de chaque image couleur en niveaux de gris
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Conversion en float pour le calcul de la moyenne
    float_frame = gray_frame.astype(np.float32)
    if accumulateur is None:
        accumulateur = float_frame
    else:
        accumulateur += float_frame

# Calcul de l'image moyenne du fond en niveaux de gris
fond_gris = (accumulateur / M).astype(np.uint8)

# Affichage de l'image moyenne du fond en niveaux de gris
cv2.imshow('Fond Gris', fond_gris)
cv2.waitKey(0)

# Extraction de la route en utilisant un masque
# Pour cet exemple, nous allons simuler un masque avec des opérations simples
masque_route = cv2.inRange(fond_gris, np.array([0]), np.array([100]))

# Application du masque pour isoler la route
route = cv2.bitwise_and(fond_gris, fond_gris, mask=masque_route)

# Affichage de la route isolée
cv2.imshow('Route', route)
cv2.waitKey(0)

# Isolation des voitures
# Pour cet exemple, nous allons simuler la détection des voitures avec des opérations simples
masque_voitures = cv2.inRange(route, np.array([150]), np.array([255]))

# Application du masque pour isoler les voitures
voitures = cv2.bitwise_and(route, route, mask=masque_voitures)

# Affichage des voitures isolées
cv2.imshow('Voitures', voitures)
cv2.waitKey(0)

# Libération des ressources et fermeture des fenêtres
cap.release()
cv2.destroyAllWindows()