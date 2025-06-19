import sys 
#ferramenta que gera uma lista de combinações possíveis
from itertools import product

n = int(sys.stdin.readline().strip())
entradas = []
for i in range(0, n):
    entrada = list(map(int, sys.stdin.readline().strip().split()))
    entradas.append(entrada)
for linhas in entradas:
    #pega as combinações possivel de 1 ate o numero de faces do dados, em seguida 
    #pega todas as combinações possiveis da qtd de dados
    possibilidades = list(product(range(1, linhas[2] + 1),repeat = linhas[1]))
    #cria um filtro que verifica se a soma das combinações é igual ao valor da primeira linha
    qtd = [1 for x in possibilidades if sum(x) == linhas[0] ]
    #imprime a quantidade de combinações que satisfazem o filtro dividido pelo total de combinações possíveis
    print(repr(len(qtd) / (linhas[2] ** linhas[1])))
        