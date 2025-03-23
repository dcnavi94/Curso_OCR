#EXTRACCION DE CARACTERISTICAS APARTIR DE IMAGENES

import cv2
import time
import numpy as np
import uuid
import os



def procesarImagen(img, kernelSG, kernelSM, metodoBinary):
    metodosBinary = {"normal": cv2.THRESH_BINARY, "invertido": cv2.THRESH_BINARY_INV}
    gaussiana = cv2.GaussianBlur(img, kernelSG, 0)
    umbral, binaria = cv2.threshold(gaussiana, 0, 255, metodosBinary[metodoBinary] + cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSM)
    erosionada = cv2.morphologyEx(binaria, cv2.MORPH_OPEN, kernel)   
    return erosionada


def obtenerMomentos(contorno):
    M = cv2.moments(contorno)
    area = M['m00']
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    return area, (cx,cy), M


def agregarBorde(imagen):
    h,w = imagen.shape
    borde = 25
    nuevoAlto = h + 2*borde
    nuevoAncho = w + 2*borde
    imgBorde = np.zeros((nuevoAlto, nuevoAncho), dtype = np.uint8)
    imgBorde[borde:borde+h, borde:borde+w] = imagen
    return imgBorde



def etiquetarImagenes(ordenado, dictCaracteres, cadena):
    for i, clave in enumerate(ordenado):
        imagenChar = dictCaracteres[clave]
        miUUID = str(uuid.uuid1())
        
        rutaCarpeta = "./trainOCR/"+cadena[i]
        if not os.path.exists(rutaCarpeta):
            os.makedirs(rutaCarpeta)
        cv2.imwrite("./trainOCR/"+cadena[i]+"/"+miUUID+".jpg", imagenChar)


cap = cv2.VideoCapture(0, cv2.CAP_V4L2) # backend DirectShow
time.sleep(1)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

cv2.namedWindow("erosionada", cv2.WINDOW_NORMAL)
cv2.namedWindow("resultadoContornos", cv2.WINDOW_NORMAL)
cv2.namedWindow("recorte", cv2.WINDOW_NORMAL)

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
        dictCaracteres = {}
        for contorno in contornos:
            area, centroide, M = obtenerMomentos(contorno)
            if area > 10:
                xcont, ycont, wcont, hcont = cv2.boundingRect(contorno)
                cv2.rectangle(frame, (xcont + x, ycont + y), (xcont + wcont + x, ycont + hcont + y), (0, 255, 0), 2) 
                recorte = erosionada[ycont:ycont+hcont, xcont:xcont+wcont]
                
                imgCaracterThBorde = agregarBorde(recorte)
                imgCaracterTh128 = cv2.resize(imgCaracterThBorde, (128,128))
                
                dictCaracteres[centroide[0]] = imgCaracterTh128
                
        ordenado = sorted(dictCaracteres.keys())
        
        for clave in ordenado:
            caracter = dictCaracteres[clave]
            caracteristicas = caracter.flatten()
            caracteristicas = np.array([caracteristicas])
        

        cv2.imshow("resultadoContornos", frame)
        cv2.imshow("erosionada", erosionada)
        cv2.imshow("recorte", caracter)
        
        key = cv2.waitKey(1)
        
        if key == ord('q'):
            print("Terminando programa")
            break
        
        elif key == 32: # codigo ASCII para barra espaciadora
            cadena = input("Ingresa los caracteres reales: ")
            cadena = cadena.upper().replace(" ", "")
            if len(cadena) == len(ordenado):
                etiquetarImagenes(ordenado, dictCaracteres, cadena)
            else:
                print("La cantidad de caracteres de la cadena no coincide con los caracteres detectados en la imagen")
    
    if cuenta <= 10:
        cuenta += 1
        
cap.release()
cv2.destroyAllWindows()