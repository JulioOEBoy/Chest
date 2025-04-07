sexo = ''
while sexo not in ['m', 'M', 'f', 'F']:
    sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()
    if sexo not in ['M','F']:
        print('Digite uma opção valida: ')

print(f'Voce escolheu o sexo {sexo}')
