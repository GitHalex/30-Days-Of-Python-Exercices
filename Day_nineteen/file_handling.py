# .txt file
with open("/home/halex/30DaysOfPython/30-Days-Of-Python-Exercices/Day_nineteen/my_file.txt", "r+") as txt_file:
    
    txt = txt_file.read(4)
    print(txt, "hola")
    print(txt)


import os
print(os.getcwd())

print("################################")

f = open("/home/halex/30DaysOfPython/30-Days-Of-Python-Exercices/Day_nineteen/my_file.txt")
print(f)

""" txt = f.read()
print(txt)
print(type(txt))
f.close() """

""" txt = f.read(10)
print(txt)  #Esto es un  solo 10 caracters
print(type(txt))
f.close() """

""" line = f.readline()
print(line)    #solo muestra la primera linea del texto
print(type(line))
f.close() """


""" lines = f.readlines()
print(lines)
print(type(lines))
f.close() """

""" lines = f.read().splitlines() # lo envuelve en una lisata ['Esto es una prueba', 'otra fila', 'fila prime']
print(lines)
f.close() """


with open("/home/halex/30DaysOfPython/30-Days-Of-Python-Exercices/Day_nineteen/my_file.txt", "a") as txt_file:
    txt_file.write("\nparrafo con write")



# .json file
import json

json_file = open("/home/halex/30DaysOfPython/30-Days-Of-Python-Exercices/Day_nineteen/my_file.json", "w+")

json_test = {
    "name": "Alex",
    "surname": "Lopez",
    "age": 23,
    "language": ["Python","Java","NodeJS"],
    "website": "https://moure.dev"
}

# json_file.write(json_test)
json.dump(json_test, json_file, indent=2)

# dictionary
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}

person_json = json.dumps(person_dct, indent=4)
print(type(person_json))
print(person_json)