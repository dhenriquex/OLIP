n = int(input())
fila = list(map(int, input().split()))
m = int(input())
saiu = set(map(int, input().split())) 


fila = [x for x in fila if x not in saiu]

for pessoa in fila:
    print(pessoa, end=" ")
