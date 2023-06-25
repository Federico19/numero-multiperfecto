def backtracking(cortes, longitud, long_actual, 
                 valor_corte, comb_corte, max_valor, max_comb):
  
  if long_actual == 0:
    print(valor_corte, comb_corte)
    if valor_corte > max_valor:
        max_valor = valor_corte
        max_comb = comb_corte
    return max_valor, max_comb
  
  for corte in range(long_actual, 0, -1):
    nueva_long = long_actual - corte
    nuevo_valor = valor_corte + valores[corte-1]
    nueva_comb = comb_corte + [corte]
    print("Nueva llamada", nueva_long)
    max_valor, max_comb = backtracking(cortes, longitud, nueva_long, nuevo_valor, nueva_comb, max_valor, max_comb)
  print("------------------")
  return max_valor, max_comb


def cortar_varilla(cortes, longitud):
    max_valor = 0
    max_comb = []
    long_actual = longitud
    valor_corte = 0
    comb_corte = []
    max_valor, max_comb = backtracking(cortes, longitud, long_actual, valor_corte, comb_corte, max_valor, max_comb)

    return max_valor, max_comb

# Ejemplo de uso
cortes = [1, 2, 3, 4, 5, 6, 7, 8]
valores = [1, 5, 8, 9, 10, 17, 17, 20]
longitud = 8
max_valor, max_comb = cortar_varilla(cortes, longitud)
print("Valor máximo de venta:", max_valor)
print("Combinación óptima de cortes:", max_comb)