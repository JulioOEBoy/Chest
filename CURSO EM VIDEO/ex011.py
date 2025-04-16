print('='*90)
n = float(input('Coloque aqui o valor em metros da largura:').replace(',','.'))
print('='*90)
n1 = float(input('Coloque aqui o valor em metros da altura:').replace(',','.'))
print('='*90)
n2 = n * n1
n3 = n2 / 2
print('Uma parede com a largura ({}m), e altura ({}m), tem uma área de ({}m²).'.format(n,n1,n2))
print('E se o litro da tinta pintar 2m², será necessário ({:.2f}L) de tinta para ser pintada.'.format(n3))
print('='*90)