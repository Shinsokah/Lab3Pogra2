# Ejercicio 2: palabras que empiezan con p
palabras = ["perro","gato","pato","hamster"]
p = list(filter(lambda x: x.startswith("p"), palabras))
print(p)
