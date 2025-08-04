import sys

paises, esportes = map(int, sys.stdin.readline().strip().split())

# Criar estrutura para armazenar medalhas por país, índices de 1 a paises
medalhas = [[0,0,0] for _ in range(paises + 1)]

for _ in range(esportes):
    o, p, b = map(int, sys.stdin.readline().strip().split())
    medalhas[o][0] += 1  # ouro
    medalhas[p][1] += 1  # prata
    medalhas[b][2] += 1  # bronze

# Ordenar países pelos critérios pedidos
resultado = sorted(range(1, paises + 1), key=lambda i: (-medalhas[i][0], -medalhas[i][1], -medalhas[i][2], i))

print(*resultado)
