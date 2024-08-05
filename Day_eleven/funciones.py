def add_two_numbers(num1: int, num2: int) -> int:
  return num1 + num2

print(add_two_numbers(2, 2))
print(add_two_numbers("2", "3"))
####################

from math import pi

def areaOfCircle(radio: int) -> float:
  area = pi*radio**2
  return round(area, 2)

print(areaOfCircle(2))
##########################

def addAllNums(*argumentos: int) -> float:
  suma = 0
  for arg in argumentos:
    if isinstance(arg, (int, float)):
      suma += arg
    else:
      return f"Error: '{arg} no es un numero.  Please provide only numeric values'"

  return suma
print(addAllNums(1, 2, 3.5))  # Should return 6.5
print(addAllNums(1, 'two', 3))  # Should return an error message
#########################################################3

