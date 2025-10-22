# Ejercicio 2: multiplicar elementos con reduce
from functools import reduce
nums = [2,3,4]
prod = reduce(lambda x, y: x * y, nums)
print(prod)
