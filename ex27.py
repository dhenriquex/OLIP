import sys

palavra = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())

# Pega os últimos n caracteres e inverte
a =palavra[len(palavra) -n:][::-1]
print(a + palavra[:len(palavra) - n])