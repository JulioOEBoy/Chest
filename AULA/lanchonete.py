total_pedido = []  # lista
import time


def lin():
    print(' \033[31m -=*=-\033[m' * 10)


titulo = "MENU PYTHON BURGER:"
lin()
print(titulo.center(68, '*'))
lin()
time.sleep(0.5)


def menu_hamburguer():  # função menu opções
    print(""" \033[32m
1- Coral Burger.......................................................... R$ 27
   (Blend de carnes (140g) + cheddar + pasta tomate defumad+ anéis de cebola)

2- Cascavel Burger     ..................................................... R$ 30
   (Blend de carnes (140g) + duplo cheddar + molho da casa + duplo bacon + salada)

3- Surucucu Burger (Combo para compartilhar) ............................... R$ 62
   (2 Burguers blend (140g cada), duplo cheddar+ duplo bacon +picles + catupiry + salada)

4- Jararaca Burger (combo família) ......................................... R$ 90
   (4 Burguer blend (100g) cada + cheddar + bacon+ salada)

5- Píton burger ............................................................ R$ 30
   (Blend de carnes ( 140g) + duplo bacon + duplo cheddar + catupiry empanado + molho da casa + salada)\033[m

  \033[1;31;40m 0 - SEM BURGER \033[m

""")
    return int(input('Digite o código do seu burguer: '))  # resposta para o menu hamburguer


def menu_acomp():
    print(""" \033[32m
    Acompanhamento:

   Batata média .......................................................... R$ 18
\033[m
""")


def bebidas():
    print('''\033[32m
    Bebida: 

1- Refrigerante em lata .......................................................... R$ 6

2- Refrigerante 1,5L .......................................................... R$ 10\033[m

 \033[1;31;40m0 - SEM BEBIDA \033[m
''')
    return int(input('Digite o código da sua bebida: '))


def sobremesa():
    print(''' \033[32m
    Sobremesa:

1- Brownie recheado com Nutella .......................................................... R$ 6 \033[m
''')


while True:
    coral = 27
    cascavel = 30
    surucucu = 62
    jararaca = 90
    píton = 30
    time.sleep(1)
    try:
        lanche = menu_hamburguer()
    except(ValueError, TypeError, NameError):
        print('Digite um valor válido!')
        continue
    if lanche == 0:
        break
    if lanche == 1:
        print('Você escolheu: Coral Burger!')
        conf = ' '
        while conf not in 'SN':
            conf = str(input('Confirma? [S/N]')).upper()[0]
            if conf == 'S':
                q = int(input('Digite a Quantidade:'))
                total = q * coral
                total_pedido.append(total)

            elif conf == 'N':
                outped = ' '
                while outped not in 'SN':
                    outped = str(input('Deseja fazer um pedido? [S/N]')).upper()[0]
                    if outped == 'S':
                        menu_hamburguer()
                    if outped == 'N':
                        break
    elif lanche == 2:
        print('Você escolheu: Cascavel Burger!')
        conf = ' '
        while conf not in 'SN':
            conf = str(input('Confirma? [S/N]')).upper()[0]
            if conf == 'S':
                q = int(input('Digite a Quantidade:'))
                total = q * cascavel
                total_pedido.append(total)

            elif conf == 'N':
                outped = ' '
                while outped not in 'SN':
                    outped = str(input('Deseja fazer um pedido? [S/N]')).upper()[0]
                    if outped == 'S':
                        menu_hamburguer()
                    if outped == 'N':
                        break
    elif lanche == 3:
        print('Você escolheu: Surucucu Burger!')
        conf = ' '
        while conf not in 'SN':
            conf = str(input('Confirma? [S/N]')).upper()[0]
            if conf == 'S':
                q = int(input('Digite a Quantidade:'))
                total = q * surucucu
                total_pedido.append(total)

            elif conf == 'N':
                outped = ' '
                while outped not in 'SN':
                    outped = str(input('Deseja fazer um pedido? [S/N]')).upper()[0]
                    if outped == 'S':
                        menu_hamburguer()
                    if outped == 'N':
                        break
    elif lanche == 4:
        print('Você escolheu: Jararaca Burger!')
        conf = ' '
        while conf not in 'SN':
            conf = str(input('Confirma? [S/N]')).upper()[0]
            if conf == 'S':
                q = int(input('Digite a Quantidade:'))
                total = q * jararaca
                total_pedido.append(total)

            elif conf == 'N':
                outped = ' '
                while outped not in 'SN':
                    outped = str(input('Deseja fazer um pedido? [S/N]')).upper()[0]
                    if outped == 'S':
                        menu_hamburguer()
                    if outped == 'N':
                        break
    elif lanche == 5:
        print('Você escolheu: Píton Burger!')
        conf = ' '
        while conf not in 'SN':
            conf = str(input('Confirma? [S/N]')).upper()[0]
            if conf == 'S':
                q = int(input('Digite a Quantidade:'))
                total = q * píton
                total_pedido.append(total)
            elif conf == 'N':
                outped = ' '
                while outped not in 'SN':
                    outped = str(input('Deseja fazer um pedido? [S/N]')).upper()[0]
                    if outped == 'S':
                        menu_hamburguer()
                    if outped == 'N':
                        break
    elif lanche < 1 or lanche > 5:
        print('Número inválido! Tente novamente')
        lanche = menu_hamburguer()
    break
while True:
    try:
        batata = menu_acomp()
    except(ValueError, TypeError, NameError):
        print('Digite um valor válido!')
        continue
    conf = ' '
    while conf not in 'SN':
        conf = str(input('Deseja incluir batatas? [S/N]: ')).upper()[0]
        if conf == 'S':
            batata = 18
            q = int(input('Digite a Quantidade:'))
            total = q * batata
            total_pedido.append(total)

        elif conf == 'N':
            break
    break
while True:
    bebida = 0
    try:
        bebida = bebidas()
    except(ValueError, TypeError, NameError):
        print('Digite um valor válido!')
        continue
    if bebida == 0:
        break
    if bebida == 1:
        print('Você escolheu: refrigerante em lata! ')
        conf = ' '
        while conf not in 'SN':
            conf = str(input('Confirma? [S/N]: ')).upper()[0]
            if conf == 'S':
                bebida1 = 6
                q = int(input('Digite a Quantidade:'))
                total = q * bebida1
                total_pedido.append(total)

            elif conf == 'N':
                break
    elif bebida == 2:
        print('Você escolheu: Refrigerante 1,5 L!')
        conf = ' '
        while conf not in 'SN':
            conf = str(input('Confirma? [S/N]: ')).upper()[0]
            if conf == 'S':
                bebida2 = 10
                q = int(input('Digite a Quantidade:'))
                total = q * bebida2
                total_pedido.append(total)

            elif conf == 'N':
                break
    elif bebida < 1 or bebida > 2:
        print('Numero inválido, tente novamente')
        bebida = bebidas()
    break
while True:
    sobremesa = sobremesa()
    conf = ' '
    while conf not in 'SN':
        conf = str(input('Deseja incluir brownie? :)) [S/N]: ')).upper()[0]
        if conf == 'S':
            sobremesa = 6
            q = int(input('Digite a Quantidade:'))
            total = q * sobremesa
            total_pedido.append(total)

        elif conf == 'N':
            break
    break

print('Calculando pedido...')
time.sleep(1.5)
print(f'Seu pedido custa R${sum(total_pedido)}\n')


def pagamento():
    print(''' Qual será a forma de pagamento?
    1 - Cartão 
    2- Dinheiro 
    ''')


pagamento = pagamento()
while True:
    try:
        n = int(input('Digite o código da forma de pagamento: '))
    except (ValueError, TypeError):
        print('ERRO! Por favor, um  número válido')
        continue
    if n == 1:
        time.sleep(0.5)
        print('''Sua opção de pagamento é cartão!'\n
                Seu pedido está sendo processado... 
                Apresente no balcão o seu número de pedido para finalizar a compra.\n ''')
    elif n == 2:
        print('Troco para quanto?')
        troco = 0
        while True:
            try:
                troco = float(input(f'[Digite 0 se não precisa de troco]:  '))
            except(ValueError, TypeError):
                print('Digite um valor válido!')
            if troco == 0:
                print(f'Valor à pagar: {sum(total_pedido)}')
                break
            if troco > (sum(total_pedido)):
                print(f'troco será de R$ {troco - (sum(total_pedido))}')
                break
    elif n < 1 and n > 2:
        print('Digite um código válido!')
        n = pagamento()
    break
from random import randint

num_pedido = randint(100, 900)
print(f'Seu número de pedido é:{num_pedido}')
time.sleep(0.5)
print('Obrigado pela preferência! Volte sempre!! :))')