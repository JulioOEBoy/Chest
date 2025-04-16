n = 0
v = [c for c in range (1, 501, 2) if c % 3 == 0]

for c in v:
    n += c

print(f'O somatório de todos os valores impares foi {n}')