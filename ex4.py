    """A Olimpíada Municipal de Programação vai distribuir camisetas para os melhores colocados, e por isso solicitou que os premiados informassem o tamanho preferido da camiseta, entre os tamanhos pequeno e médio.

A empresa que confeccionou as camisetas, por uma falha, pode ter se enganado na quantidade de camisetas para cada tamanho. Foram produzidas camisetas em número suficiente para todos os premiados, mas talvez não do tamanho preferido.

Dadas a lista com os tamanhos preferidos pelos premiados e a quantidade de camisetas de cada tamanho produzidas pela empresa, escreva um programa para determinar se todos os premiados receberão camisetas do tamanho escolhido.
Entrada

A primeira linha contém um inteiro NN, o número de premiados. A segunda linha contém NN inteiros TiTi​, indicando os tamanhos solicitados pelos premiados, sendo que Ti=1Ti​=1 representa o tamanho pequeno e Ti=2Ti​=2 representa o tamanho médio. A terceira linha contém um inteiro PP, o número de camisetas de tamanho pequeno produzidas. A quarta e última contém um inteiro MM, o número de camisetas de tamanho médio produzidas.
Saída

Seu programa deve produzir uma única linha, contendo um único caractere, que deve ser a letra maiúscula ‘S’ se todos os premiados serão atendidos com a camiseta do tamanho que escolheram, ou a letra maiúscula ‘N’ caso contrário
    """

N = int(input())
entradas = list(map(int, input().split()))
p = int (input())
m = int (input())
if p == entradas.count(1) and m == entradas.count(2):
    print("S")
else:
    print("N")