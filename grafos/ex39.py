import sys
from collections import  defaultdict


pessoas, relacao = map(int, sys.stdin.readline().split())
grafo = defaultdict(list)

for _ in range(relacao):
    pessoa1, pessoa2 = map(int, sys.stdin.readline().split())
    grafo[pessoa1].append(pessoa2)
    grafo[pessoa2].append(pessoa1)

visitado = [False] * (pessoas + 1)
count = 0
'''
ESTOROU O TEMPO DE EXECUÇÃO
visitado = [False] * (pessoas + 1)
def defs(pessoa):
    visitado[pessoa] = True
    for amigos in grafo[pessoa]:
        if not visitado[amigos]:
            defs(amigos) 

'''
def defs(pessoa):
    conexoes = [pessoa]
    while conexoes:
        atual = conexoes.pop()
        if not visitado[atual]:
            visitado[atual] = True
            for amigo in grafo[atual]:
                if not visitado[amigo]:
                    conexoes.append(amigo)
                    
for i in range(1, pessoas + 1):
    if not visitado[i]:
        count += 1
        defs(i)
print(conexoes)


