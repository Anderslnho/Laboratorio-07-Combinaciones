from itertools import combinations_with_replacement
from math import comb

def combinaciones_repeticion(n,r):
    if n<=0 or r<0: raise ValueError("n debe ser positivo y r no negativo")
    return list(combinations_with_replacement(range(n),r))

n,r=5,3
resultado=combinaciones_repeticion(n,r)
print(f"Combinaciones con repetición n={n}, r={r}:")
for x in resultado: print(x)
print("Cantidad generada:",len(resultado))
print("Cantidad por fórmula:",comb(n+r-1,r))
