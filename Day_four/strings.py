palabra1 = "Thirty"
palabra2 = "Days"
palabra3 = "Of"
palabra4 = "Python"

respuesta = palabra1 + " " + palabra2 + " " + palabra3 + " " + palabra4
print(respuesta)

company = "Coding for All"

print(f"Variable: {company}")

print(f"tamaño: {len(company)}")

print(f"En MAYUSCULAS: {company.upper()}")

print(f"EN MINUSCULAS: {company.lower()}")

print(f"capitalize: {company.capitalize()} => title: {company.title()} => swapcase: {company.swapcase()}")

primeraPalabra = company[:7]
print(f"Primera palabra: {primeraPalabra}")

print(company.index("Coding"))
print(company.find("Coding"))

print(company.replace("Coding", "Python"))

print("Esto es otro")

print("Python for Everyone".replace("Everyone", "All"))

print(company.split(" "))

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
arregloCompanies = companies.split(",")
print(arregloCompanies)

print(company[0])
print(company[-1])
print(company[10])


palabraAcronimo = "Python For All people"

acronimo = palabraAcronimo.split(" ")
print(acronimo[0][0] + acronimo[1][0] + acronimo[2][0])

acronimoCompani = company.split(" ")
print(acronimoCompani[0][0] + acronimoCompani[1][0] + acronimoCompani[2][0])

print(company.index("C"))
print(company.index("f"))

print(palabraAcronimo.rindex("l"))

phrase = 'You cannot end a sentence with because because because is a conjunction'
print(phrase.find("because"))

print(phrase.rindex("because"))

primeroBecause = phrase.find("because")
segundoBecause = phrase.rfind("because")

print(type(primeroBecause))

resultado = phrase[primeroBecause:segundoBecause + 7]
print(resultado)


# Define la cadena
string = "Coding For All"

# Comprueba si la cadena comienza con la subcadena "Coding"
starts_with_coding = string.startswith("Coding")
# Muestra el resultado
print(f"Does 'Coding For All' start with the substring 'Coding'? {starts_with_coding}")

cadena = '   coding For All    '
print(cadena.strip())

var = "30DaysOfPython"
var2 = "thirty_days_of_python"
print(var.isidentifier())
print(var2.isidentifier())
print("def".isidentifier())

pythonLibraries = ["Django","Flask","Bottle","Pyramid","Falcon"]
cadenaLibraries = "-".join(pythonLibraries)
print(cadenaLibraries)

print("I am enjoying this challenge\nI just wonder what is next.")

print("Name\tAge\tCountry\tCity\nAlex\t250\tFinland\tChacobamba")

radius = 10
area = 3.14 * radius ** 2

print(f"The area of a circle with radius {radius} is {area} meters square.")

number = 8
number1 = 6

print(f"{number} + {number1} => {number+number1}\n{number} - {number1} => {number-number1}")
print(f"{number} x {number1} => {number*number1}\n{number} / {number1} => {round(number/number1, 2)}")
print(f"{number} % {number1} => {number%number1}\n{number} // {number1} => {number//number1}")
print(f"{number} ** {number1} => {number**number1}")