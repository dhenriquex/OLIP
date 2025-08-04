"""
retorna o numero com a maior frequncia em uma sequencia de numero
"""
N = int(input())
entradas = list(map(int, input().split()))

if len(entradas) != N:
    print("Erro: quantidade de números diferente de N.")
else:
    mais_repetidos = max(entradas, key=entradas.count) # o max permite retornar o maior valor, sau key personliza sa saida 
    qtd = entradas.count(mais_repetidos)
    print(qtd)
