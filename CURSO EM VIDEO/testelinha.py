largura = 60  # Define a largura do quadrado
linha = '-=-' * 20  # Linha superior e inferior

print(f'\033[1;34m{linha}\033[m')  # Azul
print(f'\033[1;34m|\033[m\033[1;31m{"Coloque o valor de 3 lados a seguir:":^{largura-2}}\033[m\033[1;34m|\033[m')
print(f'\033[1;34m{linha}\033[m')

n1 = float(input('\033[1;34m--\033[m Coloque o primeiro valor: '))
n2 = float(input('\033[1;34m--\033[m Coloque o segundo valor: '))
n3 = float(input('\033[1;34m--\033[m Coloque o terceiro valor: '))
print(f'\033[1;34m{linha}\033[m')

if n1 + n2 <= n3 or n2 + n3 <= n1 or n3 + n1 <= n2:
    print(f'\033[1;34m|\033[m\033[1;31m{"Não dá para formar um triângulo!":^{largura-2}}\033[m|')  # Vermelho
elif n1 == n2 and n2 == n3:
    print(f'\033[1;34m|\033[m\033[1;32m{"Triângulo Equilátero!":^{largura-2}}\033[m\033[1;34m|\033[m')  # Verde
elif n1 == n2 or n2 == n3 or n3 == n1:
    print(f'\033[1;34m|\033[m\033[1;33m{"Triângulo Isósceles!":^{largura-2}}\033[m\033[1;34m|\033[m')  # Amarelo
else:
    print(f'\033[1;34m|\033[m\033[1;35m{"Triângulo Escaleno!":^{largura-2}}\033[m\033[1;34m|\033[m')  # Roxo

print(f'\033[1;34m{linha}\033[m')
