import sys
import math
from functools import reduce

n = int(sys.stdin.readline())
entradas = list(map(int, sys.stdin.readline().split()))
# forma de salvar as varivaeis de forma eficiente 

def mdc_lista(lista):
    # math.gcd calcula o mdc de todos os numeros
    return reduce(math.gcd, lista)
    #reduce retorna o mdc do elemntos 

print(mdc_lista(entradas))
