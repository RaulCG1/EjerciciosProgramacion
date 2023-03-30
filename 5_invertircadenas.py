"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def reverse_string(cadena_una):
    cadena_dos=cadena_una[::-1]
    print(cadena_una,cadena_dos)

reverse_string("Hola mundo")


def reverse_string_na(cadena_una):
    tamanio = len(cadena_una)
    cadena=""
    for index in range(0 , tamanio):
        cadena += cadena_una[tamanio-1 - index]

    print(cadena_una,cadena)

reverse_string_na("Hola mundo")