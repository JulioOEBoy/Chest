n = float(input('Coloque aqui o valor do produto para receber o desconto de 5%:').replace(',','.'))
n1 = 5 * n
n2 = n1 / 100
n3 = n - n2
print('O valor R$:{} com 5% de desconto ficará no valor de R$:{:.2f}, com R$:{:.2f} de desconto.'.format(n,n3,n2))