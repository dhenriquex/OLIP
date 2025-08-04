
"""

 beecrowd | 3465
Cimba

Por Aline Regina de Oliveira, Instituto Federal do Sul de Minas Gerais BR Brazil
Timelimit: 1

Cimba herdou um terreno em formato triangular após o falecimento de seu pai. Para passar o terreno para seu nome, o cartório exige que seja informada a área do terreno. Sabe-se que o terreno é delimitado por uma cerca e Cimba consegue medir cada um dos lados do terreno. Você consegue ajudar Cimba a calcular a área do terreno dadas as medidas dos lados?
Entrada

A entrada é composta por 3 números a b c, que representam os lados do terreno.

Limites:
1 ≤ a, b, c ≤ 2023
Saída

Seu programa deve mostrar a área do terreno herdado por Cimba com 3 casas decimais, seguido do texto "m2". Confira nos exemplos.
Exemplos de Entrada 	Exemplos de Saída

7 8 9
	

26.833 m2

1598 1041 1800
	

825807.679 m2

1827 1789 1039
	

899046.078 m2
"""
import sys
import math
numero = list(map(int,(sys.stdin.readline().strip().split())))
s = sum(numero) / 2
resultado = math.sqrt(s*(s-numero[0])*(s-numero[1])*(s-numero[2]))
print("{:.3f} m2".format(resultado))

