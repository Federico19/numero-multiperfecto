def backtrack(c, n, current_length, current_value, current_combination, max_value, max_combination):
    if current_length == 0:
        print(current_combination, current_value)
        if current_value > max_value:
            max_value = current_value
            max_combination = current_combination
        return max_value, max_combination

    for i in range(len(c)):
        print(i, current_length)
        if current_length >= c[i]:
            new_length = current_length - c[i]
            new_value = current_value + values[i]
            new_combination = current_combination + [c[i]]
            max_value, max_combination = backtrack(c, n, new_length, new_value, new_combination, max_value, max_combination)

    return max_value, max_combination

def rod_cutting(c, n):
    max_value = 0
    max_combination = []
    current_length = n
    current_value = 0
    current_combination = []
    max_value, max_combination = backtrack(c, n, current_length, current_value, current_combination, max_value, max_combination)

    return max_value, max_combination

# Ejemplo de uso
c = [1, 2, 3, 4]
values = [1, 5, 8, 9]
n = 4
max_value, max_combination = rod_cutting(c, n)
print("Valor máximo de venta:", max_value)
print("Combinación óptima de cortes:", max_combination)

""" 
En este ejemplo, la función rod_cutting toma una lista c con las longitudes posibles de corte y una longitud total n.
La función backtrack realiza la recursión, generando todas las posibles combinaciones de cortes y actualizando el 
máximo valor y combinación encontrados.
"""