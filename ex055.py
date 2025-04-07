maior = None
menor = None

for c in range(1, 6):
    peso = float(input(f'Digite aqui o peso da {c}ª pessoa: '))

    if maior is None or peso > maior:
        maior = peso
    if menor is None or peso < menor:
        menor = peso

print(f'\nO maior peso é: {maior} kg')
print(f'O menor peso é: {menor} kg')