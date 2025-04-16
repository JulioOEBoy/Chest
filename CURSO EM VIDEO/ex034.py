s = float(input('Digite aqui o seu sálario para o calculo do aumento: ').replace(',','.'))
if s <= 1250:
    print('Seu sálario agora é de R$:{:.2f} '.format(((s*15)/100)+s).replace(',','.'))
else:
    print('Seu sálario agora é de R$:{:.2f} '.format(((s*10)/100)+s).replace(',','.'))