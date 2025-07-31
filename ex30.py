import sys 
#complexidade O(n) e espaço O(n)
def subVetores(n, vetor):
    from collections import Counter
    #importa a biblioteca Counter para contar ocorrências de prefixos
    # ele funciona como um dicionário que mapeia cada prefixo a sua contagem de ocorrências
    prefixo = 0
    contador = Counter()
    contador[0] = 1
    #inicializa o prefixo com 0 e o contador com 1 para o prefixo 0
    # para vetores vazios, o prefixo 0 é considerado como um subvetor válido e par 
    total = 0
    for i in vetor:
        prefixo ^= i 
        total += contador[1 - prefixo]
        contador[prefixo] += 1
        # contador = {0:qtd0, 1:qtd1}
    return total

n = int(sys.stdin.readline().strip())
vetor = list(map(int, sys.stdin.readline().strip().split()))
print(subVetores(n, vetor))