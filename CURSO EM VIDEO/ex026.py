frase = str(input('Digite um frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A últim letra A apareceu na posição {}'.format(frase.rfind('A')+1))
