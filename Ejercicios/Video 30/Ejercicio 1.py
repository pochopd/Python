## Video: Video 30.mp4
## Link al video: https://www.youtube.com/watch?v=kV1cN_bqcSw

## 1
# Modifica el código escrito para conseguir la misma respuesta utilizando la función 'presentacion()'.
# La respuesta debe ser
# Baw Baw! Soy un perro pequeño.
# Guau Guau! Soy un perro mediano.
# Wof Wof! Soy un perro grande.

class Chihuahua():
    def __init__(self):
        self.tamanio = 'pequeño'
    def presentar(self):
        print(f'Baw Baw! Soy un perro {self.tamanio}')

class Doberman():
    def __init__(self):
        self.tamanio = 'mediano'
    def presentar(self):
        print(f'Guau Guau! Soy un perro {self.tamanio}')

class GranDanes():
    def __init__(self):
        self.tamanio = 'grande'
    def presentar(self):
        print(f'Wof Wof! Soy un perro {self.tamanio}')

def presentacion(raza):
    raza.presentar()

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN DEBAJO DE ESTE COMENTARIO #########

perro1 = Chihuahua()
perro1.presentar()

perro2 = Doberman()
perro2.presentar()

perro3 = GranDanes()
perro3.presentar()

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN ENCIMA DE ESTE COMENTARIO #########