# Ejercicio 2: generador de impares del 1 al 20 usando yield
class Impares:
    def __iter__(self):
        for i in range(1, 21, 2):
            yield i

for n in Impares():
    print(n)
