lanche = ('hamburguer','suco','pizza','pudin') #tuplas

lanche = ['hamburguer','suco','pizza','pudin'] #listas
lanche[3] = 'picole'     #substitui e deleta o numero 3 por picole

lanche.append('coockie')     #adciona coockie e cria um novo elemento

lanche.insert(0,'coockie')   #Ele cria uma posição nova e coloca onde voce quer e o python se adapta.

del lanche[3]               #remove pelo numero
lanche.pop(3)               #remove pelo numero
lanche.remove('pizza')      #remove pelo nome

só lanche.pop()       #remove só o ultimo

# se tentar remover algo que não existe da erro

if 'pizza' in lanche:
    lanche.remove('pizza')

    # só remove o que eu quero se tiver para não da erro, é como um checador

valores = list(range(4,11))

valores = [8,2,5,4,9,3,0]
valores.sort()     # ele ordena os valores acima
valores.sort(reverse=True)           #Ele coloca a ordem ao contrario do maior ao menor

len(valores)         # ele conta quantos elementos tem

num.remove(2) #só elemina o primeiro 2
