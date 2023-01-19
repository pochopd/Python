## Video: Video 28.mp4
## Link al video: https://www.youtube.com/watch?v=jMQQN9OxwVc

## 1
# Sobreescribe el método 'estado()' en la clase hija 'Moto()' para que imprima luego de 'Modelo: {self.modelo}'
# el texto 'Ruedas: {self.ruedas}'.
# Ejecuta el ejercicio.
# La respuesta debe ser
# Marca: Suzuki 
# Modelo: RGTV2
# Ruedas: 2
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
        print(f'Marca: {self.marca} \nModelo: {self.modelo} \nEn marcha: {self.enMarcha} \nAcelerando: {self.acelera} \nFrenando: {self.frena}')

class Moto(Vehiculos):

    ruedas = 2

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN DEBAJO DE ESTE COMENTARIO #########

    def estado(self):
        print(f'Marca: {self.marca} \nModelo: {self.modelo} \nEn marcha: {self.enMarcha} \nAcelerando: {self.acelera} \nFrenando: {self.frena}')

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN ENCIMA DE ESTE COMENTARIO #########

moto1 = Moto('Suzuki', 'RGTV2')
moto1.estado()