"""
Você está de volta em seu hotel na Tailândia depois de um dia de mergulhos. O seu quarto tem duas lâmpadas. Vamos chamá-las de AA e BB. No hotel há dois interruptores, que chamaremos de I1I1​ e I2I2​. Ao apertar I1I1​, a lâmpada AA acende se estiver apagada, e apaga se estiver acesa. Se apertar I2I2​, cada uma das lâmpadas AA e a BB troca de estado: se estiver apagada, fica acesa e se estiver acesa apaga.

As lâmpadas inicialmente estão ambas apagadas. Seu amigo resolveu bolar um desafio para você. Ele irá apertar os interruptores em uma certa sequência, e gostaria que você respondesse o estado final das lâmpadas AA e BB.
Entrada

A primeira linha contém um número NN que representa quantas vezes seu amigo irá apertar algum interruptor. Na linha seguinte seguirão N números, que pode ser 1, se o interruptor I1I1​ foi apertado, ou 2, se o interruptor I2I2​ foi apertado.
Saída

Seu programa deve imprimir dois valores, em linhas separadas. Na primeira linha, imprima 1 se a lâmpada AA estiver acesa no final das operações e 0 caso contrário. Na segunda linha, imprima 1 se a lâmpada BB estiver acesa no final das operações e 0 caso contrário.
"""
N = int(input())
bt1 = 0
bt2 = 0
entradas = list(map(int, input().split()))
for i in entradas:
    if i == 1:
        bt1 = bt1 ^ 1
    else: 
        bt1 = bt1 ^ 1
        bt2 = bt2 ^ 1
print(bt1)
print(bt2)