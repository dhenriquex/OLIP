import sys

def soma (flores, posicao):
    soma = 0
    for _ in range(1, posicao + 1):
        maiorValor = max(flores)
        indice = flores.index(maiorValor)
        
        soma = sum(int (x) for x in str(maiorValor))
        flores[indice] -= soma
    return soma

tamnaho, posicao = map(int, sys.stdin.readline().strip().split())
flores =  list(map(int, sys.stdin.readline().strip().split()))

print(soma(flores, posicao))


