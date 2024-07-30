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

if person.get("skills"):
  tam = len(person['skills']) // 2
  print(f"{person['skills'][tam]}")


