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

