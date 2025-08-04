import sys 
#complexidade O(n) e espaço O(n)
n = int(sys.stdin.readline().strip())
registros = []
# lê os registros de tempo
for _ in range(n):
    linha = sys.stdin.readline().strip().split()
    registros.append(linha[0], int(linha[1]))
# inicializa o tempo atual e dicionários para pendentes e respostas
tempoAtual = 0
pendentes = {}
tempoResposta = {}
for i in range(n):
    # processa cada registro
    tipo, numero = registros[i]
    # atualiza o tempo atual dependendo do tipo de registro
    if tipo == 'T':
        tempoAtual += numero
    else:
        
        if tipo == 'R':
            # se for um registro de início, adiciona ao dicionário pendentes
            pendentes[numero] = tempoAtual 
            if numerro not in tempoResposta:
                # se o número não estiver no dicionário de respostas, inicializa com 0
                tempoResposta[numero] = 0 
        elif tipo == 'E':
            # se for um registro de fim, calcula o tempo de resposta
            if numero in pendentes:
                # se o número estiver pendente, calcula o tempo de resposta
                tempoRespota[numero] += tempoAtual - pendentes.pop(numero)
            elif numero not in tempoResposta:
                # se o número não estiver pendente, inicializa com 0
                tempoResposta[numero] = 0
        if i + 1 < n and registros[i + 1][0] != 'T':
            # se o próximo registro não for um tempo, incrementa o tempo atual
            tempoAtual += 1
for x in pendentes:
    # se ainda houver pendentes, define o tempo de resposta como -1
    tempoResposta[x] = -1


for amigo in sorted(tempoResposta):
    # imprime o número do amigo e o tempo de resposta
    print(f"{amigo} {tempoResposta[amigo]}")



