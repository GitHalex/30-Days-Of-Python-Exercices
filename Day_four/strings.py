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
