from time import sleep
print('\n\033[91m********* SEQUÊNCIA DE FIBONACCI **********')
valor = int(input('\n\033[92mDigite quantos Termos deseja exibir: '))
print('\n\033[94mGerando Valores... aguarde\n')
sleep(2)
cont = 3
v1 = 0
v2 = 1
print('\033[95m{} ➠ {} '.format(v1, v2), end='')
while cont <= valor:
    v3 = v1 + v2
    print('\033[95m➠ {} '.format(v3), end='')
    v1 = v2
    v2 = v3
    cont += 1
print(' ➠ FIM')
