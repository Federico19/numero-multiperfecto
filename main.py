"""def divisores(numero):
  #Tanto 1 como el mismo numero son divisores de numero
  lista_divisores=[1,numero]
  #Los divisores de cualquier numero se encuentran entre 1 y el numero dividido 2, a excepcion del mismo numero
  #Si el numero es par, analizamos desde 2 hasta n//2+1 para encontrar sus divisores
  if (numero % 2 == 0):
    for i in range(2, numero//2 +1):
      if (numero % i) == 0:
        lista_divisores.append(i)
  else:
    #Si el numero es impar, analizamos desde 3 hasta n//2 analizando solamente los impares
    for i in range(3, numero//2, 2):
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
  #Tomamos que suma_divisores//numero >1 ya que k debe ser >=2
  if (numero >5 and suma_divisores%numero == 0 and suma_divisores//numero >1):
    return True
  return False



total = []
for i in range(10000):
  if(es_multiperfecto(i,sumaDivisores(divisores(i)))):
    total.append(i)
print(total)"""


from math import sqrt

def obtener_divisores(n):
    divisores = [1]
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            divisores.append(i)
            if n // i != i:
                divisores.append(n // i)
    return divisores

def encontrar_multiperfectos(rango):
    divisores_cache = {}
    multiperfectos = []
    for n in range(2, rango+1):
        if n in divisores_cache:
            divisores = divisores_cache[n]
        else:
            divisores = obtener_divisores(n)
            divisores_cache[n] = divisores
        suma_divisores = sum(divisores)
        if suma_divisores > n and suma_divisores % n == 0:
            multiperfectos.append(n)
    return multiperfectos

print(encontrar_multiperfectos(1000))
