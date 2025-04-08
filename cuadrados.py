class Cuadrado:
    def __init__(self,lado):
        self.lado = lado


    def calcular_area(self):
        return self.lado ** 2
    

if __name__ == "__main__":
    lado = float(input("Ingresa el valor del lado del cuadrado: "))
    mi_cuadrado = Cuadrado(lado)
    area = mi_cuadrado.calcular_area()
    print(f"El área del cuadrado con lado {lado} es: {area}")