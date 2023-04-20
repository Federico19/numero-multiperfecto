def divisores(numero):
  #Tanto 1 como el mismo numero son divisores de numero
  lista_divisores=[1,numero]
  #Los divisores de cualquier numero se encuentran entre 1 y el numero dividido 2, a excepcion del mismo numero
  for i in range(2, numero//2 +1):
    if (numero % i) == 0:
      lista_divisores.append(i)

  return lista_divisores

def sumaDivisores(lista_divisores):
  resultado = 0
  for numero in lista_divisores:
    resultado += numero
  return resultado

def es_multiperfecto(numero, suma_divisores):
  #Tomamos que parta del 6 en adelante ya que este es el primer numero multiperfecto.
  if (numero >5 and suma_divisores%numero == 0 and suma_divisores//numero >1):
    return True
  return False

total = []
for i in range(1,8130):
  if(es_multiperfecto(i,sumaDivisores(divisores(i)))):
    total.append(i)
print(total)