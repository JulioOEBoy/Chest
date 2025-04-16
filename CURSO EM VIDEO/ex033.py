n = int(input('Digite o primeiro número: '))
n1 = int(input('Digite o segundo número: '))
n2 = int(input('Digite o terceiro número: '))
# Verificando quem é o menor
menor = n
if n1 < n and n1 < n2:
    menor = n2
if n2 < n and n2 < n1:
    menor = n2
#Verificando quem é o maior
maior = n
if n1 > n and n1 > n2:
    maior = n1
if n2 > n and n2 > n1:
    maior = n2
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))