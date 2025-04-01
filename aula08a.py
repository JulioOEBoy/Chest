import math
#from math import sqrt
num = int(input('Digite um número:'))
raiz = math.sqrt(num)
print('A raiz de {} é igual a:{}'.format(num, math.ceil(raiz)))