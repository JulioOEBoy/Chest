import math
print('='*70)
n = float(input('Digite um angulo: ').replace(',','.'))
n4 = math.radians(n)
n1 = math.sin(n4)
n2 = math.cos(n4)
n3 = math.tan(n4)
print('O número escolhido foi :{}'.format(n))
print('O Seno é               :{:.4f}'.format(n1))
print('O Cosseno é            :{:.4f}'.format(n2))
print('O Trangente é          :{:.4f}'.format(n3))
