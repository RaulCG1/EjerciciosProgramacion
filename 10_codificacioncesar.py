texto = "Hola Calamardo"
texto = texto.upper()

lista = list(texto)

abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
cifrad =[]
k=3
"""ascii sencillo"""
for c in texto:
    cifrad += chr(ord(c)+3)

desi = []
#desincriptar
for c in cifrad:

    desi += chr(ord(c)-3)
textcifrado = []
for c in texto:
    if c in abc:
        valor= (abc.index(c) + 3) % 27
        textcifrado.append(abc[valor])
    else:
        textcifrado.append(" ")

textodesiflado= []
for c in textcifrado:
    if c != " ":
        valor= (abc.index(c) - 3) % 27
        textodesiflado.append(abc[valor])
    else:
        textodesiflado.append(" ")
print(textcifrado)
print(textodesiflado)
#print(str(cifrad))
#print(str(desi))

"""
for c in texto:
 if c in abc:
    cifrad += abc[(abc.index(c)+k%(len(abc)))]
 else:
     cifrad+=c
['K', 'R', 'O', 'D']
"""