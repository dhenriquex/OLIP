import sys

n = int(sys.stdin.readline().strip())

pares = {}
for _ in range (0, n):
    numero, pe = sys.stdin.readline().strip().split()
    numero = int(numero)
    if numero not in pares:
        pares[numero] = {'D': 0, 'E': 0}
    pares[numero][pe] += 1
print( sum(min(p['E'], p['D']) for p in pares.values()))   