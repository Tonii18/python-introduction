def cuenta_letras(*palabras):
    contador = 0
    for palabra in palabras:
        contador += len(palabra)
    return contador


print(cuenta_letras('pelota', 'porteria'))