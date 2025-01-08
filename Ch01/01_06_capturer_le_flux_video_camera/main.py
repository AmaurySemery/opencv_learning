import cv2

# Charger la vidéo
cap = cv2.VideoCapture("../../Data/video_01.mp4")

# Récupérer la fréquence d'images (fps)
fps = cap.get(cv2.CAP_PROP_FPS)
factor = 0.75
delay = int((1000 / fps) * factor)  # Temps d'attente entre les frames en millisecondes

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Redimensionner l'image
    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # Afficher l'image
    cv2.imshow("Image", frame)
    cv2.moveWindow("Image", 0, 0)

    # Attendre une durée adaptée à la cadence vidéo
    ch = cv2.waitKey(delay)
    if ch & 0xFF == ord("q"):
        break

# Libérer les ressources
cap.release()
cv2.destroyAllWindows()