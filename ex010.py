n = float(input('Digite o valor em Dollar a ser convertido para Reais:').replace(',','.'))
n1 = 3.27
n2 = float(n / n1)
print('O valor selecionado foi US$:{} o valor convertido ficará R$:{:.2f}'.format(n,n2))