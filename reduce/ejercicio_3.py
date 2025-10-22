# Ejercicio 3: encontrar el mayor con reduce
from functools import reduce
nums = [7,3,9,1,5]
mayor = reduce(lambda a, b: a if a > b else b, nums)
print(mayor)
