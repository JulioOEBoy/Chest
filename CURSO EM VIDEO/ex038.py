n = float(input('Escreva o primeiro valor: ').replace(',','.'))
n1 = float(input('Escreva o segundo valor: ').replace(',','.'))
if n > n1:
    print('O primeiro valor é maior!')
elif n1 > n:
    print('O segundo valor é maior!')
else:
    print('Os dois números são iguais!')

#print('O primeiro valor é maior' if n > n1 else 'O segundo valor é maior' if n1 > n else 'Os dois números são iguais')