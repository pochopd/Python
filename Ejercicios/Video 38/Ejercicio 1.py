## Video: Video 38.mp4
## Link al video: https://www.youtube.com/watch?v=CkfDnMC79b4

## 1
# Asigna como valor de la variable 'listaDePersonas' una lista con los objetos 'persona1', 'persona2' y 'persona3'.
# Asigna como valor de la variable archivo la función 'opnen' con los parámetros 'listaDePersonas' y el parámetro
# correspondiente para abrir el archivo en modo escritura binaria.
# Utiliza la función 'dump' del módulo pickle con las variables 'listaDePersonas' y 'archivo' como parámetros.

import pickle
from io import open

class Persona():
    def __init__ (self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def presentacion (self):
        print(f'Hola, mi nombre es {self.nombre} {self.apellido} y tengo {self.edad} años de edad.')

persona1 = Persona('Jhon', 'Doe', 40)
persona2 = Persona('Alice', 'Doe', 37)
persona3 = Persona('Ian', 'Doe', 29)

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN DEBAJO DE ESTE COMENTARIO #########

listaDePersonas = 

archivo = 

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN ENCIMA DE ESTE COMENTARIO #########

archivo.close()

del archivo