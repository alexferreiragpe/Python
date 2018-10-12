print('\033[94m********** Fatorial em Python **********\n')
fat=int(input('\033[91mDigite o VALOR INTEIRO para exibir seu FATORIAL: '))
cont=fat
soma=1
lista=[]
while fat>0:
    lista.append(str(fat)+' x')
    soma=soma*fat
    fat-=1
print('\n\033[95mFatorial de {} é:\n\033[96m{}'.format(cont,soma))
print(' '.join(map(str, lista)))


