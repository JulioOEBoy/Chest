velocidade = float(input('Escreva uma velocidade: '))
if velocidade <= 80:
    print('O carro está na velocidade normal!')
else:
    print('Sua velocidade passou do limite! Sua multa será de R$:{} reais.'.format((velocidade-80)*7,00))


