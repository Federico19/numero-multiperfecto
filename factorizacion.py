from decorators import delta_time

def criba_eratostenes(maximo):
    factores = [0] * (maximo + 1)
    for i in range(2, maximo + 1):
        if factores[i] == 0:
            for j in range(i, maximo + 1, i):
                factores[j] = i
    return factores

def suma_divisores(n, factores):
    suma = 1
    while n > 1:
        d = factores[n]
        e = 0
        while n % d == 0:
            e += 1
            n //= d
        suma *= (d ** (e + 1) - 1) // (d - 1)
    return suma

def es_multiperfecto(numero, suma_divisores):
    if (numero > 5 and suma_divisores % numero == 0 and suma_divisores // numero > 1):
        return True
    return False

@delta_time("GRUPO G4")
def multiperfecto(rango):
    factores = criba_eratostenes(rango)
    lista = []
    for numero in range(2, rango+1):
        suma_div = suma_divisores(numero, factores)
        if es_multiperfecto(numero, suma_div):
            lista.append(numero)
    return lista

if __name__ == "__main__":
    resultado = multiperfecto(1000000)
    print(resultado)

    """La función criba_eratostenes genera una lista de factores primos para todos los números 
    en el rango dado. Luego, en lugar de calcular la suma de divisores de cada número de forma independiente, utilizamos 
    la lista de factores precalculada en la función suma_divisores para mejorar el rendimiento."""

"""Esta versión optimizada debería ser más rápida que la anterior. Sin embargo, encontrar números multiperfectos 
para rangos grandes sigue siendo un problema computacionalmente costoso. Si el rendimiento sigue siendo 
insuficiente, podrías considerar utilizar enfoques más avanzados, como algoritmos de búsqueda en paralelo o 
técnicas de programación de alto rendimiento."""