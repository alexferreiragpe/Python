print('\n\033[96m********** Estatística de Produtos ***********\n')
totalgasto, mais, menor, cont = 0, 0, 0, 0
opt = 'S'
barato = ''
while opt in 'Ss':
    prod = str(input('\n\033[95mNome do Produto: '))
    valor = float(input('Valor do Produto: R$'))
    opt = str(input('Deseja Continuar: '.upper()))
    totalgasto += valor
    if valor > 1000:
        mais += 1
    if cont == 0:
        menor = valor
        barato = prod
    elif cont > 0:
        if menor > valor:
            menor = valor
            barato = prod
    cont += 1
print('\n\033[93mTotal Gasto: {:.2f}'.format(totalgasto))
print('Total Produtos maior que R$1000,00: {}'.format(mais))
print('Produto mais Barato é o \'{}\' e custa R$ {}'.format(barato, menor))
