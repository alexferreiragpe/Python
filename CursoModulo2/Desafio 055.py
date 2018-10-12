maior = 0
menor = 0
for c in range(1, 6):
    num = float(input('Digite o {}º Peso: '.format(c)).replace(',', '.'))
    if maior < num:
        maior = num
    elif menor == 0:
        menor = num
    if menor == 0 or menor > num:
        menor = num
print('\nO MAIOR PESO é: {}'.format(maior))
print('O MENOR PESO é: {}'.format(menor))
