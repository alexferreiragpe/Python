soma=0
for c in range(1,7):
    valor=int(input('Digite o {}º opcao: '.format(c)))
    if valor%2==0:
        soma=soma+valor
print('\n\033[94mA soma dos números pares é: {}'.format(soma))
