def retornar_promedio(v1, v2, v3):
    promedio = (v1 + v2 + v3)//3
    return promedio
#bloque principal
valor1 = int(input("Ingresa tu primera nota: "))
valor2 = int(input("Ingresa tu segunda nota: "))
valor3 = int(input("Ingresa tu tercera nota: "))
print("Tu promedio es: ", retornar_promedio(valor1, valor2, valor3))