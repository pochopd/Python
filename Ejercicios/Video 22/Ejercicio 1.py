## Video: Video 22.mp4
## Link al video: https://www.youtube.com/watch?v=dLH-oay4Bts

## 1
# Modifica la función 'imprimoColor()' para que arroje un error de tipo 'NameError' con el mensaje 'Índice desconocido.'
# al ingresar un número mayor a 5.
# Ejecuta el ejercicio.
# La respuesta debe ser Naranja.
# La respuesta debe ser Amarillo.
# La respuesta debe ser NameError: Índice desconocido.

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN DEBAJO DE ESTE COMENTARIO #########

def imprimoColor(numero):
    if numero == 1:
        print("Naranja")
    elif numero == 2:
        print("Azul")
    elif numero == 3:
        print("Violeta")
    elif numero == 4:
        print("Amarillo")
    elif numero == 5:
        print("Verde")
    else:
        print("Índice desconocido")

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN ENCIMA DE ESTE COMENTARIO #########

imprimoColor(1)
imprimoColor(4)
imprimoColor(6)