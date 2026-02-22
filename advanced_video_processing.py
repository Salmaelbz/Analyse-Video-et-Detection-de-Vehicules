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
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    float_frame = gray_frame.astype(np.float32)
    if accumulateur is None:
        accumulateur = float_frame
    else:
        accumulateur += float_frame

# Calcul de l'image moyenne du fond en niveaux de gris
fond_gris = (accumulateur / M).astype(np.uint8)

# Définir la ROI (à ajuster selon la vidéo)
y_min, y_max = 250, 350

compteur_voitures = 0
voitures_detectees = []
# Ralentir la vidéo en augmentant le délai dans 
cv2.waitKey(100)
# Par exemple, utiliser 100 ms au lieu de 1 ms pour ralentir la vidéo 100 fois

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    difference = cv2.absdiff(fond_gris, gray_frame)
    _, voitures_binaires = cv2.threshold(difference, 50, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    voitures_binaires = cv2.morphologyEx(voitures_binaires, cv2.MORPH_CLOSE, kernel)
    contours, _ = cv2.findContours(voitures_binaires, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    voitures_isolees = gray_frame.copy()
    for contour in contours:
        if cv2.contourArea(contour) > 100:
            x, y, w, h = cv2.boundingRect(contour)
            centre_contour = (int(x + w/2), int(y + h/2))
            if y_min < centre_contour[1] < y_max:
                if not any(centre_contour == centre for centre in voitures_detectees):
                    voitures_detectees.append(centre_contour)
                    compteur_voitures += 1
            cv2.drawContours(voitures_isolees, [contour], -1, (0, 255, 0), 2)

    cv2.putText(frame, "Voitures: {}".format(compteur_voitures), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Fond Gris Moyen', fond_gris)
    cv2.imshow('Voitures Binaires', voitures_binaires)
    cv2.imshow('Voitures Isolees', voitures_isolees)
   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("Nombre total de voitures détectées dans la vidéo :", compteur_voitures)

cap.release()
cv2.destroyAllWindows()











