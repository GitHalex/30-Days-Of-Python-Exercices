from math import pi

""" age: int = 30
height: float = 1.7
complejo: complex = 1 + 4j

base: int = int(input("Ingrese la base: "))
altura: int = int(input("Ingrese la altura: "))

area: float = (base*altura) / 2
print(f"The area of the triangle is {area}")

a: int = int(input("Valor de a: "))
b: int = int(input("Valos de b: "))
c: int = int(input("Valor de c; "))

perimetroTriangulo = a + b + c


print(f"The perimeter of the triangle is: {perimetroTriangulo}")
 """

# Definimos los coeficientes de la ecuación de la línea y = mx + b
m = 2  # Pendiente (slope)
b = -2  # Intersección con el eje y (y-intercept)

# Cálculo de la intersección con el eje x (x-intercept)
# En la intersección con el eje x, y = 0
# 0 = 2x - 2
# 2x = 2
# x = 1
x_intercept = -b / m

# Resultados
print(f"Pendiente (slope): {m}")
print(f"Intersección con el eje y (y-intercept): {b}")
print(f"Intersección con el eje x (x-intercept): {x_intercept}")

import math

# Coordenadas de los puntos
x1, y1 = 2, 2
x2, y2 = 6, 10

# Cálculo de la pendiente (slope)
slope = (y2 - y1) / (x2 - x1)

# Cálculo de la distancia euclidiana
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Resultados
print(f"Pendiente (slope): {slope}")
print(f"Distancia euclidiana (Euclidean distance): {distance}")


cadena1: str = "python"
cadena2: str = "dragon"

print(cadena1 == cadena2)


for x in range(5):
  y = x**2 + 6*x + 9
  print(f"x:{x} resultado de y=x² + 6x + 9 => {y}")


print('on' in cadena1 and 'on' in cadena2)

sentencia: str = "I hope this course is not full of jargon"
print("jargon" in sentencia)
print("Prueba")

texto: int = len("python")
print(float(texto))
print(type(str(texto)))

for numero in range(10):
  if numero % 2 == 0:
    print(f"Par: {numero}")
  else:
    print(f"impar: {numero}")

verificar: int = 7 / 3
convertido: int = int(2.7)

print(int(verificar) == convertido)

print('10' == 10)

print('9.8' == 10)


horas = int(input("Ingrese la cantidad de horas: "))
trabajoHora = int(input("Ingrese la cantidad de horas tranajadas: "))
gana = horas * trabajoHora
print(gana)

years = 100
print(f"You have lived for {100*360*24*60*60}")


for num in range(1, 6):
  print(f"{num}\t{num**0}\t{num**1}\t{num**2}\t{num**3}")