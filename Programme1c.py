import numpy as np
import cv2

captureVideo = cv2.VideoCapture('Autoroute.mp4')

while captureVideo.isOpened():
    retour, image = captureVideo.read()
    if retour is False:
        quit()
    #dessiner un rectangle rouge en haut à gauche de l'image

    cv2.rectangle(image, (20, 20), (100, 100), (0, 0, 255), 3)
    cv2.imshow('video avec rectangle rouge',image)
    if cv2.waitKey(1) == ord('q'):
        break

captureVideo.release()
cv2.destroyAllWindows()