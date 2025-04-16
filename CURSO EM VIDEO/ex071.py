valor = int(input("Digite o valor a ser sacado: "))
cedula = 50
cedula1 = 20
cedula2 = 10
cedula3 = 1
total = valor
cont = 0
cont1 = 0
cont2 = 0
cont3 = 0

while total > 0:
    if total >= cedula:
        total -= cedula
        cont += 1
    elif total >= cedula1:
        total -= cedula1
        cont1 += 1
    elif total >= cedula2:
        total -= cedula2
        cont2 += 1
    elif total >= cedula3:
        total -= cedula3
        cont3 += 1

print(f'\nNotas de R$50: {cont}')
print(f'Notas de R$20: {cont1}')
print(f'Notas de R$10: {cont2}')
print(f'Notas de R$1: {cont3}')