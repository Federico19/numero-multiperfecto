from decorators import delta_time

@delta_time("ProgramacionDinamica")
def corte_optimo(longitud_corte, precio, n):
    matriz_aux = [[0 for _ in range(n + 1)] for _ in range(len(longitud_corte) + 1)]
    
    for i in range(1, len(longitud_corte) + 1):
        for j in range(1, n + 1):
            if longitud_corte[i - 1] <= j:
                matriz_aux[i][j] = max(precio[i - 1] + matriz_aux[i][j - longitud_corte[i - 1]], matriz_aux[i - 1][j])
            else:
                matriz_aux[i][j] = matriz_aux[i - 1][j]

    # Imprimir la matriz auxiliar con los resultados
    # print("Matriz auxiliar (matriz_aux):")
    # for row in matriz_aux:
    #     print(row)

    mayor_ganancia = matriz_aux[len(longitud_corte)][n]
    cortes_optimos = []
    i = len(longitud_corte)
    j = n
    while i > 0 and j > 0:
        if matriz_aux[i][j] != matriz_aux[i - 1][j]:
            cortes_optimos.append(longitud_corte[i - 1])
            j -= longitud_corte[i - 1]
        else:
            i -= 1

    return mayor_ganancia, cortes_optimos


if __name__ == "__main__":
    # Ejemplo de uso
    longitud_corte = [1, 2, 3, 4, 5, 6, 7, 8]
    precio = [1, 5, 8, 9, 10, 17, 17, 20]
    largo_total = 8

    mayor_ganancia, cortes_optimos = corte_optimo(longitud_corte, precio, largo_total)
    print("Valor máximo obtenido:", mayor_ganancia)
    print("Cortes realizados:", cortes_optimos)

