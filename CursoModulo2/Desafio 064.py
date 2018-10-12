from time import sleep

print('\n\033[91m********* Somador 1.0 **********')
soma, cont, valor = 0, 0, 0
while valor != 999:
    valor = int(input('\n\033[92mDigite um VALOR INTEIRO: Para SAIR DIGITE [999]: '))
    print('\033[94mVerificando Valor... aguarde')
    sleep(1)
    if valor != 999:
        soma = soma + valor
        cont += 1
print('\n\033[93mCalculando Valores... aguarde')
sleep(2)
print('\n\033[95mForam Digitados: {} Valores.'.format(cont))
print('\n\033[95mSomatória dos Valores é: {}.'.format(soma))