from decorators import delta_time

@delta_time("ProgramacionDinamica")
def corte_optimo(cortes, valor_corte, n):
    matriz_aux = [[0 for _ in range(n + 1)] for _ in range(len(cortes) + 1)]
    
    for i in range(1, len(cortes) + 1):
        for j in range(1, n + 1):
            if cortes[i - 1] <= j:
                matriz_aux[i][j] = max(valor_corte[i - 1] + matriz_aux[i][j - cortes[i - 1]], matriz_aux[i - 1][j])
            else:
                matriz_aux[i][j] = matriz_aux[i - 1][j]

    # Imprimir la matriz auxiliar con los resultados
    # print("Matriz auxiliar (matriz_aux):")
    # for row in matriz_aux:
    #     print(row)

    max_valor = matriz_aux[len(cortes)][n]
    max_comb = []
    i = len(cortes)
    j = n
    while i > 0 and j > 0:
        if matriz_aux[i][j] != matriz_aux[i - 1][j]:
            max_comb.append(cortes[i - 1])
            j -= cortes[i - 1]
        else:
            i -= 1

    return max_valor, max_comb


if __name__ == "__main__":
    # Ejemplo de uso
    cortes = [1, 2, 3, 4, 5, 6, 7, 8]
    valor_corte = [1, 5, 8, 9, 10, 17, 17, 20]
    longitud = 8

    max_valor, max_comb = corte_optimo(cortes, valor_corte, longitud)
    print("Valor máximo de venta:", max_valor)
    print("Combinación óptima de cortes:", max_comb)

