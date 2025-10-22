# Ejercicio 2: yield que devuelve los impares de una lista
def impares(lista):
    for n in lista:
        if n % 2 != 0:
            yield n

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for n in impares(nums):
    print(n)
