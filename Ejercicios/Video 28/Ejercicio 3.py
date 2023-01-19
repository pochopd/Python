## Video: Video 28.mp4
## Link al video: https://www.youtube.com/watch?v=jMQQN9OxwVc

## 1
# Modifica la clase 'MotoElectrica()' para que herede las propiedades y métodos de las clases 'Vehiculos' y
# 'VElectricos'.
# Ejecuta el ejercicio.
# La respuesta debe ser
# Marca: Sunra 
# Modelo: Miku Super
# En marcha: True
# Acelerando: False
# Frenando: False
# El vehículo está cargando.

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
        print(f'Marca: {self.marca} \nModelo: {self.modelo} \nEn marcha: {self.enMarcha} \nAcelerando: {self.acelera} \nFrenando: {self.frena}')

class VElectricos():

    def __init__(self):
        self.cargando = False

    def cargarEnergia(self):
        self.cargando = True

    def estadoCarga(self):
        if self.cargando == True:
            print('El vehículo está cargando.')
        else:
            print('El vehículo no está en carga.')

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN DEBAJO DE ESTE COMENTARIO #########

class MotoElectrica():
    pass

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN ENCIMA DE ESTE COMENTARIO #########

moto1 = MotoElectrica('Sunra','Miku Super')
moto1.arrancar()
moto1.estado()
moto1.cargarEnergia()
moto1.estadoCarga()