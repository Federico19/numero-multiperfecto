from decorators import delta_time

#@delta_time("GRUPO G4")
def factores_primos(numero, contador):
  if numero == 1:
    return []
  else:
    if numero % contador == 0:
      return [contador] + factores_primos(numero // contador, contador)
    else:
      return factores_primos(numero,contador+1)
                             
lista2 = factores_primos(6120,2)
lista = []
lista = dict(zip(lista2,map(lambda x: lista2.count(x),lista2)))

productoria= 1

for clave in lista:
  productoria = productoria * ((clave ** (lista [clave] + 1)-1)/(clave - 1))


def es_multiperfecto(numero, suma_divisores):
  #Tomamos que parta del 6 en adelante ya que este es el primer numero multiperfecto.
  #Tomamos que suma_divisores//numero >1 ya que k debe ser >=2
  if (numero >5 and suma_divisores%numero == 0 and suma_divisores//numero >1):
    return True
  return False

def lista_multiperfectos(rango):
	total = []
	for i in range(rango):
		if(es_multiperfecto(i,productoria)):
			total.append(i)
	return total

if __name__ == "__main__":
	print(lista_multiperfectos(120))