n = float(input('Selecione o valor em metros desejado:').replace(',','.'))
n1 = n * 10
n2 = n * 100
n3 = n * 1000
n4 = n / 10
n5 = n / 100
n6 = n / 1000
#print('O valor em metros obtido era de ({:.0f}m)\nConvertido em centimetros fica ({:.0f}cm)\nE para milimetros fica ({:.0f}mm)'.format(n,n1,n2))
print('='*70)
print('O valor em metros selecionado é de ({}m) e ela corresponde a:'.format(n))
print('='*70)
print('O valor em quilõmetros é de : {}km'.format(n6))
print('O valor em hectõmetro é de  : {}hm'.format(n5))
print('O valor em decômetro é de   : {}dam'.format(n4))
print('O valor em decimetro é de   : {:.0f}dm'.format(n1))
print('O valor em centímetro é de  : {:.0f}cm'.format(n2))
print('O valor em milimetro é de   : {:.0f}mm'.format(n3))
print('='*70)