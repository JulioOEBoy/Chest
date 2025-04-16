n = float(input("Coloque aqui o seu sálario que irá receber o aumento de 15%:").replace(',','.'))
n1 = 15 * n
n2 = n1 / 100
n3 = n + n2
print('O seu sálario de R$:{}, irá aumentar para R$:{:.2f} com os 15% de desconto.'.format(n,n3))