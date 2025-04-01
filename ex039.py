from datetime import datetime
n = int(input('Selecione o ano em que você nasceu: '))
ano = datetime.today().year
idade = ano - n
if idade < 18:
    print(f'Quem nasceu em {n} tem {idade} anos em {ano}.')
    print(f'Ainda falta {18-idade} ano para o alistamento.')
    print('Seu alistamento será em {}.'.format(18-idade+ano))
elif idade > 18:
    print('Você já deveria ter se alistado!')
else:
    print(f'Quem nasceu em {n} e tem 18 anos em {ano}.')
    print('Voce teme que se alistar IMEDIATAMENTE!')