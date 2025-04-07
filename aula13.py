#for c in range (1,7):
    #print(c)
#rint('Fim')

# no for c in range (1,7) se eu quiser que ele conte ao contrario é só colocar (1,7, -1)
# se eu colocar por exemplo (1,8, 2) ele conta de 2 em 2

'''n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('fim')
'''
#outra ideia basica
i = int(input('Inicio: '))
f = int(input('FIM: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('fim')