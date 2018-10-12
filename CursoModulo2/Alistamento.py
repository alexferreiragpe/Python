from time import sleep
from datetime import date

print('\033[1;34m-=-' * 20, '\n        Alistamento Militar       \n', '-=-' * 20)
anonasc=int(input('Informe o ano de Nascimento: '))
print('\nVerificando dados...\n')
sleep(2)

dif=date.today().year-anonasc

print('Quem nasceu em {}, tem {} ano(s) em {}.\n'.format(anonasc,dif,date.today().year))
if dif<18:
    print('Falta {} ano(s) para o alistamento.'.format(18-dif))
elif dif==0:
    print('Ano de Alistamento, verifique as datas para apresentação.')
elif dif>18:
    print('Seu Alistamento foi a {} ano(s) atrás.'.format(dif-18))