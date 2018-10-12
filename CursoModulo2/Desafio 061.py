print('\n\033[95m+++++ PROGRESSÃO ARITIMÉTICA COM WHILE +++++\n')
termo = int(input('\033[92mDigite o 1º TERMO da PA: '))
razao = int(input('Digite a RAZÃO da PA: '))
cont = 0
pa = []
totalPa = 0
while cont < 10:
    totalPa = totalPa + termo
    pa.append(totalPa)
    totalPa += razao - termo
    cont += 1
print('\n\033[91mA PROGRESSÃO DE ''{}'' COM A RAZÃO ''{}'' É:\n\033[92m{}'.format(termo,razao,pa))
