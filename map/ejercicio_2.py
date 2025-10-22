# Ejercicio 2: convertir celsius a fahrenheit usando map
celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)
