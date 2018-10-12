print('\033[95m********* Calculadora Python **********\n')
def opc():
    print('\n\033[092mEscolha a Opção Desejada \n'
          '[1] Somar\n'
          '[2] Multiplicar\n'
          '[3] MAIOR Valor\n'
          '[4] Novos Valores\n'
          '[5] Sair do Programa')
v1 = float(input('Digite o 1º Valor: ').replace(',', '.'))
v2 = float(input('Digite o 2º Valor: ').replace(',', '.'))
opc()
opcao = int(input('\nDigite a Opção Desejada: '))
while opcao < 1 or opcao > 4:
    print('Opção Inválida!\n'
          'Digite Novamente')
    opcao = int(input('Digite a Opção Desejada: '))
while opcao < 5:
    if opcao == 1:
        print('\n\033[94mVocê escolheu SOMAR:\n'
              'A SOMA de {} + {} = {}'.format(v1, v2, v1 + v2))
    elif opcao == 2:
        print('\n\033[94mVocê escolheu MULTIPLICAR:\n'
              'A MULTIPLICAÇÃO de {} * {} = {}'.format(v1, v2, v1 * v2))
    elif opcao == 3:
        print('\n\033[94mVocê escolheu VERIFICAR O MAIOR:\n')
        if v1 > v2:
            print('O MAIOR valor é: {}'.format(v1))
        elif v2 > v1:
            print('O MAIOR valor é: {}'.format(v2))
        else:
            print('Os valores são IGUAIS.')
    elif opcao == 4:
        print('\n\033[93mVocê escolheu DIGITAR NOVOS VALORES:\n')
        v1 = float(input('Digite o 1º Valor: ').replace(',', '.'))
        v2 = float(input('Digite o 2º Valor: ').replace(',', '.'))
    opc()
    opcao = int(input('\nDigite a Opção Desejada: '))
    if opcao == 5:
        print('\nObrigado por usar o Sistema!')
