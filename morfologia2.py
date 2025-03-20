import cv2

gris = cv2.imread("01.jpeg", 0)

cv2.namedWindow("gris", cv2.WINDOW_NORMAL)
cv2.namedWindow("gaussiana", cv2.WINDOW_NORMAL)
cv2.namedWindow("binaria", cv2.WINDOW_NORMAL)
cv2.namedWindow("dilatada", cv2.WINDOW_NORMAL)

gaussiana = cv2.GaussianBlur(gris, (9, 9), 0)

umbral, binaria = cv2.threshold(gaussiana, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))

# dilatada = cv2.dilate(binaria, kernel, iterations=1)
cierre = cv2.morphologyEx(binaria, cv2.MORPH_CLOSE, kernel)



cv2.imshow("gris", gris)
cv2.imshow("gaussiana", gaussiana)
cv2.imshow("binaria", binaria)
cv2.imshow("dilatada", cierre)

cv2.waitKey(0)

    
cv2.destroyAllWindows()