cont = 0
from datetime import date
n = int(input('\033[95mdigite o número de pessoas para consultar: '))
while cont < n:
    dia = int(input('\n\033[92mdigite o dia de nasc da pessoa: '))
    mes = int(input('digite o mês:'))
    ano = int(input('digite o ano de nasc: ex: xxxx '))
    cont += 1
    print('\n\033[91mA {}ª pessoa fará {} anos no dia {}/{}/{}'.format(cont, (date.today().year - ano) + 1, dia, mes,
                                                                       (date.today().year) + 1))
