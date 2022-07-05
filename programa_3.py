def superficie_1(b,h):
    superficie_ = (b * h)
    return superficie_

#bloque principal
base1 = int(input("Ingresa el valor de la base: "))
altura1 = int(input("Ingresa el valor de la altura: "))
print("La superficie del primer rectangulo es:")
print(superficie_1(base1, altura1))

def superficie_2(b,h):
    superficie_1 = (b * h)
    return superficie_1

#bloque principal
base2 = int(input("Ingresa el valor de la base: "))
altura2 = int(input("Ingresa el valor de la altura: "))
print("La superficie del segundo rectangulo es:")
print(superficie_2(base2, altura2))

#verificar cual es mayor
if superficie_1(base1, altura1) > superficie_2(base2, altura2):
    print("La superficie del rectangulo 1° es mayor")
else:
    print("La superficie del rectangulo 2° es mayor")