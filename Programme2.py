import cv2
import numpy as np

captureVideo=cv2.VideoCapture("Route.mp4")
while captureVideo.isOpened():

    retour, image = captureVideo.read()
    if retour is False:
        quit()

    #conversion (niveaux de gris) et filtrage (canny) d'une zone de l'image
    zoneGris=cv2.cvtColor(image[430:431, 420:510], cv2.COLOR_BGR2GRAY)
    arrayZoneDetection=cv2.Canny(zoneGris, 75, 150)
    #sur la vidéo la zone est matérialisée sous forme d'un rectangle rouge



    cv2.rectangle(image, (420, 430), (510, 432), (0, 0, 255), 1)
    #balayage des pixels de la zone de détection:

    s1=-1
    zoneDetection = arrayZoneDetection[0]







    if cv2.waitKey(1) == ord('q'):
        break


captureVideo.release()
cv2.destroyAllWindows()