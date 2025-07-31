import sys 
e = int(sys.stdin.readline().strip())
a = int(sys.stdin.readline().strip())
c = int(sys.stdin.readline().strip())
pontos = e * 2 + a * 3 + c * 5 
if pontos>= 200:
    print("O")
elif pontos >= 150 and pontos < 200:
    print("S")
elif pontos >= 100 and pontos < 150:
    print("B")
else:
    print("N")

