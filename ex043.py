largura = 60
linha = '-=-' * 20

print(f'\033[1;34m{linha}\033[m')
print(f'\033[1;34m|\033[m\033[1;31m{"Preencha os valores necessarios:":^{largura-2}}\033[m\033[1;34m|\033[m')
print(f'\033[1;34m{linha}\033[m')

peso = float(input('\033[1;34m--\033[mColoque o seu peso aqui: ').replace(',','.'))
altura = float(input('\033[1;34m--\033[mColoque a sua altura aqui: ').replace(',','.'))
print(f'\033[1;34m{linha}\033[m')

imc = peso / altura ** 2

if imc <= 18.5 :
    print('Voce esta abaixo do peso!')
    print(f'Seu indice de IMC esta: {imc:.1f}')
elif 18.5 <= imc <= 25:
    print('Voce esta no peso ideal')
    print(f'Seu indice de IMC esta: {imc:.1f}')
elif 25 <= imc <= 30:
    print('Voce esta com Sobrepeso')
    print(f'Seu indice de IMC esta: {imc:.1f}')
elif 30 <= imc <= 40:
    print('Voce esta com obesidade')
    print(f'Seu indice de IMC esta: {imc:.1f}')
elif imc >= 40:
    print('\033[1;31mVoce esta com obesidade mormida\033[m')
    print(f'Seu indice de IMC esta: \033[1;31m{imc:.2f}\033[m')
    print('Busque um medico e tente emagracer imediatamente!!!')
print(f'\033[1;34m{linha}\033[m')