import sys
humanos, elfos, anoes, orc, wargs, aguias = map(int, sys.stdin.readline().strip().split())
if (humanos + elfos + anoes + aguias) >= (orc + wargs):
    print("Middle-earth is safe.")
else: 
    print("Sauron has returned.")