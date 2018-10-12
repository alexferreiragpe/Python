soma=0
for c in range(1,501):
    if c%3==0:
        print(c)
        soma=soma+c
print('\n\033[94mSoma \033[91mde Números \033[0mImpares\033[1m entre 1 e 500 é: '
      '\033[92m{}\033[4m'.format(soma))