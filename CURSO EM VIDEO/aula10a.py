from unittest.mock import sentinel

carro.siga()
carro.esquerda()
carro.siga()
carro.direitra()
carro.siga()
carro.direita()
carro.siga()
carro.esquerda()
carro.siga()
carro.pare()
2 caminhos
carro.siga
bifurcação(nao é comando)
                carro.siga()

se carro.esquerda()          senão

carro.siga()                 carro.siga()
carro.direitra()             carro.esquerda()
carro.siga()                 carro.siga()
carro.direita()              carro.esquerda()
carro.esquerda()             carro.siga()
carro.siga()
carro.direita()
carro.siga()
                  carro.pare()

reorganizado

carro.siga()

se carro.esquerda()
    carro.siga()
    carro.direitra()
    carro.siga()
    carro.direitra()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()

senão

    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()

carro.pare()

codigo

se carro.esquerda()
    bloco _v_
senão
    bloco _F_

codigo real em ingles

if carro.esquerda():
    bloco True
else:
    bloco False


tempo = int(input('Quantos anos tem seu carro?: '))
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')

ou

tempo = int(input('Quantos anos tem seu carro?: '))
print('carro novo' if tempo<=3 else 'carro velho')
print('--FIM--')