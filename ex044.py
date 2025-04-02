largura = 60
linha = '-=-' * 20

print(f'\033[1;34m{linha}\033[m')
print(f'\033[1;34m|\033[m\033[1;31m{"Supermecado Cesar":^{largura-2}}\033[m\033[1;34m|\033[m')
print(f'\033[1;34m{linha}\033[m')

valor = float(input('\033[1;34m--\033[mValor da compra: R$ ').replace(',','.'))
print(f'\033[1;34m{linha}\033[m')

print('[1] a vista dinheiro/cheque')
print('[2] a vista cartao')
print('[3] 2x no cartao')
print('[4] 3x ou mais no cartao')
print(f'\033[1;34m{linha}\033[m')

print('\033[1;34m--\033[mFORMAS DE PAGAMENTO')
forma = int(input('\033[1;34m--\033[m' ))
print(f'\033[1;34m{linha}\033[m')

if forma == 1:
    valor1 = (valor * 10) / 100
    print(f'Sua compra de \033[1;32mR$:{valor:.2f}\033[m vai custar \033[1;33mR$:{valor - valor1:.2f}\033[m ')
    print(f'\033[1;34m{linha}\033[m')
    print(f'\033[1;34m|\033[m\033[1;33m{"Volte sempre":^{largura-2}}\033[m\033[1;34m|\033[m')
    print(f'\033[1;34m{linha}\033[m')
elif forma == 2:
    valor2 = (valor * 5) / 100
    print(f'Sua compra de \033[1;32mR$:{valor:.2f}\033[m vai custar \033[1;33mR$:{valor - valor2:.2f}\033[m ')
    print(f'\033[1;34m{linha}\033[m')
    print(f'\033[1;34m|\033[m\033[1;33m{"Volte sempre":^{largura - 2}}\033[m\033[1;34m|\033[m')
    print(f'\033[1;34m{linha}\033[m')
elif forma == 3:
    valor3 = valor / 2
    print(f'Sua compra de \033[1;32mR$:{valor:.2f}\033[m vai custar 2 parcelas de \033[1;33mR$:{valor3}\033[m ')
    print(f'\033[1;34m{linha}\033[m')
    print(f'\033[1;34m|\033[m\033[1;33m{"Volte sempre":^{largura - 2}}\033[m\033[1;34m|\033[m')
    print(f'\033[1;34m{linha}\033[m')
elif forma == 4:
    valor4 = (valor * 20) / 100
    valor5 = valor + valor4
    print(f'Sua compra de \033[1;32mR$:{valor:.2f}\033[m vai custar \033[1;33mR$:{valor5:.2f}\033[m ')
    parcela = int(input('Quantas parcelas deseja ?'))
    print(f'Voce quer {parcela} parcelas, o valor de cada fica \033[1;33mR$:{valor5 / parcela:.2f}\033[m ')
    print(f'\033[1;34m{linha}\033[m')
    print(f'\033[1;34m|\033[m\033[1;33m{"Volte sempre":^{largura - 2}}\033[m\033[1;34m|\033[m')
    print(f'\033[1;34m{linha}\033[m')
else:
    print('\033[1;31mDigite uma forma de pagamento valida!\033[m')
    print('\033[1;31mNao desiste tente novamente!\033[m')
    print(f'\033[1;34m{linha}\033[m')