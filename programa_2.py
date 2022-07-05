def contador_minuscula_mayuscula(letra):
    palabra_a = letra.lower()
    letra_ = palabra_a.count('a')
    return letra_
palabra_a = input("Ingresar una palabra: ")
print("Hay ", contador_minuscula_mayuscula(palabra_a), "letra(s) a")