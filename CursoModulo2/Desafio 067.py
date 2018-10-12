n=int(input('Digite o valor para exibir a tabuada: '))

while n>0:
    for a in range(10):
        print('{} x {} = {}'.format(n,a+1,(n*(a+1))))
    n = int(input('\nDigite o valor para exibir a tabuada: '))