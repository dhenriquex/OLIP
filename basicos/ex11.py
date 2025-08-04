    """Horo e os copos

Por Aline Regina de Oliveira, Instituto Federal do Sul de Minas Gerais BR Brazil
Timelimit: 1

Astrologia é uma pseudociência segundo a qual as posições relativas dos corpos celestes poderiam prover informação sobre a personalidade, as relações humanas, e outros assuntos relacionados à vida do ser humano. Horo não acredita em astrologia, mas ele ganhou uma coleção de copos de aniversário, e cada copo estava estampado com um dos signos do zodíaco. Em um momento de curiosidade, resolveu pesquisar quais seriam os signos de seus amigos. Considerando a tabela abaixo com as datas de cada signo, ajude Horo a descobrir o signo de seus amigos.

Entrada

A entrada contém a data de aniversário de um amigo de Horo (data no formato dd/mm).
Saída

Para cada data de aniversário, informe o signo do amigo de Horo, com letras minúsculas e sem acento.
Exemplos de Entrada 	Exemplos de Saída

26/02
	

peixes

16/10
	

libra

27/05
	

gemeos
    """

import sys
data = sys.stdin.readline().strip()
dia, mes = map(int,data.split("/"))
if (dia>=21 and mes==3) or (dia<=20 and mes==4):
    print("aries")
elif (dia>=21 and mes==4) or (dia<=20 and mes==5):
    print("touro")
elif (dia>=21 and mes==5) or (dia<=20 and mes==6): 
    print("gemeos")
elif (dia>=21 and mes==6) or (dia<=22 and mes==7):
    print("cancer")
elif (dia>=23 and mes==7) or (dia<=22 and mes==8):
    print("leão")
elif (dia>=23 and mes==8) or (dia<=22 and mes==9):
    print("virgem")
elif (dia>=23 and mes==9) or (dia<=22 and mes==10):
    print("libra")
elif (dia>=23 and mes==10) or (dia<=21 and mes==11):
    print("escorpião")
elif (dia>=22 and mes==11) or (dia<=21 and mes==12):
    print("sagitário")
elif (dia>=22 and mes==12) or (dia<=20 and mes==1):
    print("capricórnio")
elif (dia>=21 and mes==1) or (dia<=19 and mes==2):  
    print("aquário")
elif (dia>=20 and mes==2) or (dia<=20 and mes==3):
    print("peixes")