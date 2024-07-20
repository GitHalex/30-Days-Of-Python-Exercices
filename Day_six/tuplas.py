tuplavacia = ()
print(tuplavacia)
print(type(tuplavacia))

namesTuplaFemale = ("Ana", "Juana", "Chanel")
namesTuplaMale = ("Alex","Juan", "Chanel")

brothersTupla = namesTuplaFemale + namesTuplaMale
print(brothersTupla)

siblings = brothersTupla.count("Chanel")
print(f"Tengo: {siblings} hermanos gemelos")

family_members = list(brothersTupla)
family_members.append("Father")
family_members.append("Mother")

print(family_members)
enTuplaMiembros = tuple(family_members)
print(enTuplaMiembros)

familiaOrdenada = sorted(family_members)

a, b, *cd, e, f, g, h = familiaOrdenada

print(cd)
print(e)
print(h)

fruits = ("Platano", "Fresa", "Tomate")
vegetables = ("Papa", "Lechuga")
animal_products= ("Carna", "Pollo")

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

listaFood = list(food_stuff_tp)
mitad = len(listaFood) // 2
print(listaFood)

mitadFoods = listaFood[0: mitad]
print(mitadFoods)
ultimosTres = food_stuff_tp[-3:]
print(ultimosTres)

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)