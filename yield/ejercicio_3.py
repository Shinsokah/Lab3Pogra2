# Ejercicio 3: clase con __iter__() que da los cuadrados del 1 al 10
class Cuadrados:
    def __iter__(self):
        for i in range(1, 11):
            yield i ** 2

for n in Cuadrados():
    print(n)
