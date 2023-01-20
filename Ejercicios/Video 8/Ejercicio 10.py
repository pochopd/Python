## Video: Video 8.mp4
## Link al video: https://www.youtube.com/watch?v=vawEHhV_HFA

## 1
# Escribir una función llamada desempaquetado_dict() que reciba un diccionario con las claves 'a', 'b' y 'c' y sus 
# respectivos valores. 
# La función debe asignar cada valor a una variable distinta y luego imprimir cada variable una junto a otra
# separadas por un espacio.
# Ejecuta el ejercicio.
# La respuesta debe ser 5 8 10.



######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN DEBAJO DE ESTE COMENTARIO #########

def desempaquetado_dict(mi_dict):
    a = mi_dict['a']
    b = mi_dict['b']
    c = mi_dict['c']
    print(a, end = " ")
    print(b, end = " ")
    print(c, end = " ")

######### CAMBIA SOLAMENTE LAS LÍNEAS DE CÓDIGO QUE ESTÁN ENCIMA DE ESTE COMENTARIO #########

mi_dict = {'a':5, 'b':8, 'c':10}
desempaquetado_dict(mi_dict)