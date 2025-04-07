'''for c in range(1,10):
    print(c)
print('Fim')'''


'''c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')'''

# condição de parada

'''n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')'''

# S ou N para continuar ou parar
'''r = 'S'
while r == 'S':
    n = int(input("Digite um valor: "))
    r = str(input('Quer continuar [S/N} ')).strip().upper()
print('Fim')'''

#Perguntar quantos numeros que colocou som pares ou impares

n = 1
par = impar = 0

while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print(f'Voce digitou {par} números pares e {impar} números ímpares!')
