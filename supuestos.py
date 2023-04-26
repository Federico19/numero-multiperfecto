def factores_primos(n):  
  factors = {}
  d = 2

  while d * d <= n:
      print('Entro')
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

print(factores_primos(12))