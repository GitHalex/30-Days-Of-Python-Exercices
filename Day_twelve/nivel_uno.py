from random import randint

characteres = "abcdefghijklmnopqrstuwxyz123456789"

def random_user_id() -> str:
        
    id = ""
    for _ in range(6):
        aux = randint(0, len(characteres) - 1)
        id += characteres[aux]

    return id

print(random_user_id())


""" def user_id_gen_by_user() -> None:
    
   
    tam = int(input("Ingrese el tamaño: "))
    cuantos = int(input("Cantidad de lineas: "))
 
    for i in range(cuantos):
        id = "#"
        for _ in range(tam):
          aux = randint(0, len(characteres) - 1)
          id += characteres[aux]
        print(id)
            
user_id_gen_by_user() """

def rgb_color_gen() -> str:
  listaValor = []
  for i in range(3):
     numero = randint(0, 255)
     listaValor.append(numero)

  return f"rgb{tuple(listaValor)}"

print(rgb_color_gen())


def list_of_hexa_colors(limite: int) -> list:
   
   hexadecimal = "1234567890ABCEDF"
   arrHexa = []
   for i in range(limite):
      indice = 0
      valor = "#"
      for j in range(6):
         indice = randint(0, len(hexadecimal) - 1)
         valor += hexadecimal[indice]
      arrHexa.append(valor)

   return arrHexa
      

print(list_of_hexa_colors(3))

def list_of_rgb_colors(limite: int) -> list:
   listaResultado = []
   for i in range(limite):
      listaValor = []
      for i in range(3):
        numero = randint(0, 255)
        listaValor.append(numero)

      listaResultado.append(f"rgb{tuple(listaValor)}")

   return list_of_rgb_colors

print(list_of_rgb_colors(3))









































