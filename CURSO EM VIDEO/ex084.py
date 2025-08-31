galera = []
dado = []
totmai = totmen = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    galera.append(dado[:])
    dado.clear()

    resposta = input('Quer continuar? [S/N] ').strip().upper()
    while resposta not in ['S', 'N']:
        resposta = input('Resposta inválida. Digite apenas [S/N]: ').strip().upper()
    if resposta == 'N':
        break

pesos = [p[1] for p in galera]
maior = max(pesos)
menor = min(pesos)

for p in galera:
    if p[1] >= 100:
        totmai += 1
    elif p[1] <= 70:
        totmen += 1

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(galera)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
print(', '.join([p[0] for p in galera if p[1] == maior]))

print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
print(', '.join([p[0] for p in galera if p[1] == menor]))

print(f'\nExtras:')
print(f'Pessoas com 100Kg ou mais: {totmai}')
print(f'Pessoas com 70Kg ou menos: {totmen}')
print('-=' * 30)
