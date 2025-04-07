from time import sleep

primeiro = float(input('Coloque o primeiro valor: '))
segundo = float(input('Coloque o segundo valor : '))

while True:
    print('    [ 1 ] Somar')
    print('    [ 2 ] Multiplicar')
    print('    [ 3 ] Maior')
    print('    [ 4 ] Novos números')
    print('    [ 5 ] Sair do programa')

    n = int(input('Digite a opção: '))

    if n == 1:
        print(f'{primeiro} + {segundo} = {primeiro+segundo}')
    elif n == 2:
        print(f'{primeiro} x {segundo} = {primeiro*segundo}')
    elif n == 3:
        if primeiro > segundo:
            print(f'O {primeiro:.0f} é maior!')
        elif segundo > primeiro:
            print(f'O {segundo:.0f} é maior!')
    elif n == 4:
        primeiro = float(input('Coloque o primeiro valor: '))
        segundo = float(input('Coloque o segundo valor : '))

    elif n == 5:
        print('Finalizando o programa... Até logo!')
        break

    else:
        print('Opção invalida! Tente novamente.')
    sleep(5)
