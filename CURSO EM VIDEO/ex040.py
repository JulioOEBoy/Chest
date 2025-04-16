print('Coloque duas notas para calcular a media!')
nota1 = float(input('Coloque aqui a primeira nota: ').replace(',','.'))
nota2 = float(input('Coloque aqui a segunda nota: ').replace(',','.'))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1} e {nota2}, a média do aluno é {media}')
if media < 5.1 :
    print('Reprovado!')
elif media > 6.9 :
    print('Aprovado!')
else:
    print('Recuperação!')
