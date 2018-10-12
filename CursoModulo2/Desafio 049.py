valor=int(input('Digite um opcao inteiro para mostrar sua tabuada: '))
for c in range(1,11):
    print('\033[94m{} x {} = {}'.format(valor,c,valor*c))