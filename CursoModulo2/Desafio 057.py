sexo=str(input('Digite o SEXO: ').upper())
while sexo not in 'MF':
    print('SEXO Inválido! Digite novamente')
    sexo = str(input('Digite o SEXO: ').upper())
print('\n\033[95mParabéns! Você digitou o sexo {} corretamente.'.format(sexo))