def divisores(n):
  lista=[]
  for i in range(1, n+1):
    if (n % i) == 0:
      lista.append(i)

  return lista

def sumaDivisores(lista):
  

divisores = divisores(6)
print(divisores)