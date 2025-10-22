# Ejercicio 1: primeros 10 numeros pares con yield
def pares():
    for i in range(0, 20, 2):
        yield i

for n in pares():
    print(n)
