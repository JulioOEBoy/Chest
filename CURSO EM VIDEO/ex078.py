lista = []
c = 1
maior = None
menor = None
while c <= 5:
    numero = int(input(f'Digite um valor para posição ({c})° '))
    lista.append(numero)
    c += 1
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero

pos_maior = [i + 1 for i, v in enumerate(lista) if v == maior]
pos_menor = [i + 1 for i, v in enumerate(lista) if v == menor]


print(f'O maior número é {maior} na posição {pos_maior}')
print(f'O menor número é {menor} na posição {pos_menor}')

