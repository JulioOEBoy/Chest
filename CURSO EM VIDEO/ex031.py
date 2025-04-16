d = float(input('Escreva a distancia da sua viagem em km: '))
if d <= 200:
    print('A viagem custará R$:{:.2f}'.format(d*1/2))
else:
    print('A viagem custará R$:{:.2f}'.format(d*0.45))