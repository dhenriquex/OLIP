"""
Esse é o meu lugar!

Por Aline Regina de Oliveira, Instituto Federal do Sul de Minas Gerais BR Brazil
Timelimit: 1

Sheldon Cooper é um cara excêntrico. Uma de suas excentricidades é ter um local favorito no sofá: o lado esquerdo (de quem se senta). Mas não é um gosto aleatório, ele tem suas razões para isso: no inverno, esse lugar é perto o bastante do aquecedor para continuar quente, e não tão perto para causar transpiração. No verão, está no caminho de uma brisa, criada por duas janelas. Daí ele vê a televisão num ângulo que não é nem direto, que desencoraje a conversa, e não é longe o bastante para criar distorções na lente. Faça um programa que considere onde Leonard Hofstadter (o colega de apartamento de Sheldon) está sentado e mostre o que Sheldon irá falar.
Entrada

A entrada possui múltiplos casos de teste e termina com fim de arquivo. Cada caso de teste possui uma string com três caracteres que representam os lugares do sofá, onde 'x' é um lugar vago e 'L' é o local onde Leonard está sentado.
Saída

Seu programa deverá mostrar a fala do Sheldon ao ver Leonard. Se Leonard estiver no lugar favorito do Sheldon: "Esse eh o meu lugar", caso contrário: "Oi, Leonard".

"""

import sys
entradas = []
while True:
    n = sys.stdin.readline().strip().split()
    if not n:
        break
    entradas.append(n)
for n in entradas:
    if "xxL" in n:
        print("Esse eh o meu lugar")
    else :
        print("Oi, Leonard")