# version de python 3.10.12
numero1: int = 3
numero2: int = 4

print(f"addition:\t \t {numero1} - {numero2} => {numero1 + numero2}")
print(f"subtraction:\t \t {numero1} - {numero2} => {numero1 - numero2}")
print(f"multiplication:\t \t {numero1} X {numero2} => {numero1 * numero2}")
print(f"division:\t \t {numero1} / {numero2} => {numero1 / numero2}")
print(f"modulus:\t \t {numero1} % {numero2} => {numero1 % numero2}")
print(f"exponential:\t \t {numero1} ^ {numero2} => {numero1 ** numero2}")
print(f"floor operation:\t {numero1} // {numero2} => {numero1 // numero2}")

entero: int = 10
flotante: float = 9.8
Constante: float = 3.14
varComplejo: complex = 4 - 4j
miNombre: str = "Alex"
miFamilyName: str = "Lopez Perez"
myCountry: str = "Bolivia"

print(f"Tipo de la variable entero {type(entero)}")
print(f"Tipo de la variable flotante {type(flotante)}")
print(f"Tipo de la variable constante {type(Constante)}")
print(f"Tipo de la variable varcomplejo {type(varComplejo)}")
print(f"Tipo de la variable minombre {type(miNombre)}")
print(f"Tipo de la variable myfamily {type(miFamilyName)}")
print(f"Tipo de la variable micontry {type(myCountry)}")


def demonstrate_data_types():
    # Number: Integer
    integer_example: int = 42
    print(f"Integer: {integer_example}, Type: {type(integer_example)}")

    # Number: Float
    float_example: float = 3.14159
    print(f"Float: {float_example}, Type: {type(float_example)}")

    # Number: Complex
    complex_example: complex = 1 + 2j
    print(f"Complex: {complex_example}, Type: {type(complex_example)}")

    # String
    string_example: str = "Hello, World!"
    print(f"String: '{string_example}', Type: {type(string_example)}")

    # Boolean
    boolean_example: bool = True
    print(f"Boolean: {boolean_example}, Type: {type(boolean_example)}")

    # List
    list_example: list = [1, 2, 3, 4, 5]
    print(f"List: {list_example}, Type: {type(list_example)}")

    # Tuple
    tuple_example: tuple = (1, 2, 3, 4, 5)
    print(f"Tuple: {tuple_example}, Type: {type(tuple_example)}")

    # Set
    set_example: set = {1, 2, 3, 4, 5}
    print(f"Set: {set_example}, Type: {type(set_example)}")

    # Dictionary
    dictionary_example: dict = {"one": 1, "two": 2, "three": 3}
    print(f"Dictionary: {dictionary_example}, Type: {type(dictionary_example)}")

if __name__ == "__main__":
    demonstrate_data_types()
