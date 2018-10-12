from time import sleep

print('\033[1;34m-=-' * 20, '\n        Número Maior       \n', '-=-' * 20)
v1=int(input('Primeiro Valor: '))
v2=int(input('Segundo Valor: '))
print('Verificando... Aguarde...')
sleep(2)
if v1>v2:
    print('O Valor Maior é o {}, e o Menor é {}.'.format(v1,v2))
elif v2>v1:
    print('O Valor Maior é o {}, e o Menor é {}.'.format(v2, v1))
else:
    print('Os valores são iguais.')
