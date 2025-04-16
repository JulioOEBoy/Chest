print('Coloque aqui o número que quer saber se é número primo ou não!')
n = int(input('--'))

divisores = 0

for i in range (1, n + 1):
    if n % i == 0:
        divisores += 1

if divisores == 2:
    print(f'O número {n} é primo')
else:
    print(f'O número {n} não é primo')