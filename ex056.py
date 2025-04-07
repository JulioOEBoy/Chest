velho_idade = 0
novo = ''
total = 0
menores_20 = 0

for c in range(1,5):
    print(f'---- {c}ª PESSOA ----')
    n = str(input('Nome: '))
    idade = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).strip().upper()

    total += idade

    if s == 'F' and idade < 20:
        menores_20 +=1
    elif s == 'M':
        if idade > velho_idade:
            velho_idade = idade
            velho_nome = n

media = total / 4
print(f'A média de idade do grupo é de {media:.1f}')
print(f'Ao todo são {menores_20} mulheres com menos de 20 anos')
if velho_nome :
    print(f'O homem mais velho tem {velho_idade} anos e se chama {velho_nome}')
else:
    print("nenhum homem foi informado!")