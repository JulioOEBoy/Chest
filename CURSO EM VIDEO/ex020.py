import random

nomes = [input(f'Selecione o nome do lider do grupo {i+1}: ')for i in range(4)]

random.shuffle(nomes)

for i, nome in enumerate(nomes,1):
    print(f'{i} lugar: {nome}')