countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

usandoDistintasListas = filter(lambda pais: len(pais) == 6, map(lambda pais: pais.upper(), countries))
print(list(usandoDistintasListas))

listaDatos = ["Alex", "Calcina", 23, 2024]
soloCadenas = filter(lambda i: isinstance(i, str) and i.isalpha(), listaDatos)
print(list(soloCadenas))

from functools import reduce  # Importar reduce desde functools

def add(a, b):
    return a + b

print(reduce(add, [1, 2, 3, 4]))  # 10

sumaAll = reduce(lambda a, b: a+b, numbers)
print(sumaAll)

""" for pais in countries:
  print(pais)

for name in names:
  print(name)

for number  in numbers:
  print(number) """

""" mayusculas = list(map(lambda pais: pais.upper(), countries))
print(mayusculas) """


""" square = map(lambda number: number ** 2, numbers)
print(list(square)) """

""" def namesMayuscula(name):
  return name.upper()

namesMayusculas = map(namesMayuscula, names)
print(list(namesMayusculas)) """


""" def funcionFilter(pais):
  if "land" in pais:
    return True
  
countriesLand = filter(funcionFilter, countries)
print(list(countriesLand)) """

""" otro = list(filter(lambda pais: "land" in pais, countries))
print(otro) """

""" soloSeis = list(filter(lambda pais: len(pais) == 6, countries))
print(soloSeis) """

""" masSeis = list(filter(lambda pais: len(pais) >= 7, countries))
print(masSeis) """

""" empieza_E = list(filter(lambda pais: "E" in pais, countries))
print(empieza_E) """


