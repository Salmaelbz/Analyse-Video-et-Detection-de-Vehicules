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
M = 10  # Nombre d'images pour calculer la moyenne

# Définition de la zone d'intérêt (ROI)
x, y, w, h = 100, 200, 300, 400  # À ajuster selon la zone souhaitée
roi = (x, y, x+w, y+h)

# Lecture des M premières images pour calculer le fond
for i in range(M):
    ret, frame = cap.read()
    if not ret:
        break
    # Sélection de la ROI dans l'image
    frame_roi = frame[y:y+h, x:x+w]
    # Conversion de chaque image couleur en niveaux de gris
    gray_frame = cv2.cvtColor(frame_roi, cv2.COLOR_BGR2GRAY)
    # Conversion en float pour le calcul de la moyenne
    float_frame = gray_frame.astype(np.float32)
    if accumulateur is None:
        accumulateur = float_frame
    else:
        accumulateur += float_frame

# Calcul de l'image moyenne du fond en niveaux de gris
fond_gris = (accumulateur / M).astype(np.uint8)

# Soustraction de fond pour obtenir les différences
difference = cv2.absdiff(fond_gris, gray_frame)

# Seuillage pour obtenir une image binaire des voitures
_, voitures_binaires = cv2.threshold(difference, 50, 255, cv2.THRESH_BINARY)

# Morphologie pour améliorer la forme des objets détectés
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
voitures_binaires = cv2.morphologyEx(voitures_binaires, cv2.MORPH_CLOSE, kernel)

# Détection de contours pour identifier les voitures
contours, _ = cv2.findContours(voitures_binaires, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filtrage des contours et dessin sur l'image originale
voitures_isolees = gray_frame.copy()
for contour in contours:
    if cv2.contourArea(contour) > 100:  # Seuil de taille à ajuster
        cv2.drawContours(voitures_isolees, [contour], -1, (0, 255, 0), 2)

# Affichage des résultats
cv2.imshow('Fond Gris Moyen', fond_gris)
cv2.imshow('Voitures Binaires', voitures_binaires)
cv2.imshow('Voitures Isolees', voitures_isolees)

# Attente d'une touche pour fermer les fenêtres
cv2.waitKey(0)
cv2.destroyAllWindows()