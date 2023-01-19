## Video: Video 25.mp4
## Link al video: https://www.youtube.com/watch?v=x5CY8fVyYLo

## 1
# Crea un objeto llamado 'persona1' de la clase 'Persona' y llama a su método 'estudiar'.
# Crea otro objeto llamado 'persona2' de la clase 'Persona' y llama a su método 'saludar'.

## 2
# Llama al método 'estado' de persona1.
# Llama al método 'estado' de persona2.
# Ejecuta el ejercicio.
# Las respuestas deben ser
# Hola! Buenas tardes.
# True
# False

class Persona():
    nombre = 'Jhon'
    edad = 26
    altura = 1.70
    estudiando = False

    def saludar(self):
        print('Hola! Buenas tardes.')

    def estudiar(self):
        self.estudiando = True
    
    def estado(self):
        print(self.estudiando)
        
######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN DEBAJO DE ESTE COMENTARIO #########



######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN ENCIMA DE ESTE COMENTARIO #########