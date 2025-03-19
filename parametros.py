import cv2
import time

cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
time.sleep(2)

brillo = cap.get(cv2.CAP_PROP_BRIGHTNESS) #Brillo de la imagen 0 255
print("Brillo original", brillo)
cap.set(cv2.CAP_PROP_BRIGHTNESS, 128)

contraste = cap.get(cv2.CAP_PROP_CONTRAST) #Contraste de la imagen 0 255
print("Contraste original", contraste)
cap.set(cv2.CAP_PROP_CONTRAST, 128)

saturacion = cap.get(cv2.CAP_PROP_SATURATION) #Saturación 0 255
print("Satruación original", saturacion)
cap.set(cv2.CAP_PROP_SATURATION, 128)

cv2.namedWindow("Webcam", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()

    if not ret:
        print("No se pudo recibir el frame")
        break
    
    cv2.imshow("Webcam", frame)
    
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        print("Terminando programa")
        break
    
cap.release()
cv2.destroyAllWindows()