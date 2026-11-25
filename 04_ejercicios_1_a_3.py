from math import comb, factorial
from itertools import combinations
from collections import Counter

def combinacion(n,r):
    if not isinstance(n,int) or not isinstance(r,int) or n<0 or r<0 or r>n:
        raise ValueError("Se requiere n>=0 y 0<=r<=n")
    return comb(n,r)

print("1. C(10,3) =",combinacion(10,3))
print("\n2. Parejas de 1..6:")
pares=list(combinations(range(1,7),2))
for p in pares: print(p)
print("Total:",len(pares))
texto="TALLAHASSEE"
f=Counter(texto)
total=factorial(len(texto))
for cantidad in f.values(): total//=factorial(cantidad)
print("\n3. Frecuencias de TALLAHASSEE:",dict(f))
print("Disposiciones distintas:",total)
