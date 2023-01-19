## Video: Video 38.mp4
## Link al video: https://www.youtube.com/watch?v=CkfDnMC79b4

## 1
# Modifica la función 'open' para que el método de apertura sea lectura binaria.
# En la variable listaDePersonas asigna como valor la función 'load()' del módulo pickle, pasando como parámetro
# la variable 'archivo'.
# Ejecuta el ejercicio.
# La respuesta debe ser
# Hola, mi nombre es Jhon Doe y tengo 40 años de edad.
# Hola, mi nombre es Alice Doe y tengo 37 años de edad.
# Hola, mi nombre es Ian Doe y tengo 29 años de edad.

import pickle
from io import open

class Persona():
    def __init__ (self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def presentacion (self):
        print(f'Hola, mi nombre es {self.nombre} {self.apellido} y tengo {self.edad} años de edad.')

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN DEBAJO DE ESTE COMENTARIO #########

archivo = open('listaDePersonas', 'w')

listaDePersonas = 

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN ENCIMA DE ESTE COMENTARIO #########

archivo.close()

for i in listaDePersonas:
    print(i.presentacion())