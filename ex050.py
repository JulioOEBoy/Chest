n = 0
for _ in range (0,7):
    c = int(input("Coloque um número aqui: "))
    if c %2 == 0:
        n += c

print(f'O somatório de todos os valores pares foi {n}')