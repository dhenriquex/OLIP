import sys
anoes, distancia = map(int,sys.stdin.readline().strip().split())

print("{:.2f}".format(distancia/(anoes+2)))