print('-=-'*20)
print('Coloque o valor de\033[1;31m 3 lados\033[m a se seguir: ')
print('-=-'*20)
n1 = float(input('Coloque o primeiro valor: '))
n2 = float(input('Coloque o segundo valor: '))
n3 = float(input('Coloque o terceiro valor: '))
print('-=-'*20)
if n1 + n2 <= n3 or n2 + n3 <= n1 or n3 + n1 <= n2:
    print('\033[1;31mNão da para formar um triangulo forneça dados validos!\033[m ')
elif n1 == n2 and n2 == n3:
    print('Da pra formar um triangulo \033[1;31mequilatero\033[m!')
elif n1 == n2 or n2 == n3 or n3 == n1:
    print('DA pra formar um triangulo \033[1;31misosceles\033[m!')
else:
    print('Da pra formar um triangulo \033[1;31mescaleno\033[m!')

print('-=-'*20)
