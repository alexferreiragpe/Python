from time import sleep

print('\033[96m*' * 30)
print('{:^30}'.format('Ferreiras Bank'))
print('\033[96m*' * 30)
print('\n\033[95mSaque Facilitado:\n')
print('\033[94mNotas disponíveis [R$50, R$20, R$10, R$5, R$2 e R$1]\n')
while True:
    try:
        valor = int(input('\033[96mDigite o VALOR Desejado: R$ '))
        break
    except ValueError:
        print('\n\033[95mOoops! Digite um valor Inteiro!')
print('\n\033[93mAguarde... Calculando Troco!\n\033[95m')
sleep(2)
while valor > 0:
    if valor >= 50:
        cinquenta = valor // 50
        valor -= 50 * cinquenta
        print('\033[91m{} - Notas de R$ 50,00'.format(cinquenta))
    elif valor >= 20:
        vinte = ((valor % 50) // 20)
        valor -= 20 * vinte
        print('{} - Notas de R$ 20,00'.format(vinte))
    elif valor >= 10:
        dez = (((valor % 50) % 20) // 10)
        valor -= 10 * dez
        print('{} - Notas de R$ 10,00'.format(dez))
    elif valor >= 5:
        cinco = ((((valor % 50) % 20) % 10) // 5)
        valor -= 5 * cinco
        print('{} - Notas de R$  5,00'.format(cinco))
    elif valor >= 2:
        dois = (((((valor % 50) % 20) % 10) % 5) // 2)
        valor -= 2 * dois
        print('{} - Notas de R$  2,00'.format(dois))
    elif valor >= 1:
        um = ((((((valor % 50) % 20) % 10) % 5) % 2) // 1)
        valor -= 1 * um
        print('{} - Notas de R$  1,00'.format(um))
print('\n\033[95mObrigado e Volte Sempre!')
