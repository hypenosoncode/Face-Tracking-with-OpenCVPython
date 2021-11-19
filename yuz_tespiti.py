import cv2
import numpy as np

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

face_cascade = cv2.CascadeClassifier("goruntu_isleme_yuz_algilama/haarcascade_frontalface_default.xml")

while True:

    ret, frame = capture.read()
   
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5)

    for (x, y, w, h) in faces:

        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), thickness = 1)

        text = "Yuz algilandi!"
        koordinat = (x+w -20, y-20)
        yazi_tipi = cv2.FONT_HERSHEY_DUPLEX
        olcek = 1
        renk = (0, 0, 255)
        kalinlik = 1

        cv2.putText(frame, text, koordinat, yazi_tipi, olcek, renk, kalinlik)

        cv2.imshow("Yuz Algilama Ekrani", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
capture.release()
cv2.destroyAllWindows()