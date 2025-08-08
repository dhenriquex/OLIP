import sys

n = int(sys.stdin.readline().strip())
dic = {}

for _ in range(n):
    a, b, c = sys.stdin.readline().strip().split()
    dic[int(a)] = [b, int(c)]  # a = chave (esquerda), b = letra, c = próxima peça (direita)

# Já sabemos que começa em 0
e = 0
resultado = ""

for _ in range(n):
    letra, proximo = dic[e]
    resultado += letra
    e = proximo  # próximo número a acessar

print(resultado)
