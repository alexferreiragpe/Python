from random import randint
print('\n\033[96m********** GAME PAR ou IMPAR ***********\n')
vit,der = 0,0
while vit >= 0:
    ran = randint(1, 10)
    valor = int(input('\033[95mDiga um valor: '))
    opcao = str(input('\033[95mPar ou Ímpar? [P/I]: ').upper())
    soma = valor + ran
    if opcao == 'P' and soma % 2 == 0:
        print('\033[93mVocê ganhou!\nComputador jogou {} \nA soma foi {}'.format(ran, soma))
        vit += 1

    elif opcao == 'I' and soma % 2 != 0:
        print('\033[92mVocê ganhou!\nComputador jogou {} \nA soma foi {}'.format(ran, soma))
        vit += 1

    else:
        print('\033[96mVocê Perdeu!\nComputador jogou {} \nA soma foi {}'.format(ran, soma))
        der += 1
    if (vit-der)==-1:
        print('\n\033[95m********** GAME OVER ***********\n\033[92mResultado: \nComputador: {}\nVocê: {}'.format(der,
                                                                                                                 vit))
        vit=-1


