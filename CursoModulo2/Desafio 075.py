valor,cont,nove,pares = [],0,0,[]
while cont < 4:
    valor.append(int(input('\033[95mDigite o {}º valor: '.format(cont + 1))))
    cont += 1
for c in valor:
    if c == 9:
        nove += 1
    if c % 2 == 0:
        pares.append(c)

print('\n\033[93mOs valores Digitados foram', valor)

if nove > 0:
    print('\n\033[92mO número 9 apareceu {} vezes'.format(nove))
else:
    print('\n\033[92mO número 9 não foi digitado!')

try:
    print('O número 3 apareceu pela primeira vez na posição {}'.format(valor.index(3) + 1))
except:
    print('O número 3 não foi digitado!')

if len(pares)>0:
    print('Os valores pares digitados foram:', pares)
else:
    print('Não foi digitado nenhum número Par!')