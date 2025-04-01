import math
n = float(input('Digite um número pra o cateto oposto: ').replace(',','.'))
n1 = float(input('Digite um número pra o cateto oposto: ').replace(',','.'))
n2 = math.pow(n, 2)
n3 = math.pow(n1, 2)
n4 = (n2+n3)
n5 = math.sqrt(n4)
print('Se o cateto oposto for{} e o adjacente for {} a hipotenusa será :{:.2f}≈{:.2f}'.format(n,n1,n4,n5))