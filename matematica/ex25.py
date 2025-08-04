import sys
import datetime

horario, qtd = map(int, sys.stdin.readline().strip().split())
saidas = []

meiaNoite = datetime.datetime.strptime("00:00:00", "%H:%M:%S")
limite_tempo = datetime.timedelta(minutes=horario)

for i in range(qtd):
    linha = sys.stdin.readline().strip()
    horasStr, pessoa = linha.split()
    
    horasStr = f"{horasStr}:00"
    horas = datetime.datetime.strptime(horasStr, "%H:%M:%S")
    
    tempo_passado = horas - meiaNoite
    
    if tempo_passado <= limite_tempo:
        saidas.append(pessoa)
for i in saidas:
    print(i)
