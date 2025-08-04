
"""

Caverna de Ordinskaya

Alguns de seus amigos decidiram viajar até a Russia para explorar Ordinskaya, a caverna subaquática mais comprida do país. Apesar da boa visibilidade das águas da caverna sempre é possível encontrar novas passagens e túneis que levam para longe da gruta principal, o que poderia fazer com que alguém se perdesse e provavelmente congelasse nas frias temperaturas observadas ali. Para evitar que algo assim ocorresse durante os mergulhos, o grupo usou uma fita métrica para marcar o caminho feito e garantir um retorno seguro. Além disso aproveitaram para medir quanto haviam explorado, sempre que retornavam à superfície alguém do grupo anotava num caderno o quão longe haviam ido.

O único problema com essa estratégia é que a cada mergulho pessoas diferentes ficavam responsáveis por verificar a fita métrica e anotar quanto havia sido explorado. Assim, se o comprimento da fita era 10 metros, após um mergulho em que o grupo explorou 3 metros da caverna, um dos amigos poderia ter desenrolado a fita do começo para o fim e anotar que 3 metros foram explorados, enquanto outromais desatento, sem perceber que havia desenrolado a fita no sentido contrário, poderia anotar que 7 metros foram explorados.

Apenas no final da viagem seus amigos perceberam a bagunça feita e agora pediram sua ajuda para reconstruir as distâncias de fato exploradas. Você foi informado que antes da viagem o grupo comprou uma fita com MM metros e que no total eles fizeram NN mergulhos. Outra informação importante é que a cada novo mergulho pelo menos a mesma distância do mergulho anterior era explorada, então se o comprimento da fita fosse de 10 metros e as anotações feitas fossem 3 e 8 metros, nessa ordem, os únicos cenários que realmente poderiam ter acontecido são:

    3 metros no primeiro mergulho e 8 no segundo;
    7 metros no primeiro mergulho e 8 no segundo.

Mas se os valores anotados foram 2 e 8, existem três possibilidades:

    2 metros no primeiro mergulho e 8 no segundo;
    2 metros no primeiro mergulho e 2 no segundo;
    8 metros no primeiro mergulho e 8 no segundo.

Como pode ter ocorrido algum engano nas anotações, pode ser impossível reconstruir a sequência
original, não se preocupe, todos vão entender caso isso aconteça.
Entrada

A primeira linha contém dois inteiros NN e MM, representando respectivamente a quantidade de mergulhos que o grupo fez e o comprimento em metros da fita que levaram para a exploração. A segunda linha contém NN inteiros A1,A2,…,ANA1​,A2​,…,AN​ representando as medições feitas a cada mergulho, na ordem em que foram anotadas.
Saída

Seu programa deve produzir uma única linha, contendo apenas um inteiro, que representa a soma das distâncias exploradas. Caso exista mais de uma sequência possível, imprima a menor soma das sequencias possíveis. Se não existir nenhuma sequência compatível com os dados, imprima apenas o inteiro -1.
Restrições

    1≤N≤1041≤N≤104
    1≤M≤5∗1051≤M≤5∗105
    0≤Ai≤M0≤Ai​≤M

Exemplos de Entrada 	Exemplos de Saída
5 7
2 5 3 6 0
	
20
3 5
2 1 2
	
-1
Traduzido por Arthur Freitas

"""
def tam(sequen, fita):
    soma = 0
    a = sequen[0]
    b = fita - sequen[0]
    # pega o primerio menor numero possivel do array
    anterior = min(a, b)
    soma += anterior

    for i in range(1, len(sequen)):
        a = sequen[i]
        b = fita - sequen[i]
        
        x, y = sorted([a, b])

        if x >= anterior:
            atual = x
        elif y >= anterior:
            atual = y
        else:
            print("-1")
            returna
        soma += atual
        anterior = atual

    print(soma)


qtd, fita = map(int, input().split())
sequencia = list(map(int, input().split()))
tam(sequencia, fita)
