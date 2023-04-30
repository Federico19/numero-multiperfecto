#Calculo de numeros multiperfectos mediante sus factores y en forma recursiva
from decorators import delta_time
import sys
sys.setrecursionlimit(100000)

def factores_primos_diccionario(numero, contador, diccionario):
  if numero == 1:
    return diccionario
  else: 
    if numero % contador == 0:
      if contador not in diccionario:
        diccionario[contador] = 0
      diccionario[contador] += 1
      return factores_primos_diccionario(numero // contador, contador, diccionario)
    else:
      return factores_primos_diccionario(numero, contador +1, diccionario)
    
def suma_divisores(factores):
  """  if len(factores) == 1:
      base = next(iter(factores.keys()))
      exponente = factores[base]
      return (base**(exponente+1) -1) // (base-1)
    else:
      base = list(factores.keys())[-1]
      exponente = factores[base]
      del factores[base]
      return ((base**(exponente+1) -1) // (base-1)) * suma_divisores(factores)"""
  sumatoria = 1
  while len(factores)<1:
      base = list(factores.keys())[-1]
      exponente = factores[base]
      sumatoria *= (base**(exponente+1) -1) // (base-1)
  return sumatoria
  
  
def multiperfectos(rango):
  lista_multiperfectos = []
  for numero in range(6,rango+1):
    """print(numero)

      if( sumatoria % numero == 0 and sumatoria//numero >1):
        lista_multiperfectos.append(numero)
        """
    diccionario = factores_primos_diccionario(numero,2,dict())
    #sumatoria = suma_divisores(diccionario)
    print(numero)
    print(diccionario)
  return lista_multiperfectos

print(multiperfectos(1000000))
