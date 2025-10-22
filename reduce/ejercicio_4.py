# Ejercicio 4: concatenar cadenas con reduce
from functools import reduce
palabras = ["Hola", " ", "Mundo", "!"]
texto = reduce(lambda a, b: a + b, palabras)
print(texto)
