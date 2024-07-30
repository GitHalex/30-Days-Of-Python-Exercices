""" age = int(input("Enter your age: "))
if age >= 18:
  print("You are old enough to learn to drive")

if age > 0 and age < 18:
  edadAdecuada = 18 - age
  print(f"You need {edadAdecuada} more years to learn to drive")

myAge = int(input("Enter my age: "))
yourAge = int(input("Enter your age: "))

if myAge > yourAge:
  valor = myAge - yourAge
  print(f"I am {valor} than you")
else:
  valor = yourAge - myAge
  print(f"You are {valor} older than me") """

""" primerNumero = int(input("Primer numero: "))
segundoNumero = int(input("Segundo numero: "))
candidato = primerNumero
if segundoNumero > candidato:
  candidato = segundoNumero
  print(f"{candidato} is greater than {primerNumero}")
else:
  print(f"{candidato} is greater than {segundoNumero}") """


""" score = int(input("ingrese una nota entre 0 - 100"))
if score >= 90 and score <= 100:
  print("A")
elif score >= 70 and score <= 89:
  print("B")
elif score >= 60 and score <= 69:
  print("C")
elif score >= 50 and score <= 59:
  print("D")
else:
  print("F") """


""" fruits = ['banana', 'orange', 'mango', 'lemon']
fruta = input("ingrese una fruta: ")
if fruta in fruits:
  print(f"That fruit already exist in the list: {fruits}")
else:
  fruits.append(fruta) """
from math import floor

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

print(person)

# Verificar si el diccionario tiene la clave 'skills'
if 'skills' in person:
    skills = person['skills']
    
    # Imprimir la habilidad del medio en la lista de habilidades
    middle_index = len(skills) // 2
    print(f"La habilidad del medio es: {skills[middle_index]}")
    
    # Verificar si la persona tiene la habilidad 'Python' y imprimir el resultado
    has_python = 'Python' in skills
    print(f"Tiene habilidad en Python: {has_python}")
    
    # Determinar el título del desarrollador basado en las habilidades
    if 'JavaScript' in skills and 'React' in skills and 'Node' not in skills and 'MongoDB' not in skills and 'Python' not in skills:
        print('Él es un desarrollador de frontend.')
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print('Él es un desarrollador de backend.')
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print('Él es un desarrollador fullstack.')
    else:
        print('Título desconocido.')

# Verificar si la persona está casada y vive en Finlandia
if person.get('is_married') and person.get('country') == 'Finland':
    first_name = person['first_name']
    last_name = person['last_name']
    country = person['country']
    print(f"{first_name} {last_name} es casado y vive en {country}.")


