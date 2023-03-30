"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

def esprimo():
    for numero in range(1,101):
        is_divisible = False
        if numero >= 2:
            for dividento in range(2,numero):
                if numero%dividento == 0:
                    is_divisible = True
                    break
            if not is_divisible:
                print(numero)


esprimo()