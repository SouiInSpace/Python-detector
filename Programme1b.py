import numpy as np
import cv2

captureVideo = cv2.VideoCapture('Autoroute.mp4')

while captureVideo.isOpened():
    retour, image = captureVideo.read()
    if retour is False:
        quit()
    #convertir les couleurs de l'image en niveaux de gris
    imageGris=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('video en niveau de gris', imageGris)
    #filtrage de l'image avec la fonction "canny" qui détecte les contours des objets
    imageContours=cv2.Canny(imageGris, 50, 175) #on peut changer les valeurs de seuil 50 et 175



    cv2.imshow("video avec les contours des objets", imageContours)


    if cv2.waitKey(1) == ord('q'):
        break

captureVideo.release()
cv2.destroyAllWindows()




