from time import sleep

print('\n\033[91m********* Calcular Média... Maior/Menor Valor 1.0 **********')
soma, cont, opcao, valor = 0, 0, 'S', 0
lista = []
while opcao == 'S':
    valor = int(input('\n\033[92mDigite um VALOR INTEIRO: '))
    opcao = str(input('\033[95mDeseja continuar digitando [S/N]: ').upper().strip()[0])
    print('\033[94mVerificando Opcao... aguarde')
    sleep(1)
    lista.append(valor)
    soma += valor
    cont += 1
print('\n\033[93mCalculando Valores... aguarde')
sleep(2)
print('\n\033[95mVocê digitou {} númeors e a Média dos valores Digitados é: {:.2f}'.format(cont, sum(lista) / cont))
print('\033[95mMAIOR Valor digitado foi: {}'.format(max(lista)))
print('\033[95mMENOR Valor digitado foi: {}'.format(min(lista)))
