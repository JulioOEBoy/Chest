n = int(input('Quantos termos voce quer mostrar? '))
f = 0
f1 = 1
print(f'{f} -> {f1}',end='')

cont = 3
while cont <= n:
    f2 = f + f1
    print(f' -> {f2}',end='')
    f = f1
    f1 = f2
    cont += 1

print(' -> FIM')