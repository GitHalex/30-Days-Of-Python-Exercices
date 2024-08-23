countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
# countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
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

concatenacionCadenas = reduce(lambda ca1, ca2: ca1 +", "+ ca2, countries)
print(f"{concatenacionCadenas} are north Europan countries")

def categorize_countries(pais) -> str:

  if "land" in pais:
     return pais
  
paises_patron = filter(categorize_countries, countries)
print(list(paises_patron))


def categoria_countries(pais: str, patron: str) -> str:

  if patron in pais:
     return pais
  
countriesPatron = filter(lambda pais: categoria_countries(pais, "land"), countries)


print(list(countriesPatron))


def categorize_countries(pais: str, patron: str) -> str:
    if patron in pais:
        return pais
    return None

paises_patron = map(lambda pais: categorize_countries(pais, "land"), countries)
# Filtramos los resultados para excluir los valores None
paises_filtrados = filter(None, paises_patron)

print(list(paises_filtrados))

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


