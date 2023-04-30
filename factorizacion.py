#Calculo de numeros multiperfectos mediante sus factores primos.
from decorators import delta_time
import sys
sys.setrecursionlimit(100000)

@delta_time("GRUPO G4")
def multiperfecto(rango):
	return multiperfectos(rango)

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
  return factors

def suma_divisores(factores):
  if len(factores) == 1:
    base = next(iter(factores.keys()))
    exponente = factores[base]
    return (base**(exponente+1) -1) // (base-1)
  else:
    base = list(factores.keys())[-1]
    exponente = factores[base]
    del factores[base]
    return ((base**(exponente+1) -1) // (base-1)) * suma_divisores(factores)
  
def multiperfectos(rango):
  lista_multiperfectos = []
  for numero in range(6,rango+1):
    sumatoria = suma_divisores(divisores(numero))
    if( sumatoria % numero == 0 and sumatoria//numero >1):
      lista_multiperfectos.append(numero)
  return lista_multiperfectos

if __name__ == "__main__":
	print(multiperfecto(1000000))
