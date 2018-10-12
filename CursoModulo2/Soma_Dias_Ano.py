from time import sleep

print('\033[1;34m-=-' * 20, '\n        Soma Dias Ano - (365 dias)       \n', '-=-' * 20)
soma=0
ano=0
print('\n\033[1;31mCalculando... Aguarde!\n')
sleep(2)
while ano<366:
    ano=ano+1
    soma=soma+ano
    print(soma)
print('\n\033[1;36mA Soma dos dias de um ano com 365 é: {}'.format(soma))