def soma ( a , b ):
    return a + b
a = int(input('COloque aqui um valor: '))
b = int(input('COloque aqui um valor: '))
resultado = soma(a,b)
print('Seu numero é \033[1;31m{}\033[m.'.format(resultado))
