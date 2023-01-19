## Video: Video 26.mp4
## Link al video: https://www.youtube.com/watch?v=OU-e2uhoGxE

## 1
# Modifica la clase Persona para su método "moverCuerdasVocales"este encapsulado.
# Ejecuta el ejercicio.
# La respuesta debe estar vacía.

class Persona():
    
    def __init__(self):

        self.__piernas = 2
        self.__ojos = 2
        self.__brazos = 2
        self.__nariz = 1
        self.__boca = 1
        self.__moviendoCuerdasVocales = False
        
######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN DEBAJO DE ESTE COMENTARIO #########

    def moverCuerdasVocales(self):
        self.__moviendoCuerdasVocales = True

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN ENCIMA DE ESTE COMENTARIO #########

    def cantar(self):
        self.moverCuerdasVocales()
        print("La la la! Tu ru ru! Hey!")

    def saludar(self):
        print("Hola!, buenas tardes.")
    
persona1 = Persona()