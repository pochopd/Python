## Video: Video 35.mp4
## Link al video: https://www.youtube.com/watch?v=V87m9SltcI8

## 1
# Modifica la función 'open' para que el modo de apertura sea lectura.
# Ejecuta el ejercicio.
# La respuesta debe ser Esto es un texto de ejemplo.

from io import open

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN DEBAJO DE ESTE COMENTARIO #########

archivo = open('archivo.txt', 'w')

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN ENCIMA DE ESTE COMENTARIO #########

texto = archivo.read()

archivo.close()

print(texto)
