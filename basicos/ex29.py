import sys

animo, atvC, atvR = map(int, sys.stdin.readline().strip().split())
entradas = []

for _ in range(atvC + atvR):
    n = int(sys.stdin.readline().strip())
    entradas.append(n)

somaR = sum(entradas[atvC:]) + animo
somaC = entradas[:atvC]
qtd = atvR

for i in somaC:
    if somaR >= i:
        somaR -= i
        qtd += 1
    else:
        break

print(qtd)
