from decorators import delta_time
from tabulate import tabulate
def backtrack(cortes, long_actual, valor_corte, comb_corte, max_valor, max_comb):
    tabla = [[comb_corte,long_actual, valor_corte]]
    #print(tabulate(tabla))
    if long_actual == 0:
        if valor_corte > max_valor:
            max_valor = valor_corte
            max_comb = comb_corte
        return max_valor, max_comb

    for corte in range(len(cortes)):
        if long_actual >= cortes[corte]:
            nueva_long = long_actual - cortes[corte]
            nuevo_valor = valor_corte + valores[corte]
            nueva_comb = comb_corte + [cortes[corte]]
            max_valor, max_comb = backtrack(cortes, nueva_long, nuevo_valor, nueva_comb, max_valor, max_comb)

    return max_valor, max_comb

@delta_time("Backtracking")
def corte_varilla(cortes, longitud):
    max_valor = 0
    max_comb = []
    long_actual = longitud
    valor_corte = 0
    comb_corte = []
    max_valor, max_comb = backtrack(cortes, long_actual, valor_corte, comb_corte, max_valor, max_comb)

    return max_valor, max_comb


if __name__ == "__main__":
  # Ejemplo de uso
  cortes = [1, 2, 3, 4, 5, 6, 7, 8]
  valores = [1, 5, 8, 9, 10, 17, 17, 20]
  longitud = 8
  max_valor, max_comb = corte_varilla(cortes, longitud)
  print("Valor máximo de venta:", max_valor)
  print("Combinación óptima de cortes:", max_comb)