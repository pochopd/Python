## Video: Video 28.mp4
## Link al video: https://www.youtube.com/watch?v=jMQQN9OxwVc

## 1
# Modifica la clase 'Moto()' para que posea un nuevo método llamado 'sonidoEncendido'. Al ser llamado debe
# imprimir 'Brum brum! brum brum!'.
# Ejecuta el ejercicio.
# La respuesta debe ser
# Brum brum! brum brum!
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

class Moto(Vehiculos):

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN DEBAJO DE ESTE COMENTARIO #########

    pass

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN ENCIMA DE ESTE COMENTARIO #########

moto1 = Moto("Suzuki", "Akira")
moto1.sonidoEncendido()
moto1.estado()