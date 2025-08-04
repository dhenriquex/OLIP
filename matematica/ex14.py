import sys 
#ferramenta que gera uma lista de combinações possíveis
from itertools import product

n = int(sys.stdin.readline().strip())
saidas = []
for i in range(0, n):
    entrada = list(map(int, sys.stdin.readline().strip().split()))
    #pega as combinações possivel de 1 ate o numero de faces do dados, em seguida 
    #pega todas as combinações possiveis da qtd de dados
    possibilidades = list(product(range(1, entrada[2] + 1),repeat = entrada[1]))
    #cria um filtro que verifica se a soma das combinações é igual ao valor da primeira linha
    qtd = [1 for x in possibilidades if sum(x) == entrada[0] ]
    #imprime a quantidade de combinações que satisfazem o filtro dividido pelo total de combinações possíveis
    saidas.append(repr(len(qtd) / (entrada[2] ** entrada[1])))
for i in saidas:
    print(i)
        