nome = str(input('Qual é o seu nome? ').upper())
if nome == 'GUSTAVO':
    print('Que nome bonito! ')
elif nome == 'JULIO' or nome == 'PEDRO' or nome == 'PAULO':
    print('Seu nome é bem popular no Brasil.')
elif nome == 'JOAO' or nome == 'ANA':
    print('que nome feio!')
else:
    print('Seu nome é bem normal. ')
print('Tenha um bom dia, {}!'.format(nome))