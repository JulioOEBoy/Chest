from datetime import datetime
atual = datetime.now().year
maiores = 0
menores = 0

for p in range(1,8):
    ano = int(input(f'Em que ano a {p}º pessoa nasceu? '))
    idade = atual - ano
    if idade <= 17 :
        menores += 1
    else:
        maiores +=1

print(f'Maiores de 18 anos: {maiores}')
print(f'Menores de 18 anos: {menores}')