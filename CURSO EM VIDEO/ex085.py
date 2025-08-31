valor = []
impar = []
par = []

for c in range(0, 7):
    num = int(input(f'Digite o {c+1}º valor: '))

    if num not in valor:
        if len(valor) == 0 or num > valor[-1]:
            valor.append(num)
        else:
            pos = 0
            while pos < len(valor):
                if num <= valor[pos]:
                    valor.insert(pos, num)
                    break
                pos += 1

    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print('-=-' * 20)
print(f'Valores digitados em ordem: {valor}')
print(f'Pares: {par}')
print(f'Ímpares: {impar}')
print('-=-' * 20)
