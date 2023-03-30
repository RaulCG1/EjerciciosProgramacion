import random


def funcion(inicial):
    tam = len(inicial)
    sesentaporiento = int(tam*.6)
    print(sesentaporiento)
    vari = list(inicial)
    while True:
        place = random.randrange(0,tam)
        if vari.count("_") ==sesentaporiento:
          break
        vari[place] = "_"
    inicial= "".join(vari)
    
    return inicial


def ingresar(inicial,letra,palabra1):
    
    tam =len(inicial)
    word = list(palabra1)
    if  inicial == letra:
        return inicial
    for index,va in enumerate(inicial):
        if letra in inicial[index]:
            word [index] = letra    
    return word

remains = 5
intento = 0
palabra :str = "aguacate"

palabraadi =funcion(palabra)

while intento != remains:
    print(palabraadi)
    print(f"Intentos Restantes {remains}")
    remains -=1
    letra  = (input("Ingresa la letra: "))
    letra= str(letra)
    
    palabraadi=ingresar(palabra,letra,palabraadi)
    palabra1 = "".join(palabraadi)
    if palabra == palabra1:
        print(f"Juego acabado usted adivino la palabra: {palabra1}")
        break
    







