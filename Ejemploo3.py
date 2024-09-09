# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

# Función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    area = 0.5 * base * altura
    return area

# Función principal
def main():
    # Entrada de valores para el rectángulo
    base_rectangulo = float(input("Introduce la base del rectángulo: "))
    altura_rectangulo = float(input("Introduce la altura del rectángulo: "))
    area_rectangulo = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)
    print("Área del rectángulo:", area_rectangulo)

    # Entrada de valores para el triángulo
    base_triangulo = float(input("Introduce la base del triángulo: "))
    altura_triangulo = float(input("Introduce la altura del triángulo: "))
    area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)
    print("Área del triángulo:", area_triangulo)

main()
