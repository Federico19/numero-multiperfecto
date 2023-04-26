from decorators import delta_time

@delta_time("GRUPO G4")
def multiperfecto(rango):
	return lista_multiperfectos(rango)

def divisores(n):
    # factorización prima
    factors = {}
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            if d not in factors:
                factors[d] = 0
            factors[d] += 1
            n //= d
        d += 1
    if n > 1:
        if n not in factors:
            factors[n] = 0
        factors[n] += 1

    # construir la lista de divisores a partir de los factores primos
    divisors = [1]
    for prime in factors:
        temp_divisors = []
        for i in range(factors[prime] + 1):
            for divisor in divisors:
                temp_divisors.append(divisor * (prime ** i))
        divisors = temp_divisors

    return divisors

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

def lista_multiperfectos(rango):
	total = []
	for i in range(rango):
		if(es_multiperfecto(i,sumaDivisores(divisores(i)))):
			total.append(i)
	return total

if __name__ == "__main__":
	print(multiperfecto(1000000))