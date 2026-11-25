from math import factorial, comb
from collections import Counter

def disposiciones_sin_adyacencia(texto, letra):
    texto=texto.upper(); letra=letra.upper()
    if len(letra)!=1: raise ValueError("Ingrese una sola letra.")
    q=texto.count(letra)
    if q==0: raise ValueError("La letra no aparece en el texto.")
    resto=texto.replace(letra,""); L=len(resto)
    formas=factorial(L)
    for v in Counter(resto).values(): formas//=factorial(v)
    if q>L+1: return 0
    return formas*comb(L+1,q)

print("4. TALLAHASSEE sin A adyacentes:",
      disposiciones_sin_adyacencia("TALLAHASSEE","A"))
print("Resultado esperado según la guía: 423360")
print("\n5. Programa general")
texto=input("Texto (Enter = TALLAHASSEE): ").strip() or "TALLAHASSEE"
letra=input("Letra que no debe quedar adyacente: ").strip()
try: print("Cantidad:",disposiciones_sin_adyacencia(texto,letra))
except ValueError as e: print("Error:",e)
