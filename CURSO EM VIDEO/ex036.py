casa = float(input('Coloque aqui o valor da casa: '))
s = float(input('Coloque aqui o seu salario: '))
a = int(input('Coloque aqui em quantos anos voce vai pagar: '))
sim = casa / (a * 12)
nao = 0.30 * s

if sim <= nao:
    print(f'Emprestimo aprovado! A prestação mensal é R$:{sim:.2f}')
else:
    print(f'Emprestimo negado! A prestação mensal de R${nao:.2f} excede 30% de salário.')