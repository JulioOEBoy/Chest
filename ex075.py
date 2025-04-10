numeros = tuple(int(input(f'Digite o {i+1}º número: ')) for i in range(4))
print(f'Você digitou: {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu pela primeira vez na posição {numeros.index(3)+1}º')
else:
    print('O valor 3 não foi digitado.')
pares = [n for n in numeros if n % 2 == 0]
print(f'Os valores pares digitados foram: {pares}')