'''def palindromo(frase):
    frase = frase.lower().replace(' ','')
    return frase == frase [::-1]

frase = str(input('Coloque aqui a sua frase: ').replace(',','.')).strip()

if palindromo(frase):
    print(f'A frase é um polindromo! ')
else:
    print('A frase não é um palindromo. ')'''

frase = input("Digite uma frase: ").strip().lower().replace(" ", "")
if frase == frase[::-1]:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")
