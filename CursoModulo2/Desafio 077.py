palavras=('alex','vitor','olivia','cruzeiro','cristina')
vogais=('p','e','i','o','u')
b=[]
print(f'\nEncontrar Vogais nas Palavras usando Tuplas:')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower()in 'aeiou':
            print(letra.upper(),end='')