'''a = float(input('Digite aqui um ano: '))
if a % 4 == 0:
    print('Ano bissexto')
else:
    print('Não é ano bissexto')'''
from selectors import SelectSelector
from datetime import date
a = float(input('Digite aqui um ano: '))
'''if ano = 0:
    ano = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0'''
print('Ano bissexto!' if a % 4 == 0 and a % 100 != 0 or a % 400 == 0 else 'Não é bissexto!')