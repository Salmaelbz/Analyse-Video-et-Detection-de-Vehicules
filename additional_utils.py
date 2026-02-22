import cv2
import numpy as np

# Chemin vers les fichiers de YOLO
yolo_weights = 'yolov3.weights'
yolo_config = 'yolov3.cfg'
classes_file = 'coco.names'

# Charger les noms des classes
with open(classes_file, 'r') as f:
    classes = [line.strip() for line in f.readlines()]

# Charger le réseau YOLO
net = cv2.dnn.readNet(yolo_weights, yolo_config)

# Chemin vers la vidéo de l'autoroute
video_path = 'autoroute3.mp4'

# Création d'un objet VideoCapture
cap = cv2.VideoCapture(video_path)

# Vérification de l'ouverture du flux vidéo
if not cap.isOpened():
    print("Erreur lors de l'ouverture de la vidéo")
    exit()

# Initialisation des variables
compteur_voitures = 0
voitures_detectees = []

# Ralentir la vidéo en augmentant le délai dans cv2.waitKey()
delay = 100

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Pré-traitement de l'image pour YOLO
    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)

    # Obtenir les noms des couches de sortie
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    # Effectuer la détection d'objets
    detections = net.forward(output_layers)

    # Boucle sur les détections
    for detection in detections:
        for object in detection:
            scores = object[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:  # Seuil de confiance
                # Obtenir les coordonnées de la boîte englobante
                center_x, center_y, width, height = (object[0:4] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])).astype('int')
                x = int(center_x - width / 2)
                y = int(center_y - height / 2)

                # Ajouter la détection à la liste des voitures détectées
                voitures_detectees.append((x, y, width, height))
                compteur_voitures += 1

    # Afficher les résultats
    for (x, y, width, height) in voitures_detectees:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
        cv2.putText(frame, "Voitures: {}".format(compteur_voitures), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Détection YOLO', frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

print("Nombre total de voitures détectées dans la vidéo :", compteur_voitures)

cap.release()
cv2.destroyAllWindows()