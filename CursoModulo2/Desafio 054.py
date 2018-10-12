from datetime import date
cont = 0
cont2 = 0
for c in range(1, 8):
    ano = int(input('{}º - Digite o Ano de Nascimento: '.format(c)))
    if date.today().year - ano >= 21:
        cont = cont + 1
    else:
        cont2 = cont2 + 1
print('\n{} data(s) informada(s) ainda não tem 21 anos.'.format(cont2))
print('\n{} data(s) informada(s) já tem 21 anos ou mais.'.format(cont))
