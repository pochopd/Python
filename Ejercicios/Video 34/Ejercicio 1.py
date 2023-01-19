## Video: Video 34.mp4
## Link al video: https://www.youtube.com/watch?v=Zf9sN-w0BVE

## 1
# En el directorio 'Video 34' crea un archivo llamado 'setup.py'.
# Dentro del archivo 'setup.py' declara la sentencia 'from setuptools import setup'.
# Declara la función setup y dentro de ella indica lo siguiente:

name = 'paquetesaludos',
version = '1.0',
description = 'Imprime saludos',
author = 'Tu nombre',
author_email = 'jhon_doe@example.com',
url= 'www.jhondoe.com.ar',
packages = ['saludos']

## 2
# Abre una terminal y navega hasta el directorio 'Video 34'.
# Ingresa: 'python setup.py sdist'.
# Luego de finalizado el proceso deben de haberse creado dos nuevos directorios en el mismo
# directorio: dist y paquetesaludos.egg-info.
# Dentro del directorio 'dist' debe haber un archivo comprimido llamado 'saludos-1.0'.

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN DEBAJO DE ESTE COMENTARIO #########



######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN ENCIMA DE ESTE COMENTARIO #########