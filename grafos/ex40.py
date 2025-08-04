import sys
from collections import defaultdict

n = int(sys.stdin.readline().strip())
arvore = defaultdict(int)
raiz = -1
for _ in range(n):
    filho, pai = sys.stdin.readline().strip().split()
    if pai = '0':
        raiz = filho
    else:
        arvore[pai].append(filho)
balanceado = True
def tamanho(raiz):
    global balanceado
    tamanhos = []
    for filhos in arvore[raiz]:
        tamanho.append(tamanho(filhos))
    if len(tamanhos) > 1:
        balanceado = False
    return 1  + sum(tamanhos)


print("bem" if balanceado else "mal")