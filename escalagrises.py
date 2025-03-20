import cv2
import time

cap = cv2.VideoCapture(0, cv2.CAP_V4L2) # backend DirectShow
time.sleep(1)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

cv2.namedWindow("color", cv2.WINDOW_NORMAL)
cv2.namedWindow("gris", cv2.WINDOW_NORMAL)
while True:
    ret, frame = cap.read()

    if not ret:
        print("No se pudo recibir el frame")
        break
    
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    cv2.imshow("gris", gris)
    cv2.imshow("color", frame)
    
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        print("Terminando programa")
        break
    
cap.release()
cv2.destroyAllWindows()