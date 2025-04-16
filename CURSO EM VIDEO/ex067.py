'''r = 'S'
while r == 'S':
    print("Escolha o número que deseja saber a tabuada")
    n = int(input('--'))
    for c in range(0, 11):
        print(f'{n} x {c} = {n * c}')

'''
while True:
    print("Escolha o número que deseja saber a tabuada")
    n = int(input('--'))
    if n == 999:
        break
    for c in range(0, 11):
        print(f'{n} x {c} = {n * c}')
