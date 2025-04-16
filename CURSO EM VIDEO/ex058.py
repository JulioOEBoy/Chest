from random import randint

palpites = 1
n = randint(0,10)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi?')

p = int(input('Qual é o seu palpite? '))

while p != n :
    if p > n:
        print('Menos... Tente mais uma vez. ')
    elif p < n:
        print('Mais... tente mais uma vez. ')
    p = int(input('Qual é o seu palpite? '))
    palpites += 1

print(f'Parabens você acertou o número era {n}')
print(f'Em {palpites} tentativas!')