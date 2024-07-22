dog = {}
print(type(dog))
dog["Name"] = "Marrano"
print(dog)
dog["Color"] = "Amarillo"
print(dog)
dog["Breed"] = ""

students = {"firstName": "Alex","lastName": "Calcina","gender": "male","age":20,"married": True,"skills": ["HTML","CSS","JS","React"], "country": "Bolivia", "city":"Chacobamba","address": "jose Pool"}

clavesDiccionario = students.keys()
print(clavesDiccionario)

print(f"Tamaño del diccionario: => {len(students)}")

for i in students.values():
  print(f"clave {i} => Tipo {type(i)}")

students["skills"].append("NodeJS")
students["skills"].append("NextJs")

for i in students.values():
  print(f"clave {i} => Tipo {type(i)}")

listaKeys = list(students.keys())
print(listaKeys)

listaValues = list(students.values())
print(listaValues)

tuplasStudend = students.items()
print(tuplasStudend)

del students["firstName"]

print(students)

