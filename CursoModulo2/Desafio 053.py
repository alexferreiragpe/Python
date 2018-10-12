frase = str(input('Digite a Frase para verificar se é Palíndromo: ').replace(' ', '').upper())
fraserevertida = frase[::-1]
if frase == fraserevertida:
    print('É uma frase Palíndromo')
else:
    print('Não é uma frase Palíndromo')
