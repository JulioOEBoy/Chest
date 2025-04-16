valor = int(input("Digite o valor a ser sacado: "))
cedulas = [50, 20, 10, 1]

for cedula in cedulas:
    quantidade = valor // cedula
    valor = valor % cedula
    if quantidade > 0:
        print(f'Notas de R${cedula}: {quantidade}')