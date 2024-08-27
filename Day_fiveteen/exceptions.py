""" SintaxError
print "Hola comunidad" """
print("Hola mundo")

""" NameError
print(name) """
name = "Alex"
print(name)

""" IndexError
mylista = ["Python", "Java", "Go"]
print(mylista[4]) """
mylista = ["Python", "Java", "Go"]
print(mylista[0])
print(mylista[1])
print(mylista[2])  #la lista tiene un tamaño de 3

""" ModuleNotFoundError
import maths  """
import math


""" AttributeError
print(math.PI) """
print(math.pi)

my_dict = {"Nombre":"Alex", "edad":23, 1:"Python"}
""" KeyError
print(my_dict["nombre"]) """
print(my_dict["Nombre"])


""" TypeError
print(mylista["0"]) """
print(mylista[0])

""" ImportError
from math import PI """
from math import pi
print(pi)

""" ValueError
my_int = int("10 Años")
print(my_int) """

# ZeroDivisionError
# print(4/0)