# Ejercicio 4: iterador que devuelve cadenas en mayusculas
palabras = ["hola", "python", "mundo"]
it = iter(palabras)
for palabra in it:
    print(palabra.upper())
