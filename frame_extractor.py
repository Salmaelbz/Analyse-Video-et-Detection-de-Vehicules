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
M = 200  # Nombre d'images pour calculer la moyenne

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

# Seuillage pour isoler les pixels de la route
seuil_bas = 120
seuil_haut = 185
masque_route = cv2.inRange(fond_gris, seuil_bas, seuil_haut)

# Inversion du masque pour obtenir les voitures
masque_voitures = cv2.bitwise_not(masque_route)

# Application du masque pour isoler les voitures
voitures = cv2.bitwise_and(fond_gris, fond_gris, mask=masque_voitures)

# Affichage des trois images : fond gris, masque de la route et voitures isolées
cv2.imshow('Fond Gris', fond_gris)
cv2.imshow('Masque Route', masque_route)
cv2.imshow('Voitures', voitures)

# Attente d'une touche pour fermer les fenêtres
cv2.waitKey(0)
cv2.destroyAllWindows()

# Libération des ressources
cap.release()