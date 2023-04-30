from decorators import delta_time

def factores_primos(numero):
  return factores_primos_aux(numero,[] , 2)
    
def factores_primos_aux(numero, list, contador):
  if numero == 1:
    return list
  else:
    if numero % contador == 0:
      return factores_primos_aux(numero // contador, (list + [contador]), contador)
    else:
      return factores_primos_aux(numero + 0, list + [], contador+1)
    

def productoria (num):
  lista = {}
  lista = dict(zip(num,map(lambda x: num.count(x),num)))

  resultado= 1

  for clave in lista:
    resultado = resultado * ((clave ** (lista [clave] + 1)-1)/(clave - 1))
  return resultado

@delta_time("GRUPO G4")
def multiperfectos(rango):
    lista_multiperfectos = []
    for numero in range (6,rango):
        fac_prim = factores_primos (numero)
        sum = productoria (fac_prim)
        if (numero >5 and sum%numero == 0 and sum//numero >1):
          lista_multiperfectos.append(numero)
    return lista_multiperfectos


""" tope = int(input("Numero: "))
if __name__ == "__main__":
	print(multiperfectos(tope)) """
print(multiperfectos(100000));