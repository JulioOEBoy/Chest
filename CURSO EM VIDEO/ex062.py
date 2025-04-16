print('Coloque aqui o termo!')
p = int(input('--'))
print('Coloque aqui a razão!')
r = int(input('--'))
cont = 1
total = 0
mais = 10
while mais != 0 :
    total = total + mais
    while cont <= total:
        print(f'{p} -> ',end='')
        p += r
        cont += 1
    print('Pause')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados')
