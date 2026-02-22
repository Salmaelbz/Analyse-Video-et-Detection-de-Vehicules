import cv2
import numpy as np

# Chemin vers la vidéo de l'autoroute
video_path = 'video.avi'

# Création d'un objet VideoCapture
cap = cv2.VideoCapture(video_path)

# Vérification de l'ouverture du flux vidéo
if not cap.isOpened():
    print("Erreur lors de l'ouverture de la vidéo")
    exit()

# Initialisation de la structure pour calculer la moyenne
accumulateur = None
M = 1  # Nombre d'images pour calculer la moyenne

# Lecture des M premières images pour calculer le fond
for i in range(M):
    ret, frame = cap.read()
    if not ret:
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Conversion en niveaux de gris
    gray_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)  # Application d'un flou
    if accumulateur is None:
        accumulateur = np.float32(gray_frame)
    else:
        cv2.accumulateWeighted(gray_frame, accumulateur, 0.01)

# Calcul de l'image moyenne du fond
fond_gris = cv2.convertScaleAbs(accumulateur)

# Seuillage pour isoler les pixels de la route
seuil_bas = 120
seuil_haut = 185
masque_route = cv2.inRange(fond_gris, seuil_bas, seuil_haut)

# Extraction de la route
route = cv2.bitwise_and(fond_gris, fond_gris, mask=masque_route)

# Affichage des résultats
cv2.imshow('Fond Gris Moyen', fond_gris)
cv2.imshow('Masque Route', masque_route)
cv2.imshow('Route Extraite', route)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Libération des ressources
cap.release()