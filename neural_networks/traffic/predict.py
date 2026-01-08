import cv2
import keras
import numpy as np
import sys

IMG_WIDTH = 30
IMG_HEIGHT = 30

LABELS = [
    "Panneau 20",
    "Panneau 30",
    "Panneau 50",
    "Panneau 60",
    "Panneau 70",
    "Panneau 80",
    "Panneau Fin 80",
    "Panneau 100",
    "Panneau 120",
    "Panneau Dépassement Interdit",
    "Panneau Dépassement Interdit Poids Lourds",
    "Panneau Priorité Ponctuelle",
    "Panneau Route Prioritaire",
    "Panneau Cédez Passage",
    "Panneau Stop",
    "Panneau Circulation Interdite",
    "Panneau Interdiction Poids Lourds",
    "Panneau Sens Interdit",
    "Panneau Danger",
    "Panneau Virage Gauche",
    "Panneau Virage Droit",
    "Panneau Série Virages Gauche",
    "Panneau Ralentisseur",
    "Panneau Chaussée Glissante",
    "Panneau Chaussée Rétrécie Droite",
    "Panneau Travaux",
    "Panneau Feu Tricolore",
    "Panneau Piéton",
    "Panneau Enfants",
    "Panneau Vélo",
    "Panneau Neige",
    "Panneau Animaux",
    "Panneau Fin Interdiction",
    "Panneau Obligation Tourner Droite",
    "Panneau Obligation Tourner Gauche",
    "Panneau Obligation Tout Droit",
    "Panneau Obligation Tourner Droite ou Tout Droit",
    "Panneau Obligation Tourner Gauche ou Tout Droit",
    "Panneau Flèche Bas Droit",
    "Panneau Flèche Bas Gauche",
    "Panneau Rond Point",
    "Panneau Fin Interdiction Dépassement",
    "Panneau Fin Interdiction Dépassement Poids Lourds"
]


def main():
    """
    This program is meant to be used on an image to predict which traffic sign appears in it.
    In order to use it, a model needs to be generated first, using the `traffic.py` program on a data set.
    """

    # Check command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python test.py <model> <image>")

    filename_model = sys.argv[1]
    filename_image = sys.argv[2]

    # Load saved model
    model = keras.saving.load_model(filename_model)

    # Load image to predict
    image = cv2.imread(filename_image)
    redim = cv2.resize(image, (IMG_WIDTH, IMG_HEIGHT))
    
    # Add missing dimension (batch) to get correct tensor shape
    element = np.expand_dims(redim, axis=0)

    # Predict image label
    x = model.predict(element)
    idx = np.argmax(x)
    prob = x[0][idx]

    # Print the prediction result   
    print(f"\nResult: {LABELS[idx]} ({prob * 100:.2f}%)\n")


if __name__ == "__main__":
    main()
