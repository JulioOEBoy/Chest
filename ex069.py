menores_20 = 0
count = 0
homem = 0
adol = 0

while True:
    count += 1
    print(f'---- {count}ª PESSOA ----')
    n = str(input('Nome: '))
    idade = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).strip().upper()

    if s == 'F' and idade < 20:
        menores_20 += 1
    if idade > 18 :
        adol += 1
    if s == 'M' :
        homem += 1

    b = str(input('Quer continuar ? (S ou N): ')).upper()
    if b == 'N':
        break

print(f'Total de pessoas com 18 anos ou mais: {adol}')
print(f'Total de homens cadastrados: {homem}')
print(f'Total de mulheres com menos de 20 anos: {menores_20}')
