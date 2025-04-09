from random import randint

print(f'Os números sorteados foram:')
count = 0
max = None
min = None

while count < 5:
    n = randint(1,10)
    print(f'({n}) ', end='')

    if count == 0:
        max = min = n
    else:
        if n > max:
            max = n
        if n < min:
            min = n

    count += 1

print(f'\nO maior valor foi: {max}')
print(f'O menor valor foi: {min}')

