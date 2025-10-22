# Ejercicio 3: clase que genera cuadrados sin iter pero con metodo lista
class Cuadrados:
    def lista(self):
        resultado = []
        for i in range(1, 11):
            resultado.append(i ** 2)
        return resultado

print(Cuadrados().lista())
