# Ejercicio 1: sumar elementos con reduce
from functools import reduce
nums = [5,10,15,20]
suma = reduce(lambda x, y: x + y, nums)
print(suma)
