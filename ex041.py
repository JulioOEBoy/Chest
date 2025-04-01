from datetime import datetime
print('Descubra sua classificação baseado no ano de nascimento!')
ano = int(input('Coloque aqui o seu ano de nascimento: '))
atual = datetime.today().year
idade = atual - ano
print(f'O atleta tem {idade} anos.')
if idade < 9.1:
    print('MIRIM')
elif idade > 8.9 and idade < 14.1 :
    print('INFANTIL')
elif idade > 13.9 and idade < 19.1 :
    print('Júnior')
elif idade > 18.9 and idade < 25.1 :
    print('Sênior')
else:
    print('Master')