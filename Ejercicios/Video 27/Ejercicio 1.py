## Video: Video 27.mp4
## Link al video: https://www.youtube.com/watch?v=u_VbLsIyzRk

## 1
# Modifica la clase 'Moto()' para que herede las propiedades y métodos de la clase 'Vehiculos()'.
# Ejecuta el ejercicio.
# Las respuestas deben ser:
# Marca: Suzuki
# Modelo: Gn
# En marcha: False
# Acelerando: False
# Frenando: False

class Vehiculos():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True
    
    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nEn marcha: {self.enMarcha} \nAcelerando: {self.acelera} \nFrenando: {self.frena}")

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN DEBAJO DE ESTE COMENTARIO #########

class Moto():
    pass

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN ENCIMA DE ESTE COMENTARIO #########

moto1 = Moto("Suzuki","GN")
moto1.estado()