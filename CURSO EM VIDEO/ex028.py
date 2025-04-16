import random
print('-=-'*20)
n = random.randint(0,5)
r = int(input('Selecione um número : '))

print('-=-'*20)

print('PROCESSANDO...')

print('-=-'*20)
print('O número escolhido foi: {}'.format(r))
print('O número ganhador foi: {}'.format(n))
print('-=-'*20)
print('-----Você ganhou------' if r == n else '-----Você perdeu------')
print('-=-'*20)
