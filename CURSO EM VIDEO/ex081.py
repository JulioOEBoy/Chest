import time
lista = []
c = 1

while True:
    numero = int(input('Digite um valor: '))
    if numero not in lista:
        if len(lista) == 0 or numero > lista[-1]:
            lista.append(numero)
        else:
            pos = 0
            while pos < len(lista):
                if numero <= lista[pos]:
                    lista.insert(pos, numero)
                    break
                pos += 1

    resposta = input('Quer continuar? [S/N] ').strip().upper()
    while resposta not in ['S', 'N']:
        resposta = input('Resposta inválida. Digite apenas [S/N]: ').strip().upper()

    if resposta == 'N':
        break

print('-=-'*20)
print('Calculando.')
time.sleep(1)
print('Calculando..')
time.sleep(1)
print('Calculando...')
time.sleep(1)
print('-=-'*20)
print('AS RESPOSTAS FORAM GERADAS')
time.sleep(1)
print('-=-'*20)
print(f'O número total de números digitados foram: {len(lista)}')
print('-=-'*20)
time.sleep(1)
lista.sort(reverse=True)
print(f'A ordem decrescente é: {lista}')
time.sleep(1)
print('-=-'*20)

if 5 in lista:
    print(f'O número 5 está na posição {lista.index(5)}')
else:
    print('Não possui o número 5')
print('-=-'*20)