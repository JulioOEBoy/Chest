valor = []

while True:
    numero = int(input('Digite um valor: '))

    if numero not in valor:
        valor.append(numero)

    resposta = input('Quer continuar? [S/N] ').strip().upper()
    while not resposta in ['S', 'N']:
        resposta = input('Resposta inválida. Digite apenas [S/N]: ').strip().upper()

    if resposta == 'N':
        break

print(f'Números digitados (ordenados): {sorted(valor)}')
