from itertools import combinations
from math import comb

def combinaciones_manual(n,r):
    if not 0 <= r <= n: raise ValueError("Se requiere 0 <= r <= n")
    if r == 0: return [()]
    a=list(range(1,r+1)); salida=[tuple(a)]
    while True:
        i=r-1
        while i>=0 and a[i]==n-r+i+1: i-=1
        if i<0: break
        a[i]+=1
        for j in range(i+1,r): a[j]=a[j-1]+1
        salida.append(tuple(a))
    return salida

for n,r in [(6,3),(6,2),(7,5)]:
    manual=combinaciones_manual(n,r)
    it=list(combinations(range(1,n+1),r))
    print(f"\nn={n}, r={r}; C(n,r)={comb(n,r)}")
    print("Cantidad manual:",len(manual),"Cantidad itertools:",len(it))
    print("¿Coinciden?:",manual==it)
    for x in manual: print(x)
