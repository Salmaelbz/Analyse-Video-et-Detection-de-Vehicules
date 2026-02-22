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

# Utilisation de BackgroundSubtractorMOG2 pour la soustraction de fond
bg_subtractor = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=True)

# Définir la ROI (à ajuster selon la vidéo)
y_min, y_max = 250, 350

compteur_voitures = 0
voitures_detectees = []

# Ralentir la vidéo en augmentant le délai dans cv2.waitKey()
delay = 100

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Appliquer la soustraction de fond
    fg_mask = bg_subtractor.apply(gray_frame)
    
    # Utiliser le filtrage par couleur si nécessaire (à implémenter)
    
    # Appliquer des techniques de machine learning pour la détection (à implémenter)
    
    # Optimisation des paramètres de traitement d'image
    _, fg_mask = cv2.threshold(fg_mask, 50, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_CLOSE, kernel)
    
    # Détection de contours pour identifier les voitures
    contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > 100:
            x, y, w, h = cv2.boundingRect(contour)
            centre_contour = (int(x + w/2), int(y + h/2))
            if y_min < centre_contour[1] < y_max:
                if not any(centre_contour == centre for centre in voitures_detectees):
                    voitures_detectees.append(centre_contour)
                    compteur_voitures += 1

    cv2.putText(frame, "Voitures: {}".format(compteur_voitures), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Voitures Isolees', frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

print("Nombre total de voitures détectées dans la vidéo :", compteur_voitures)

cap.release()
cv2.destroyAllWindows()