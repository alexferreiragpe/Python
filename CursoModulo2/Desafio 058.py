from time import sleep
from random import randint

valor = 0
cont = 1
print('\033[95mVou pensar em um número! Tente Adivinha-lo\n'
      'Estou Pensando... aguarde')
sleep(1)
print('Pronto! Pensei...')
valor = randint(0, 11)
resp = int(input('\033[94mQual NÚMERO eu pensei? [0 a 10] : '))
while resp != valor:
    print('Verificando... aguarde')
    sleep(1)
    print('Errou! Tente Novamente')
    resp = int(input('Qual NÚMERO eu pensei? [0 a 10] : '))
    cont += 1
sleep(1)
print('\n\033[95mParabéns! Você conseguiu.\n'
      'Você tentou {} vezes até acertar o {} que havia pensando.'.format(cont, valor))
