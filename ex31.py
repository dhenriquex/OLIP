import sys
p1, c1, p2, c2 = map(int,sys.stdin.readline().strip().split())

if p1 * c1 == p2 * c2:
    print("0")
elif p1 * c1 > p2 * c2:
    print("-1")
else:
    print("1")