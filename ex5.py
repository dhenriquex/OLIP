N = int(input())

sd = 1
matriz = []

for i in range(0, N):
    entradas = list(map(int, input().split()))
    matriz.append(entradas)
# pega a linha de cada matriz e verifica com a soma da primeira  linha referencia
referencia = sum(matriz[0])
for i in range(0,N):
    if sum(matriz[i]) != referencia:
        print("-1")
        exit()
#pega a coluna de cada matriz e verifica com a soma da primeira coluna referencia
for j in range(0,N):
    if referencia != sum(matriz[i][j] for i in range(0,N)):
        print("-1")
        exit()
#pega a diagonal principal e verifica com a soma da primeira linha referencia
sd = sum(matriz[i][i] for i in range(0,N))
if referencia != sd:
    print("-1")
    exit()
#pega a diagonal secundaria e verifica com a soma da primeira linha referencia
sd = sum(matriz[i][N - 1 - i] for i in range(0,N))
if referencia != sd:
    print("-1")
    exit()
print(referencia)