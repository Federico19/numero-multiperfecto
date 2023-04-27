def es_perfecto(n, factores):
  primo = 0
  while primo < len(factores):
    potencia = 2**(factores[primo]-1)*(2**(factores[primo])-1)
    if (n > potencia):
      primo += 1
    else:
      if (n == potencia):
        return True
      else:
        return False

factores = [2,3,5,7,11,13]


