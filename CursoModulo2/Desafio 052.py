num=int(input('Digite o Valor para Verificar se é um número primo: '))
cont=0
for c in range(1,num+1):
    if num % c==0 or num==2:
        print('\033[94m{} '.format(c),end='')
        cont=cont+1
    else:
        print('\033[95m{} '.format(c),end='')
if cont<3:
    print('\nO número {} é Primo.'.format(num))
else:
    print('\nO número {} não é Primo, pois foi divido {} vezes.'.format(num,cont))