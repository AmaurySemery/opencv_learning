import cv2

# Charger l'image depuis le chemin spécifié
img = cv2.imread("../../Data/image_01.png")

# Vérifier si l'image a bien été chargée
if img is None:
    print("Erreur : Impossible de charger l'image. Vérifiez le chemin.")
else:
    # Créer une fenêtre nommée "Image"
    cv2.namedWindow("Image")

    # Afficher l'image dans la fenêtre
    cv2.imshow("Image", img)

    # Déplacer la fenêtre à la position (0, 0)
    cv2.moveWindow("Image", 0, 0)

    # Attendre la pression d'une touche
    cv2.waitKey(0)

    # Sauvegarder l'image sous un nouveau nom
    cv2.imwrite("image_01_opencv.png", img)

    # Fermer toutes les fenêtres ouvertes
    cv2.destroyAllWindows()