    """In Site

Por Andrês Rodrigues Oliveira,, UNICAMP BR Brazil
Timelimit: 1

In Site é um site de notícias muito famoso e bem reconhecido por sua confiabilidade nas matérias. Há um campeonato do qual esse grandioso site participa: a Gincana Televisiva, Empreendedora e Cultural, a GinTEC. Nesse campeonato, uma das provas mais badaladas é a Prova do Meio.

A Prova do Meio é bem simples: dadas as visualizações das postagens do site, calcula-se a mediana das visualizações e ganha quem tiver a maior mediana. Sua tarefa é dizer qual a mediana de In Site.
Entrada

A entrada contém um inteiro N (2 ≤ N ≤ 109) representando o número de postagens em ordem de publicação que In Site realizou. A próxima linha contém N inteiros Pi (2 ≤ Pi ≤ 106, 1 ≤ i ≤ N) representando o número de visualizações da postagem i.
Saída

A saída contém um inteiro com o valor da mediana das visualizações (caso a mediana seja um valor flutuante, mantenha a parte inteira).

    """


import sys
n = sys.stdin.readline().strip()
entradas =list(map(int, sys.stdin.readline().strip().split()))
entradas.sort()
if len(entradas) % 2 == 0:
    media = (entradas[len(entradas) // 2] + entradas[(len(entradas) // 2)-1])/2
    print(media)
else:
    print(entradas[len(entradas) // 2])