from time import sleep
from datetime import date
print('-=-'*20,'\n         Verificar Categoria Atleta \n','-=-'*20)
ano = int(input('Digite o Ano de Nascimento: '))
dif=date.today().year-ano
print('')
if dif<10:
    print('Idade: {} Categoria - Mirim'.format(dif))
elif dif<15 and dif>9:
    print('Idade: {} Categoria - Infantil'.format(dif))
elif dif<20 and dif>15:
    print('Idade: {} Categoria - Júnior'.format(dif))
elif dif<21 and dif>19:
    print('Idade: {} Categoria - Sênior'.format(dif))
elif dif>20:
    print('Idade: {} Categoria - Master'.format(dif))