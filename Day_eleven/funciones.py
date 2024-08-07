""" def add_two_numbers(num1: int, num2: int) -> int:
  return num1 + num2

print(add_two_numbers(2, 2))
print(add_two_numbers("2", "3")) """
####################

""" from math import pi

def areaOfCircle(radio: int) -> float:
  area = pi*radio**2
  return round(area, 2)

print(areaOfCircle(2)) """
##########################

""" def addAllNums(*argumentos: int) -> float:
  suma = 0
  for arg in argumentos:
    if isinstance(arg, (int, float)):
      suma += arg
    else:
      return f"Error: '{arg} no es un numero.  Please provide only numeric values'"

  return suma
print(addAllNums(1, 2, 3.5))  # Should return 6.5
print(addAllNums(1, 'two', 3))  # Should return an error message """
#########################################################

def convertCelsiusToFahrenheit(C: int) -> float:
  F = (C*9/5) + 32
  return F

print(convertCelsiusToFahrenheit(2))
####################################################3

""" def checkSeason(mes: str) -> None:
  match mes:
    case "diciembre" | "enero" | "febrero":
      print("Invierno")
    case "marzo" | "abril" | "mayo":
      print("Primavera")
    case "junio" | "julio" | "agosto":
      print("Verano")
    case "septiembre" | "octubre" | "noviembre":
      print("Otoño")
    case _:
      print(f" {mes}: Mes no correspondiente")
 
mes = input("Ingrese una mes: ").lower()
checkSeason(mes)



def calculate_slope(x1, y1, x2, y2):
    Calculate the slope of a line given two points (x1, y1) and (x2, y2).
    
    Args:
        x1, y1: Coordinates of the first point.
        x2, y2: Coordinates of the second point.

    Returns:
        The slope of the line connecting the two points.
    
    if x1 == x2:
        raise ValueError("The slope is undefined (vertical line).")
    
    slope = (y2 - y1) / (x2 - x1)
    return slope

# Example usage
try:
    m = calculate_slope(1, 2, 4, 8)
    print(f"The slope of the line is: {m}")
except ValueError as e:
    print(e) """
######################################33

""" from math import sqrt

print("Programa para la resolucion de la ecuacion x*x + b*x + c = 0")

def solveQuadraticeqn(a: int, b: int, c: int) -> None:

  if a != 0:
    discriminante = b**2 - 4*a*c
    if discriminante >= 0:
      x1 = (-b + sqrt(discriminante)) /(2*a)
      x2 = (-b - sqrt(discriminante)) /(2*a)
      if x1 == x2:
        print(f"Solucion: x1={x1}")
      else:
        print(f"Solucion: x1={x1} -> x2={x2}")
    else:
      print("No hay soluciones reales")
  else:
    if b != 0:
      x = -c/b
      print(f"Solucion: x={x}")
    else:
      if c != 0:
        print("La ecuacion no tiene solucion")
      else:
        print("La ecuacion tiene infinitas soluciones")

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("ingrese el valor de c: "))
solveQuadraticeqn(a, b, c) """
#########################################

""" def printList(lista: list) -> None:
  for i in lista:
    print(i)

printList(["Alex", "Calcina", True, 2.3, 2024])

def reverse_list(numbers: list) -> list:
  return numbers[::-1]

print(reverse_list([1,2,3,4,5]))
print(reverse_list(["A", "B", "C"]))

def capitalizeListItems(names: list) -> list:
  mayusculas = []
  for name in names:
    mayusculas.append(name.upper())

  return mayusculas

print(capitalizeListItems(["Alex", "Ana", "juan"])) """
##############################################3

""" def add_item(food_staf: list, food: str):
  if food not in food_staf:
    food_staf.append(food)
  
  return food_staf
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5)) """
#########################################

""" def remove_item(listaFoods: list, food: str) -> list:
  listaRes = []
  for j in listaFoods:
    if  food == j:
      listaFoods.remove(j)
    
  listaRes = listaFoods

  return listaRes

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3)) """
#################################################

""" def sum_of_numbers(numero: int) -> float:
  sumTotal = 0
  for i in range(1, numero+1):
    sumTotal += i

  return sumTotal

print(sum_of_numbers(5)) 
print(sum_of_numbers(10)) """ 
#####################################

""" def sum_of_odds(numero: int) -> float:
  sumOdds = 0
  for i in range(1, numero+1):
    if i % 2 == 0:
      sumOdds += i

  return sumOdds

print(sum_of_odds(100))

def sum_of_evens(numero: int) -> float:
  sumEvens = 0
  for i in range(1, numero+1):
    if i % 2 != 0:
      sumEvens += i

  return sumEvens

print(sum_of_evens(100)) """
#########################################

""" def evens_and_odds(numero: int) -> list:
  sumEvens = 0
  sumOdds = 0

  for i in range(0, numero + 1):
    if i % 2 == 0:
      sumEvens += 1
    else:
      sumOdds += 1

  return [sumEvens, sumOdds]

pares, impares = evens_and_odds(100)
print(pares)
print(impares) """
##############################################

""" def factorial(number: int) -> int:
  res = 1
  for i in range(number, 0, -1):
    res *= i

  return res

print(factorial(3))
print(factorial(4)) """
#########################################


def is_empty(param):
    """Check if the provided parameter is empty or not.
    
    Args:
        param: The parameter to check.

    Returns:
        True if the parameter is empty, False otherwise.
    """
    return not bool(param)

# Example usage
print(is_empty(""))           # True (empty string)
print(is_empty("Hello"))      # False (non-empty string)
print(is_empty([]))           # True (empty list)
print(is_empty([1, 2, 3]))    # False (non-empty list)
print(is_empty({}))           # True (empty dictionary)
print(is_empty({'key': 'value'}))  # False (non-empty dictionary)
print(is_empty(0))            # True (0 is considered empty)
print(is_empty(1))            # False (non-zero integers are not empty)

""" Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation). """


from typing import List
from collections import Counter
import math

def calculate_mean(numbers: List[float]) -> float:
    """Calculate the mean of a list of numbers."""
    return sum(numbers) / len(numbers)

def calculate_median(numbers: List[float]) -> float:
    """Calculate the median of a list of numbers."""
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle = n // 2
    if n % 2 == 0:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:
        return sorted_numbers[middle]

def calculate_mode(numbers: List[float]) -> float:
    """Calculate the mode of a list of numbers."""
    counter = Counter(numbers)
    most_common = counter.most_common(1)
    return most_common[0][0]

def calculate_range(numbers: List[float]) -> float:
    """Calculate the range of a list of numbers."""
    return max(numbers) - min(numbers)

def calculate_variance(numbers: List[float]) -> float:
    """Calculate the variance of a list of numbers."""
    mean = calculate_mean(numbers)
    squared_diffs = [(x - mean) ** 2 for x in numbers]
    return sum(squared_diffs) / len(numbers)

def calculate_std(numbers: List[float]) -> float:
    """Calculate the standard deviation of a list of numbers."""
    variance = calculate_variance(numbers)
    return math.sqrt(variance)

# Example usage
numbers = [1, 2, 2, 3, 4, 5, 5, 5, 6]

print(f"Mean: {calculate_mean(numbers)}")
print(f"Median: {calculate_median(numbers)}")
print(f"Mode: {calculate_mode(numbers)}")
print(f"Range: {calculate_range(numbers)}")
print(f"Variance: {calculate_variance(numbers)}")
print(f"Standard Deviation: {calculate_std(numbers)}")
