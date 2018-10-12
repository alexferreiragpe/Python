produtos=['Arroz',15.99,'Feijão',5.40]
print('-'*40)
print(f'{"Listagem de Preços":^40}')
print('-'*40)
for pos in range(0,len(produtos)):
    if pos%2==0:
        print(f'{produtos[pos]:.<30}',end='')
    else:
        print(f'R$ {produtos[pos]:>5.2f}')
print('-'*40)