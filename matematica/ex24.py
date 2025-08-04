import sys
dias, pessoas = map(int, sys.stdin.readline().strip().split())
combinacoes = 1.0
for i in range(pessoas):
    combinacoes *= (dias - i) / dias
print("{:.2f}".format((1 - combinacoes) * 100))
