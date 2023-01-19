## Video: Video 29.mp4
## Link al video: https://www.youtube.com/watch?v=oe04X1B14YY

## 1
# Modifica el método 'muestraDatos' de la clase 'Moto' utilizando la función 'super()' para que al llamarlo 
# imprima la marca, el modelo y el año de fabricación pasados por parámetro al momento de instanciar 'moto1'.
# Ejecuta el ejercicio.
# La respuesta debe ser Marca: Suzuki, modelo: Ax 100, anio de fabricación: 1995, Ruedas: 2.

class Vehiculo():
    
    def __init__(self, marca, modelo, anioFabricacion):
        self.marca = marca
        self.modelo = modelo
        self.anioFabricacion = anioFabricacion
    
    def muestraDatos(self):
        print(f'Marca: {self.marca}, modelo: {self.modelo}, anio de fabricación: {self.anioFabricacion},', end = ' ')

class Moto(Vehiculo):

    def __init__(self, ruedas, marca, modelo, anioFabricacion):
        super().__init__(marca, modelo, anioFabricacion)
        self.ruedas = ruedas

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN DEBAJO DE ESTE COMENTARIO #########
    
    def muestraDatos(self):
        print(f'Ruedas: {self.ruedas}')

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN ENCIMA DE ESTE COMENTARIO #########

moto1 = Moto(2, 'Suzuki', 'Ax 100', 1995)
moto1.muestraDatos()

