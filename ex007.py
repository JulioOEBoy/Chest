n = float(input('Coloque aqui sua primeira nota:').replace(',','.'))
n1 = float(input('Coloque aqui a sua segunda nota:').replace(',','.'))
n2 = n + n1
n3 = n2 / 2
print('Sua primeira nota de {}, mais a segunda nota de {}, da o valor de {}, após dividir o valor final é de {:.1f}.'.format(n,n1,n2,n3))