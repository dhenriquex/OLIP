qtd, tamanho = map(int, input().split())
alturaBrinquedo = list(map(int, input().split()))
soma = [x for x in alturaBrinquedo if x <= tamanho]
print(len(soma))
