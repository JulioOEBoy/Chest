print('1 para binario, 2 para octal e 3 para hexadecimal!')
e = int(input('Coloque a sua opção: '))
n = int(input("Coloque aqui o número: "))
b = (bin(n)[2:])
o = (oct(n)[2:])
h = (hex(n)[2:])
if e == 1:
    print(f'{b}')
elif e == 2:
    print(f'{o}')
elif e == 3:
    print(f'{h}')
else:
    print('Selecione um número valido! ')
