valor = []
impar = []
par = []

while True:
    numero = int(input('Digite um valor: '))

    if numero not in valor:
        if len(valor) == 0 or numero > valor[-1]:
            valor.append(numero)
        else:
            pos = 0
            while pos < len(valor):
                if numero <= valor[pos]:
                    valor.insert(pos, numero)
                    break
                pos += 1

        if numero % 2 == 0:
            par.append(numero)
        else:
            impar.append(numero)

    resposta = input('Quer continuar? [S/N] ').strip().upper()
    while resposta not in ['S', 'N']:
        resposta = input('Resposta inválida. Digite apenas [S/N]: ').strip().upper()

    if resposta == 'N':
        break

print('-=-' * 20)
print(f'Valores digitados: {valor}')
print(f'Pares: {par}')
print(f'Ímpares: {impar}')
print('-=-' * 20)
