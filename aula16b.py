'''lanche = ('Hambúrguer','Suco', 'Pizza', 'Pudim')
print('lanche[1]')'''

'''lanche = ('Hambúrguer','Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')'''

'''lanche = ('Hambúrguer','Suco', 'Pizza', 'Pudim')

for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi pra caramba')'''

lanche = ('Hambúrguer','Suco', 'Pizza', 'Pudim')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos+1}')

print('Comida pra caramba!')