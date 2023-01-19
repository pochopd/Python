## Video: Video 29.mp4
## Link al video: https://www.youtube.com/watch?v=oe04X1B14YY

## 1
# Utiliza la función 'isinstance()' dentro de la función 'print()' para comprobar si el objeto
# 'moto1' es instancia de la clase 'Vehiculo'.
# Ejecuta el ejercicio.
# La respuesta debe ser True.

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

    def muestraDatos(self):
        super().muestraDatos()
        print(f'Ruedas: {self.ruedas}')

moto1 = Moto(2, 'Suzuki', 'Ax 100', 1995)

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN DEBAJO DE ESTE COMENTARIO #########
    
print()

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN ENCIMA DE ESTE COMENTARIO #########

