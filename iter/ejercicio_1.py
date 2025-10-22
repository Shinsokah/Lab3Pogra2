# Ejercicio 1: contador del 10 al 15 usando iter y next
numeros = iter(range(10, 16))
while True:
    try:
        print(next(numeros))
    except StopIteration:
        break
