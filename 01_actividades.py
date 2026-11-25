from math import comb
from itertools import combinations

print("1.1 C(10,8) =", comb(10,8))
print("1.2 C(5,4)*C(5,4) =", comb(5,4)*comb(5,4))
print("1.3 Cadenas de 8 bits con 3 ceros:", comb(8,3))
for pos in combinations(range(8),3):
    s=["1"]*8
    for i in pos: s[i]="0"
    print("".join(s))
print("1.4 Combinaciones de 3 de {a,b,c,d}:")
for x in combinations("abcd",3): print(x)
print("1.5a Exactamente 3 caras:",comb(10,3))
print("1.5b A lo sumo 3 caras:",sum(comb(10,k) for k in range(4)))
print("1.6a 10 monedas/5 niños sin restricción:",comb(14,4))
print("1.6b Cada niño al menos 1:",comb(9,4))
print("1.6c Niño mayor al menos 2:",comb(12,4))
