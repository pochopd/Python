## Video: Video 24.mp4
## Link al video: https://www.youtube.com/watch?v=Y_SiIgxc-xI

## 1
# Modifica el cuerpo del método 'estudiar()' para modificar la propiedad 'estudiando' a 'True' utilizando
# la palabra reservada 'self'.
# Ejecuta el ejercicio.
# La respuesta debe ser True.

class Persona():
    nombre = "Jhon"
    edad = 26
    altura = 1.70
    estudiando = False

    def saludar(self):
        print("Hola!")

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN DEBAJO DE ESTE COMENTARIO #########

    def estudiar(self):
        pass

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN ENCIMA DE ESTE COMENTARIO #########

persona1 = Persona()
persona1.estudiar()
print(persona1.estudiando)