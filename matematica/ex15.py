x, y , z = map(int, input().split())

if x**2 == (y**2)+(z**2):
    print("AREA = ",((3*(z/2)**2)+z*y)/2)
else:
    print("Nao eh retangulo!")
