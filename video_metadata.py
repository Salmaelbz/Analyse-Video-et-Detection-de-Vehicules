import cv2
import numpy as np

# Chemin vers le fichier vidéo
video_path = 'autoroute2.avi'

# Création d'un objet VideoCapture
cap = cv2.VideoCapture(video_path)

# Question 2: Nombre d'images dans la séquence vidéo
if cap.isOpened():
    # Nombre total de frames dans la vidéo
    N = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Nombre d'images (N) = {N}")

# Question 3: Durée de la séquence vidéo
if cap.isOpened():
    # Nombre d'images par seconde (fps)
    fps = cap.get(cv2.CAP_PROP_FPS)
    # Durée de la vidéo en secondes
    duration = N / fps
    print(f"Durée de la vidéo (t) = {duration} secondes")

# Question 4: Résolution de la séquence vidéo
if cap.isOpened():
    # Largeur de la vidéo
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # Hauteur de la vidéo
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(f"Résolution de la vidéo = {width}x{height}")

# Liste pour stocker les frames en niveaux de gris
gray_frames = []

# Question 5: Convertir la séquence vidéo en niveaux de gris et l'afficher
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # Conversion de l'image couleur en niveaux de gris
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_frames.append(gray_frame)  # Stockage des frames en niveaux de gris
        
        # Accès aux valeurs des pixels
        # Pour une image en niveaux de gris
        valeur_niveau_gris = gray_frame[0][0]

        # Pour une image en couleur
        valeur_bgr = frame[0][0]
        bleu, vert, rouge = valeur_bgr  # Décomposition en composantes B, G, R
        
        # Affichage de la vidéo en niveaux de gris
        cv2.imshow('Gray video', gray_frame)
        
        # Quitter avec la touche 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Libération de l'objet VideoCapture et fermeture des fenêtres
cap.release()
cv2.destroyAllWindows()

# Question 6: Enregistrement des frames de la vidéo dans un vecteur
# La liste `gray_frames` contient déjà les frames en niveaux de gris

# Question 7: Calculer l'image moyenne de la vidéo sur M images
def calculer_moyenne(frames, M):
    # Initialisation de l'image moyenne avec des zéros
    moyenne = np.zeros_like(frames[0], np.float32)
    
    # Calcul de la moyenne sur M images
    for i in range(min(M, len(frames))):  # S'assurer que M ne dépasse pas le nombre de frames disponibles
        moyenne += frames[i]
    
    moyenne /= M
    return moyenne.astype(np.uint8)

# Utilisation de la fonction pour calculer la moyenne sur M images
M = 200  # Par exemple
if len(gray_frames) >= M:  # S'assurer qu'il y a suffisamment de frames pour calculer la moyenne
    image_moyenne = calculer_moyenne(gray_frames, M)
    cv2.imshow('Image Moyenne', image_moyenne)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

