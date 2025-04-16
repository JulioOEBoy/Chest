print('='*70)
n = float(input('Quantos km foram percorridos com o carro ?:'.format(',','.')))
n1 = float(input('quantos dias em que ele foi alugado:').format(',','.'))
print('='*70)
n2 = n1 * 60
n3 = n * 0.15
n4 = n2 + n3
print('O valor total ficou:{:.2f}'.format(n4))
print('='*70)