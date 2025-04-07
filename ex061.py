print('Coloque aqui o termo!')
p = int(input('--'))
print('Coloque aqui a razão!')
r = int(input('--'))
cont = 1
while cont <= 10:
    print(f'{p} -> ',end='')
    p += r
    cont += 1
print('Fim')