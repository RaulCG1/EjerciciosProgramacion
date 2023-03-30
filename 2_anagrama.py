"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def anagrama(palabra_1, palabra_2):
    palabra_2=palabra_2[::-1]
    palabra_2=palabra_2.lower().capitalize()
    print(palabra_1,palabra_2)
    if palabra_1 == palabra_2:
        print("La palabra es un anagrama")

anagrama("Amor","Roma")

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    print(sorted(word_one.lower()))
    print(sorted(word_two.lower()))
    return sorted(word_one.lower()) == sorted(word_two.lower())


print(is_anagram("Amor", "Amor"))