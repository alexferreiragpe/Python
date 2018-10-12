import random
from time import sleep

print('\033[1;34m-=-' * 20, '\n        Jokenpô        \n', '-=-' * 20)
verifica = 'S'
posicoes = ['Pedra', 'Tesoura', 'Papel']
contPc = 0
contEu = 0
while verifica == 'S':
    computador = random.choice(posicoes)
    print('\nVamos começar!')
    print('\n\033[1;35mComputador: Estou pensando, espere!')
    sleep(2)
    print('\033[1;35mComputador: Pronto! Já tenho minha escolha, agora é você')
    while True:
        try:
            minhaescolha = int(
                input('\n\033[1;33mFaça sua escolha: \033[1;34m1- Pedra 2- Tesoura 3- Papel:  \033[1;31m'))
            if minhaescolha < 1 or minhaescolha > 3:
                raise ValueError('Valor Inválido')
        except ValueError as e:
            print('Escolha Inválida! Digite Novamente.')
        else:
            break
    if minhaescolha == 1:
        minhaescolha = 'Pedra'
    elif minhaescolha == 2:
        minhaescolha = 'Tesoura'
    elif minhaescolha == 3:
        minhaescolha = 'Papel'
    sleep(2)
    if minhaescolha == 'Pedra' and computador == 'Tesoura':
        print('\nVocê Ganhou! \n\n\033[1;35mComputador: {} \n\033[1;33mVocê:       {}'.format(computador, minhaescolha))
        contEu = contEu + 1
    elif minhaescolha == 'Tesoura' and computador == 'Papel':
        print('\nVocê Ganhou! \n\n\033[1;35mComputador: {} \n\033[1;33mVocê:       {}'.format(computador, minhaescolha))
        contEu = contEu + 1
    elif minhaescolha == 'Papel' and computador == 'Pedra':
        print('\nVocê Ganhou! \n\n\033[1;35mComputador: {} \n\033[1;33mVocê:       {}'.format(computador, minhaescolha))
        contEu = contEu + 1
    elif computador == minhaescolha:
        print('\nCaramba... \nEmpatamos! \n\n\033[1;35mComputador: {} \n\033[1;33mVocê:       {}'.format(computador,
                                                                                                         minhaescolha))
    else:
        print('\nEu venci... Sou um Computador experto! \n\n\033[1;35mComputador: {} \n\033[1;33mVocê:       {}'.format(
            computador, minhaescolha))
        contPc = contPc + 1
    computador = ''
    minhaescolha = ''
    print('\n\033[1;34mParciais\n\033[1;35mComputador: {}\n\033[1;33mVocê:       {}\n'.format(contPc, contEu))
    print('\033[1;34m-=-' * 20, '\n        Jokenpô        \n', '-=-' * 20)
    verifica = str(input('\n\033[1;34mDeseja Jogar Novamente? \033[1;33mS--> Sim  N--> Não : ').upper())
