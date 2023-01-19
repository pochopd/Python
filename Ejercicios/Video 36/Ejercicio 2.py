## Video: Video 36.mp4
## Link al video: https://www.youtube.com/watch?v=0dEYVSRYl_s

## 1
# Modifica la función 'read()' para que imprima desde el décimo carácter.
# Ejecuta el ejercicio.
# La respuesta debe ser Esto es un.

from io import open

archivo = open('archivo.txt', 'r')

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN DEBAJO DE ESTE COMENTARIO #########

print(archivo.read())

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN ENCIMA DE ESTE COMENTARIO #########

archivo.close()