import cv2
import time

cap = cv2.VideoCapture(0, cv2.CAP_V4L2) # backend DirectShow
time.sleep(1)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

cv2.namedWindow("gris", cv2.WINDOW_NORMAL)
cv2.namedWindow("gaussiana", cv2.WINDOW_NORMAL)
cv2.namedWindow("binaria", cv2.WINDOW_NORMAL)
cv2.namedWindow("erosionada", cv2.WINDOW_NORMAL)
while True:
    ret, frame = cap.read()
    frame2 = frame.copy()

    if not ret:
        print("No se pudo recibir el frame")
        break
    
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gaussiana = cv2.GaussianBlur(gris, (3, 3), 0)

    umbral, binaria = cv2.threshold(gaussiana, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    # erosionada = cv2.erode(binaria, kernel, iterations=1)
    
    apertura = cv2.morphologyEx(binaria, cv2.MORPH_OPEN, kernel)
    
    cv2.imshow("gris", gris)
    cv2.imshow("gaussiana", gaussiana)
    cv2.imshow("binaria", binaria)
    cv2.imshow("erosionada", apertura)
    
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        print("Terminando programa")
        break
    
cap.release()
cv2.destroyAllWindows()