import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("No se pudo recibir el frame")
        break
    
    cv2.imshow("Webcam", frame) # Mostrar la imagen
    
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()