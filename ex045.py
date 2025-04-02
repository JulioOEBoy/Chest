import random
import time

def jogar():
    computador = random.randint(0,2)

    largura = 60
    linha = '-=-' * 20

    print(f'\033[1;34m{linha}\033[m')
    print(f'\033[1;34m|\033[m\033[1;31m{"Suas opcoes":^{largura-2}}\033[m\033[1;34m|\033[m')
    print(f'\033[1;34m{linha}\033[m')

    print('[0] PEDRA ')
    print('[1] PAPEL ')
    print('[2] TESOURA ')
    print(f'\033[1;34m{linha}\033[m')
    print('Qual e a sua jogada? ')

    numero = int(input('--'))
    print("Obrigado por jogar! Até a próxima.")
    print(f'\033[1;34m{linha}\033[m')
    print('JO...')
    time.sleep(1)
    print('ken..')
    time.sleep(1)
    print('PO.')
    print(f'\033[1;34m{linha}\033[m')
    time.sleep(1)

    opcoes = ["PEDRA", "PAPEL", "TESOURA"]

    if numero == computador:
        print(f'A opcao escolhida foi {opcoes[numero]} e o robo jogou {opcoes[computador]} ')
        print('Foi empate! ')
        print('Tente de novo ')
        print(f'\033[1;34m{linha}\033[m')
    elif numero == 0 and computador == 1:
        print(f'A opcao escolhida foi {opcoes[numero]} e o robo jogou {opcoes[computador]} ')
        print('Voce perdeu!')
        print('Tente de novo')
        print(f'\033[1;34m{linha}\033[m')
    elif numero == 0 and computador == 2:
        print(f'A opcao escolhida foi {opcoes[numero]} e o robo jogou {opcoes[computador]} ')
        print('Voce ganhou!')
        print(f'\033[1;34m{linha}\033[m')
    elif numero == 2 and computador == 0:
        print(f'A opcao escolhida foi {opcoes[numero]} e o robo jogou {opcoes[computador]} ')
        print('Voce perdeu!')
        print('Tente de novo')
        print(f'\033[1;34m{linha}\033[m')
    elif numero == 2 and computador == 1:
        print(f'A opcao escolhida foi {opcoes[numero]} e o robo jogou {opcoes[computador]} ')
        print('Voce ganhou!')
        print(f'\033[1;34m{linha}\033[m')
    elif numero == 1 and computador == 0:
        print(f'A opcao escolhida foi {opcoes[numero]} e o robo jogou {opcoes[computador]} ')
        print('Voce ganhou!')
        print(f'\033[1;34m{linha}\033[m')
    elif numero == 1 and computador == 2:
        print(f'A opcao escolhida foi {opcoes[numero]} e o robo jogou {opcoes[computador]} ')
        print('Voce perdeu!')
        print('Tente de novo')
        print(f'\033[1;34m{linha}\033[m')
    else:
        print('Escolha uma forma válida para jogar!')
        print(f'\033[1;34m{linha}\033[m')

    jogar_novamente = input("Pressione Enter para jogar novamente ou digite 'sair' para encerrar: ").lower()
    if jogar_novamente != 'sair':
        jogar()


jogar()