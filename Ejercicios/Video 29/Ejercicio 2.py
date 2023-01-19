## Video: Video 29.mp4
## Link al video: https://www.youtube.com/watch?v=oe04X1B14YY

## 1
# Modifica la clase 'Moto' para que su constructor acepte cuatro parámetros: ruedas, marca, modelo y anioFabricacion.
# Ejecuta el ejercicio.
# La respuesta debe ser
# Marca: Suzuki, modelo: V Strom, anio de fabricación: 2021
# Este vehículo posee 2 ruedas

class Vehiculo():
    
    def __init__(self, marca, modelo, anioFabricacion):
        self.marca = marca
        self.modelo = modelo
        self.anioFabricacion = anioFabricacion
    
    def muestraDatos(self):
        print(f'Marca: {self.marca}, modelo: {self.modelo}, anio de fabricación: {self.anioFabricacion}')
        
######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN DEBAJO DE ESTE COMENTARIO #########

class Moto(Vehiculo):

    def __init__(self, ruedas):
        super().__init__('Yamaha', 'Vrr', 1982)
        self.ruedas = ruedas

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN ENCIMA DE ESTE COMENTARIO #########

moto1 = Moto(2, 'Suzuki', 'V Strom', 2021)
moto1.muestraDatos()
print(f'Este vehículo posee {moto1.ruedas} ruedas')