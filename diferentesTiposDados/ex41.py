import sys

n = int(sys.stdin.readline().strip())

lista = list(map(int, sys.stdin.readline().strip().split()))

direita = n -1
esquerda = 0
operaca = 0
while esquerda < direita:
    if(lista[esquerda] ==  lista[direita] ):
        esquerda += 1
        direita -= 1
    elif lista[esquerda] < lista[direita]:
        lista[esquerda + 1] += lista[esquerda]
        esquerda += 1
        operaca += 1
    else:
        lista[direita - 1] += lista[direita]
        direita -= 1
        operaca += 1
print(operaca)

