from decorators import delta_time


#Funcion que devuelve los factores primos de un numero de forma recursiva
def factores_primos(numero, contador):
  if numero == 1:
    return []
  else:
    if numero % contador == 0:
      return [contador] + factores_primos(numero // contador, contador)
    else:
      return factores_primos(numero, contador +1)

def lista_diccionario(factores):
  diccionario = {}
  anterior = 1
  for elemento in factores:
    if elemento not in diccionario:
      diccionario[elemento] = 0
    diccionario[elemento] += 1
  return diccionario

def suma_divisores(factores):
  if len(factores) == 1:
    exponente = next(iter(factores.values()))
    base = next(iter(factores.keys()))
    return (base**(exponente+1) -1) // (base-1)
  else:
    exponente = list(factores.values())[-1]
    base = list(factores.keys())[-1]
    del factores[base]
    return ((base**(exponente+1) -1) // (base-1)) * suma_divisores(factores)
  
def multiperfectos(rango):
  lista_multiperfectos = []
  for numero in range(6,rango):
    sumatoria = 
    if( sumatoria % numero == 0 and sumatoria//numero >1):
      lista_multiperfectos.append(numero)
  return lista_multiperfectos


