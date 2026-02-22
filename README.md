# Analyse Vidéo et Détection de Véhicules : Soustraction de Fond, Région d'Intérêt (ROI) et Masquage

Ce projet traite des flux vidéo (autoroute, routes) pour en extraire des informations : métadonnées, fond moyen, régions d, masques et détection de véhicules par soustraction de fond.

---

## Objectifs et contenu

1. **Analyse des vidéos** : durée, nombre de frames, résolution, FPS.
2. **Modélisation du fond** : image moyenne sur plusieurs frames.
3. **Région d (ROI)** : se concentrer sur une zone précise de l’image.
4. **Masques** : isoler la chaussée ou les véhicules selon l’intensité.
5. **Détection de véhicules** : soustraction de fond, seuillage, morphologie, contours.

---

## Description des scripts

### Analyse des métadonnées et image moyenne
`video_metadata.py`

- Charge `autoroute2.avi`.
- Affiche :
  - nombre de frames,
  - durée (en secondes),
  - résolution (largeur × hauteur).
- Convertit chaque frame en niveaux de gris et les stocke.
- Calcule l’image moyenne sur M frames (ex. M = 200) et l’affiche.

Utile pour comprendre la structure de la vidéo avant d’appliquer des algorithmes plus complexes.

---

### Visualisation vidéo (couleur et niveaux de gris)
`dual_view_player.py`

- Lit une vidéo (par défaut `autoroute2.avi`, ou chemin passé en argument).
- Affiche en parallèle :
  - la vidéo originale en couleur,
  - la même vidéo en niveaux de gris.
- Utilisation : `python autoroute.py [chemin_video]`.

---

### Détection par soustraction de fond et ROI
`roi_vehicle_detection.py`, `roi_vehicle_detection_v2.py`

**roi_vehicle_detection.py :**

- Lit `video.avi`.
- Définit une zone rectangulaire (ex. x, y, largeur, hauteur).
- Calcule le fond moyen uniquement dans cette zone.
- Applique la soustraction de fond pour détecter les véhicules.
- Utilise la morphologie (fermeture) pour nettoyer le masque binaire.
- Détecte les contours et dessine des rectangles autour des zones de mouvement.
- Affiche le fond moyen, le masque binaire et les véhicules détectés.

**roi_vehicle_detection_v2.py** : variante ou extension de la logique ROI.

---

### Isolation des véhicules par masque (seuillage)
`threshold_vehicle_segmentation.py`

- Lit une image de route (`route.png`).
- Définit deux seuils pour les pixels de la chaussée (ex. 120–185).
- Crée un masque avec `inRange` pour la route.
- Inverse le masque pour isoler les véhicules (zones plus sombres ou plus claires).
- Applique ce masque et affiche les véhicules isolés.

Fonctionne sur une image fixe, pas sur une vidéo.

---

### Exercices : lecture vidéo et conversion
`1.5.py`, `1.6.1.py`

Scripts d’exercice sur la lecture vidéo, conversion en niveaux de gris et calculs basiques.

---

### Opérations vidéo avancées (frame par frame)
`2.1.py` à `2.4.2.py`

Exercices sur la lecture, l’affichage, le traitement frame par frame et les opérations sur des séquences vidéo.

---

### Utilitaires et extensions du pipeline
`5.py`, `52.py`

Scripts de test ou d’extension du pipeline de traitement.

---

### Métriques de précision de la détection
`6.précision.py`

Calcule des métriques de précision (par ex. rappel, précision) pour la détection de véhicules.

---

### Chaîne complète et variantes
`final.py`, `inverse.py`, `essai1.py`

Scripts finaux ou variantes du traitement : enchaînement complet, inversion de masque, tests.

---

## Installation des dépendances

```bash
pip install -r requirements.txt
```

ou :

```bash
pip install opencv-python numpy
```

---

## Commandes de lancement

```bash
# Analyse de la vidéo (nombre de frames, durée, résolution, image moyenne)
python TP_4/video_metadata.py

# Affichage vidéo original + niveaux de gris
python TP_4/dual_view_player.py

# Détection de véhicules avec ROI et soustraction de fond
python TP_4/roi_vehicle_detection.py

# Masque sur une image fixe
python TP_4/threshold_vehicle_segmentation.py
```

Assure-toi d’avoir une vidéo (ex. `autoroute2.avi`, `video.avi`) et une image de route (ex. `route.png`) dans les chemins indiqués par chaque script.

---

## Arborescence du projet

```
TP4_ELBAZ/
├── TP_4/
│   ├── video_metadata.py                    # Analyse métadonnées vidéo
│   ├── dual_view_player.py                 # Lecteur vidéo double vue
│   ├── roi_vehicle_detection.py           # Détection véhicules ROI
│   ├── roi_vehicle_detection_v2.py         # Détection véhicules ROI v2
│   ├── threshold_vehicle_segmentation.py   # Segmentation par seuillage
│   ├── full_video_pipeline.py             # Pipeline complet
│   ├── inverse_mask_operations.py         # Opérations masque inverse
│   ├── experimental_test.py               # Tests expérimentaux
│   ├── video_utils.py                     # Utilitaires vidéo
│   ├── additional_utils.py                # Utilitaires additionnels
│   ├── detection_accuracy.py              # Métriques de précision
│   ├── frame_extractor.py                 # Extraction de frames
│   ├── basic_video_processing.py          # Traitement vidéo basique
│   ├── advanced_video_processing.py       # Traitement vidéo avancé
│   └── frame_operations_*.py              # Opérations sur frames
├── requirements.txt
└── README.md
```

---

## Informations pratiques

- Adapter les chemins de vidéo et d’image dans chaque script.
- Les seuils (soustraction, morphologie, contours) peuvent être ajustés selon la scène.
- La soustraction de fond suppose une caméra fixe.

---

**Auteur :** ELBAZ

