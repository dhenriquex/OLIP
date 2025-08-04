import sys 
import re

n = sys.stdin.readline().strip()



print(f"Vogais: {re.sub(r"[bcdfghjklmnpqrstvwxyz]", "", n)}")
print(f"Consoantes: {re.sub(r"[aeiou]", "", n)}")
