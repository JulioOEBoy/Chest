frase='curso em video'
frase[9] pega uma letra do numero
frase[9:13]  pega do 9 até o 13 mas sempre 1 a menos
frase[9:21:2] ele faz a mesma coisa só de que pula de 2 em 2
frase[:5]   pega toda as letras antes de 5 e se por : dps do nmr é a contrario
len(frase)
frase.count(`o`)                       conta quantas dessas letras existe
frase.find(`deo`)                      acha a palavra selecionada que estao na ordem selecionada
frase.find(`Android`)                  procura a palavra no string se nao tiver ficar -1
`curso` in frase
frase.replace(`Python`,`Android`)             troca uma palavra pela outra
frase.upper()        coloca tudo maiusculo
frase.lower()        coloca tudo minusculo
frase.capitalize()      coloca sempre a primeira letra em maiusculo
frase.tittle()        ele faz uma quebra de palavra, e sempre a primeira palavra dps de espaco fica maiusculo
frase.strip()         remove todos os espaços do começo e do fim
frase.rstrip()        se por o r remove só os ultimos espaços e l consequentemente só esquerda
frase.split()         ele divide considerando os espaços e cria palavras separadas e gera uma nova lista de inidice
'-'.join(frase)       ele junta cada elemento de frase e o '-' coloca esse simbolo no lugar que deveria ter espaço se por nada so cria um espaçi
