"""
/*
 * Reto #38
 * BINARIO A DECIMAL
 * Fecha publicación enunciado: 19/09/22
 * Fecha publicación resolución: 27/09/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa se encargue de transformar un número binario a decimal sin utilizar
 * funciones propias del lenguaje que lo hagan directamente.
 *
 * Información adicional:
 * - Usa el canal de nuestro Discord (https://mouredev.com/discord) "🔁reto-semanal"
 *   para preguntas, dudas o prestar ayuda a la comunidad.
 * - Tienes toda la información sobre los retos semanales en
 *   https://retosdeprogramacion.com/semanales2022.
 *
 */
"""


def binariodecimal(binario):
    inc = 0
    numero=0
    miset= set()
    tam=len(binario)
    
    for n in range(0,tam):
        valor = binario[tam-1-n] 
        if valor =="1":
            var = ((1*2)**inc)
            miset.add(var)
        elif valor =="0":
            var = ((0*2)**inc)
            miset.add(var)
        
        inc += 1
    print(sum(miset))

def decimalbinario(num):
    cadena=""
    while True:
        if num == 0:
            
            break
        if num%2 == 0:
            cadena +="0"
            num = int (num/2)
        elif num%2 == 1:
            cadena +="1"
            num= int(num/2)
    cadena = cadena[::-1]    
    print(cadena)

binariodecimal("2")

decimalbinario(37)