# Ejercicio 4: serie de fibonacci con yield hasta el decimo
def fibonacci():
    a, b = 0, 1
    for _ in range(10):
        yield a
        a, b = b, a + b

for n in fibonacci():
    print(n)
