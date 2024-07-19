listaVacia = []
cinco = ["Alex","Lopes", 1, 3.14, True]
print(f"lista: {cinco} su tamaño es => {len(cinco)}")

# Get the first item, the middle item and the last item of the list
primero = cinco[0]
medio = cinco[2]
ultimo = cinco[-1]
print(f"{primero} - {medio} - {ultimo}")
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Alex", 10, 1.7, False, "Chacobamba"]
# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
# Print the list using print()
print(it_companies)
# Print the number of companies in the list
print(f"El numero de companies: {len(it_companies)}")
# Print the first, middle and last company
print(f"primero: {it_companies[0]} => medio: {it_companies[3]} => ultimo: {it_companies[-1]}")
# Print the list after modifying one of the companies
it_companies[0] = "Meta" 
print(it_companies)
# Add an IT company to it_companies
it_companies.append("HH")
# Insert an IT company in the middle of the companies list
it_companies.insert(3, "CloudLex")
# Change one of the it_companies names to uppercase (IBM excluded!)
print(it_companies[0].upper())
print(it_companies[1].upper())
print(it_companies[2].upper())
print(it_companies[3].upper())
print(it_companies[4].upper())
print(it_companies[6].upper())
print(it_companies[7].upper())
print(it_companies)
# Join the it_companies with a string '#;  '
juntsr = " #".join(it_companies)
print(juntsr)
# Check if a certain company exists in the it_companies list.
print(it_companies.index("HH"))
# Sort the list using sort() method
it_companies.sort()
print(it_companies)
# Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)
# Slice out the first 3 companies from the list
primerosTres = it_companies[:3]
print(primerosTres)
# Slice out the last 3 companies from the list
ultimosTres = it_companies[-3:]
print(ultimosTres)
# Slice out the middle IT company or companies from the list
print(it_companies[4])
# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)
# Remove the middle IT company or companies from the list
print(it_companies.remove("HH"))
# Remove the last IT company from the list
it_companies.pop()
print(it_companies)
# Remove all IT companies from the list
it_companies.clear()
print(it_companies)
# Destroy the IT companies list
del it_companies