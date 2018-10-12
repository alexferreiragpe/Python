from time import sleep

print('\033[1;34m-=-' * 20, '\n        Conversão de Base Binária (Decimal)       \n', '-=-' * 20)
repete = 'S'
while (repete == 'S'):
    valor = int(input('\033[1;33m\nDigite o Valor desejado para conversão: ').replace(',', ''))
    valor1 = valor
    base = int(input('\033[1;34m\nInforme a Base desejada: \033[1;33m1-Binário 2-Octal 3-Hexadecimal: '))
    while base < 1 or base > 3:
        print('\033[1;36m\nOpção Inválida! Digite Novamente.')
        base = int(input('\033[1;34m\nInforme a Base Desejada: \033[1;33m1-Binário 2-Octal 3-Hexadecimal: '))
    lista = []
    print('\n\033[1;31mRealizando a conversão... Aguarde!\n')
    sleep(2)
    print('\033[1;37mValores do Cálculo:\n')
    if base == 1:
        while valor % 2 < valor or valor == 1:
            lista.append(int(valor % 2))
            print('\033[1;32m{:.0f}'.format(valor))
            valor = int(valor / 2)
        lista.reverse()
        ListaFormatada = ''.join(str(e) for e in lista)
        print('\n\033[1;34m{:.0f} em Binário é: \033[1;33m{}'.format(valor1, str(ListaFormatada)))
    elif base == 2:
        while valor % 8 <= valor and valor > 0:
            lista.append(int(valor % 8))
            print('\033[1;32m{:.0f}'.format(valor))
            valor = int(valor / 8)
        lista.reverse()
        ListaFormatada = ''.join(str(e) for e in lista)
        print('\n\033[1;34m{:.0f} em Octal é: \033[1;33m{}'.format(valor1, str(ListaFormatada)))
    elif base == 3:
        hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
        r = []
        while valor > 0:
            r.append(hex[(valor % 16)])
            print('\033[1;32m{:.0f}'.format(int(valor / 16)))
            valor = valor // 16
        r.reverse()
        ListaFormatada = ''.join(str(e) for e in r)
        print('\n\033[1;34m{:.0f} em Hexadecimal é: \033[1;33m{}'.format(valor1, ListaFormatada, end=""))
    repete = str(input('\n\033[1;34mDeseja realizar outra Conversão: \033[1;33mS--> Sim   N--> Não : ').upper())
