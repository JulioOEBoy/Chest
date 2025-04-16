from random import randint
cont = 0
while True:
    numero = randint(1,10)
    print("PAR ou IMPAR? ")
    l = str(input('--')).upper()
    print("Escolha o número!")
    n = int(input('--'))
    soma = numero + n
    if soma % 2 == 1:
        print(f'Você escolheu {l} e o numero {n}, e perdeu! por que a maquina escolheu {numero} e a soma é {soma} mas não é {l}.')
        break
    else:
        print(f'Você escolheu {l} e o numero {n}, e ganhou! por que a maquina escolheu {numero} e a soma é {soma} é {l}')
        cont += 1
        print(f'Voce venceu {cont} vezes')

print(f'Voce venceu {cont} vezes')


