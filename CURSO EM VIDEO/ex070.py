soma = 0
qnt = 0
count = 0
menor_valor = None
produto_mais_barato = ''

while True:
    count += 1
    print(f'---- {count}ª Item ----')
    n = str(input('Nome: '))
    while True:
        try:
            valor = float(input('Valor: R$').replace(',','.'))
            break
        except ValueError:
            print('⚠️ Valor inválido! Por favor, digite um número válido.')

    soma += valor

    if valor > 1000:
        qnt += 1

    if menor_valor is None or valor < menor_valor:
        menor_valor = valor
        produto_mais_barato = n
    while True:
        b = input('Quer continuar? (S ou N): ').strip().upper()
        if b in ['S', 'N']:
            break
        print('⚠️ Resposta inválida! Digite apenas S ou N.')

    if b == 'N':
        break

print(f'Total da compra é: R${soma:.2f}')
print(f'Total de itens que custam mais que R$1000 : {qnt}')
print(f'Nome do produto mais barato: {produto_mais_barato}')