from time import sleep
print('\n\033[95m+++++ PROGRESSÃO ARITIMÉTICA COM WHILE +++++\n')
termo = int(input('\033[92mDigite o 1º TERMO da PA: '))
razao = int(input('Digite a RAZÃO da PA: '))
cont = 0
pa = []
totalPa = 0
opcao = 'S'
while cont < 10:
    totalPa = totalPa + termo
    pa.append(totalPa)
    totalPa += razao - termo
    cont += 1
    if cont == 10:
        print('\n\033[96m********* INÍCIO **********')
        print('\n\033[93mAguarde... Calculando a PA')
        sleep(2)
        print('\n\033[91mA PROGRESSÃO DE ''{}'' COM A RAZÃO ''{}'' É:\n\033[92m{}'.format(termo, razao, pa))
        opcao = str(input('\nDeseja exibir mais TERMOS [S/N]: '.upper()))
        while opcao in 'Ss' and cont < 20:
            totalPa = totalPa + termo
            pa.append(totalPa)
            totalPa += razao - termo
            cont += 1
            if cont == 20:
                opcao = 'N'
                print('\n\n\033[94mAguarde... Calculando próximos valores da PA')
                sleep(2)
                print('\n\033[91mPróximos TERMOS DA PROGRESSÃO DE ''{}'' COM A RAZÃO ''{}'' SÃO:\n\033[92m{}'.format(
                    termo, razao, pa))
        print('\n\033[96m********* FIM **********')
