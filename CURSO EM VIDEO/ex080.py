lista = []
c = 1

while c <= 5:
    numero = int(input(f'Digite um valor para posição ({c})° '))

    if len(lista) == 0 or numero > lista[-1]:
        lista.append(numero)
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                break
            pos += 1
    c += 1

print(f'Os valores digitados em ordem foram: {lista}')