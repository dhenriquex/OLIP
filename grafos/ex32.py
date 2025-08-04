from collections import defaultdict
import sys

alunos, relacao = map(int, sys.stdin.readline().split())
grafos = defaultdict(list)
#cria um grafo não direcionado usando defaultdict para armazenar as arestas
# defaultdict permite que você crie listas automaticamente para cada chave
for _ in range(relacao):
    amigo, colega = map(int, sys.stdin.readline().split())
    grafos[amigo].append(colega)
    grafos[colega].append(amigo)
# adiciona arestas bidirecionais entre os estudantes
# cada estudante é representado por um número inteiro de 1 a alunos
# amigo e colega são os estudantes conectados por uma amizade

visitado = [False] * (alunos + 1)
# cria uma lista de visitados para rastrear quais estudantes foram visitados
componentes = 0
# inicializa o contador de componentes conectados
def dfs(amigo):
    visitado[amigo] = True
    # marca o estudante atual como visitado
    for colega in grafos[amigo]:
        # percorre todos os colegas do estudante atual
        # se o colega ainda não foi visitado, chama a função dfs recursivamente
        if not visitado[colega]:
            dfs(colega)
for i in range(1, alunos + 1):
    if not visitado[i]:
        dfs(i)
        # se o estudante não foi visitado, inicia uma nova busca em profundidade
        # isso indica que encontramos um novo componente conectado
        # incrementa o contador de componentes conectados
        componentes += 1

print(componentes)

