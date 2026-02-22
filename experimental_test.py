import cv2
import numpy as np

class VehicleCounter:
    def __init__(self, area_pts, frame_shape):
        self.area_mask = self.create_area_mask(area_pts, frame_shape)
        self.bg_subtractor = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=True)
        self.vehicle_count = 0

    def create_area_mask(self, area_pts, frame_shape):
        mask = np.zeros(frame_shape[:2], dtype=np.uint8)  # Assurez-vous que le masque est de la même taille que le frame
        cv2.fillPoly(mask, [np.array(area_pts)], (255,))  # Utilisez un tuple à un élément pour la couleur
        return mask

    def count_vehicles(self, frame):
        # Appliquer le masque de la zone à la frame
        masked_frame = cv2.bitwise_and(frame, frame, mask=self.area_mask)
        fg_mask = self.bg_subtractor.apply(masked_frame)
        _, fg_mask = cv2.threshold(fg_mask, 250, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > 500:  # Filtre basé sur la taille de la voiture
                self.vehicle_count += 1
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        return frame

# Utilisation de la classe VehicleCounter
cap = cv2.VideoCapture('video.avi')
ret, frame = cap.read()
if not ret:
    print("Impossible de lire la vidéo.")
else:
    frame_shape = frame.shape
    area_pts = [(100, 200), (500, 200), (640, 400), (0, 400)]  # Points définissant la zone d'intérêt
    vehicle_counter = VehicleCounter(area_pts, frame_shape)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = vehicle_counter.count_vehicles(frame)
        cv2.imshow('Vehicle Counting', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"Nombre total de véhicules détectés : {vehicle_counter.vehicle_count}")