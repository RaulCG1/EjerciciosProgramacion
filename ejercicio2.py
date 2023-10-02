#tripes pitagoricos

#a2 - b2 = c2  ejemplo
#82+152=?172
#64+225=289
#289=289

#  * Crea una función que encuentre todos los triples pitagóricos
#  * (ternas) menores o iguales a un número dado.
#  * - Debes buscar información sobre qué es un triple pitagórico.
#  * - La función únicamente recibe el número máximo que puede
#  *   aparecer en el triple.
#  * - Ejemplo: Los triples menores o iguales a 10 están
#  *   formados por (3, 4, 5) y (6, 8, 10).
#  *


def triples_pitagoricos(maximo):
    triples = []
    for a in range(1, maximo + 1):
        
        for b in range(a, maximo + 1):
            c = (a**2 + b**2)**0.5
            print(c)
            if c.is_integer() and c <= maximo:
                triples.append((a, b, int(c)))
    return triples

print(triples_pitagoricos(10))


