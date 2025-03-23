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

cuenta = 0
while True:
    ret, frame = cap.read()

    if not ret:
        print("No se pudo recibir el frame")
        break
    
    if cuenta == 10:
        x, y, w, h = cv2.selectROI("Seleccionar ROI", frame)
        print((x,y),(x+w,y), (x+w, y+h), (x, y+h))
        cv2.destroyWindow("Seleccionar ROI")
    
    elif cuenta > 10:
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        gris = gris[y:y+h, x:x+w]
        
        
        gaussiana = cv2.GaussianBlur(gris, (5, 5), 0)
    
        umbral, binaria = cv2.threshold(gaussiana, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        
        erosionada = cv2.morphologyEx(binaria, cv2.MORPH_OPEN, kernel)
        
    
        
        cv2.imshow("gris", gris)
        cv2.imshow("gaussiana", gaussiana)
        cv2.imshow("binaria", binaria)
        cv2.imshow("erosionada", erosionada)
        
        key = cv2.waitKey(1)
        
        if key == ord('q'):
            print("Terminando programa")
            break
    
    if cuenta <= 10:
        cuenta += 1
        
cap.release()
cv2.destroyAllWindows()