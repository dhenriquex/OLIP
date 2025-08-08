import sys
n = int(sys.stdin.readline().strip())
dicionario ={}
for _ in range(n):
    ingles, portugues = sys.stdin.readline().strip().split()
    dicionario[ingles] = portugues
frase = sys.stdin.readline().strip().split()
for palavra in frase:
    print(dicionario.get(palavra), end=' ')
