import sys 

n = int(sys.stdin.readline().strip())
lista = []
for _ in range(n):
    aux = int(sys.stdin.readline().strip())
    lista.append(aux)
print(len(set(lista)))

