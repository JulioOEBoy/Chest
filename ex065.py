n = 0
soma = 0
cont = 0
maior = None
menor = None
r = 'S'
while r == 'S':
    n = int(input("Digite um valor: "))
    r = str(input('Quer continuar [S/N} ')).strip().upper()
    soma += n
    cont += 1
    if maior is None or n > maior:
        maior = n
    if menor is None or n < menor:
        menor = n

print(f'Você digitou {cont} números e a média foi {soma / cont}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
