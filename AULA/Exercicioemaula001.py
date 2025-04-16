nota1 = float(input('Digite sua primeira nota: ').replace(',' , '.'))
nota2 = float(input('Digite sua segunda nota: ').replace(',' , '.'))
media = (nota1 + nota2) / 2
print(f'Sua média foi: {media}')
if media >= 7:
    print(f'provado')
else:
    print(f'Reprovado')
