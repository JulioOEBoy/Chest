n = int(input('Digite um número para calcular seu fatorial: '))
c = n
fatorial = 1

print(f'Calculando {n}!')
while c > 0:
    print(f'{c}',end='')
    print(f' x ' if c > 1 else ' = ', end='')
    fatorial *= c
    c -= 1

print(f'{fatorial}')