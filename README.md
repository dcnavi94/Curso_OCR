# Curso_OCR
codigos y notas del curso OCR
librerias a instalar 
  opencv-contrib-python
  scikit-learn
  imutils
  
Backends:
Sistema Operativo 	Backend 	Descripción/Características
Windows 	cv2.CAP_DSHOW 	DirectShow, backend antiguo y eficiente para cámaras y dispositivos multimedia. Compatible con hardware más antiguo.
Windows 	cv2.CAP_MSMF 	Media Foundation, backend moderno para cámaras y multimedia. Soporta códecs y hardware más nuevos.
Windows 	cv2.CAP_VFW 	Video for Windows, un backend muy antiguo y menos eficiente. Generalmente no recomendado.
Linux 	cv2.CAP_V4L2 	Video4Linux2, el backend estándar para dispositivos de captura de video en Linux. Compatible y eficiente.
Linux 	cv2.CAP_GSTREAMER 	GStreamer, un backend avanzado que soporta transmisión y procesamiento de video mediante plugins.
macOS 	cv2.CAP_AVFOUNDATION 	AVFoundation, backend moderno de Apple para cámaras y multimedia. Optimizado para macOS.
Todos 	cv2.CAP_FFMPEG 	FFmpeg, backend multiplataforma que soporta una gran variedad de formatos de video y códecs.
Todos 	cv2.CAP_IMAGES 	Backend genérico para trabajar con imágenes estáticas

Documentacion 
  https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
  https://docs.opencv.org/3.4/d8/d01/group__imgproc__color__conversions.html
 orden de codigo 
  hola mundo
  escalagrises
  suavizadofiltrosgaussianos
  metodootsu
  morfologia1
  morfologia2
  roiimagenes
  deteccionContornos
  calculoCentroides
  extraccionAislamiento
  gimptratamiento
  extraccioncaracteristicas a partir de imagenes
  entrenamiento de clasificador lineal con linearsvc
  almacenamiento y carga de modelo 
  uso de modelo entrenado para clasificar caracteres detectados
  evaluacion de cadenas de texto 
