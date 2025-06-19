import sys
numero = {
    1:"um",
    2:"dois",
    3:"tres",
    4:"quatro",
    5:"cinco",
    6:"seis",
    7:"sete",
    8:"oito",
    9:"nove",
}
n = sys.stdin.readline().strip()
if n.isdigit():
    print(numero[int(n)])
else:
    x = [x for x, y in numero.items() if y == n.lower()]
    print(x[0])