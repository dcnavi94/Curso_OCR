import cv2
import time


def procesarImagen(img, kernelSG, kernelSM, metodoBinary):
    metodosBinary = {"normal": cv2.THRESH_BINARY, "invertido": cv2.THRESH_BINARY_INV}
    gaussiana = cv2.GaussianBlur(img, kernelSG, 0)
    umbral, binaria = cv2.threshold(gaussiana, 0, 255, metodosBinary[metodoBinary] + cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSM)
    erosionada = cv2.morphologyEx(binaria, cv2.MORPH_OPEN, kernel)   
    return erosionada


cap = cv2.VideoCapture(0, cv2.CAP_V4L2) # backend DirectShow
time.sleep(1)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

cv2.namedWindow("erosionada", cv2.WINDOW_NORMAL)
cv2.namedWindow("resultadoContornos", cv2.WINDOW_NORMAL)

cuenta = 10
while True:
    ret, frame = cap.read()

    if not ret:
        print("No se pudo recibir el frame")
        break
    
    if cuenta == 10:
        x, y, w, h = cv2.selectROI("Seleccionar ROI", frame)
        cv2.destroyWindow("Seleccionar ROI")
    
    elif cuenta > 10:
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gris = gris[y:y+h, x:x+w]
        
        erosionada = procesarImagen(gris, (5,5), (5,5), "normal")
        
        contornos, _ = cv2.findContours(erosionada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # cv2.drawContours(frame, contornos, -1, (0, 255, 0), 2)
        
        for contorno in contornos:
            xcont, ycont, wcont, hcont = cv2.boundingRect(contorno)
            cv2.rectangle(frame, (xcont + x, ycont + y), (xcont + wcont + x, ycont + hcont + y), (0, 255, 0), 2) 

        cv2.imshow("resultadoContornos", frame)
        cv2.imshow("erosionada", erosionada)
        
        key = cv2.waitKey(1)
        
        if key == ord('q'):
            print("Terminando programa")
            break
    
    if cuenta <= 10:
        cuenta += 1
        
cap.release()
cv2.destroyAllWindows()