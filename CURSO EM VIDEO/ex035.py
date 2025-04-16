n = float(input('Insira aqui o primeiro lado do triangulo: '))
n1 = float(input('Insira aqui o segundo lado do triangulo: '))
n2 = float(input('Insira aqui o terceiro lado do triangulo: '))
if n <= n2 + n1 and n1 <= n + n2 and n2 <= n1 + n:
    print('É um triangulo!')
else:
    print('Não é um triangulo!')