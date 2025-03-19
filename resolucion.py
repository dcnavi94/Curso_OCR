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

time.sleep(1)

ancho = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
alto = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Resolucion original", ancho,alto)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

time.sleep(1)

expo = cap.get(cv2.CAP_PROP_EXPOSURE) #Exposición -11 -2
print("Exposición original", expo)
cap.set(cv2.CAP_PROP_EXPOSURE, -4)
expo = cap.get(cv2.CAP_PROP_EXPOSURE) #Exposición -11 -2
print("Exposición modificada", expo)

time.sleep(1)

ganancia = cap.get(cv2.CAP_PROP_GAIN) #Ganancia 0 255
print("Ganancia original", ganancia)
cap.set(cv2.CAP_PROP_GAIN, 149) #Ganancia 0 255
time.sleep(1)
focus = cap.get(cv2.CAP_PROP_FOCUS)
print("Enfoque original", focus)
focusAuto = cap.get(cv2.CAP_PROP_AUTOFOCUS) #1.0 autofocus 2.0 manual
print("Autoenfoque activado?", focusAuto)
x = cap.set(cv2.CAP_PROP_FOCUS, 15)
print(x)




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