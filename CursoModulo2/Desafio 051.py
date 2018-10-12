termo=int(input('Digite o Primeiro Termo da PA: '))
razao=int(input('Digite o Termo da Razão: '))
dec=termo+(10-1)*razao
for c in range(termo,dec,razao):
    print('{} '.format(c),end='-> ')
print('\nFim')