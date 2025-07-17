import sys
import re

entrada = int(sys.stdin.readline().strip())
vetor = []

for i in range(entrada):
    aux = sys.stdin.readline().strip()
    vetor.append(aux)
soma = 0
for texto in vetor:
    numeros = sum([int(x) for x in re.findall(r'\d+', texto)])
    soma +=numeros
print(soma)

