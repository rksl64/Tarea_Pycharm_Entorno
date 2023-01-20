texto = "Hola buenas Hola"

def contar(texto):
    textito = texto.split()
    palabras = {}
    for i in textito:
        if i in palabras:
            palabras[i] += 1
        else:
            palabras[i] = 1
    return palabras
    print(palabras)
print(contar(texto))


def repetida(palabras):
    max_repetida = ""
    max_frecuencia = 0

    for palabra, freq in palabras.items():
        if freq > max_frecuencia:
            max_repetida= palabra
            max_frecuencia = freq

    print(max_repetida, max_frecuencia)
    return max_repetida, max_frecuencia

repetida(contar(texto))