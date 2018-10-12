numeros=('zero','hum','dois','tres','quatro','cinco','seis',
         'sete','oito','nove','dez','onze','doze','treze','quatorze',
         'quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
posicao = int(input('\033[91mDigite um valor entre [0:20]: '))

while(posicao<0 or posicao>20):
    posicao = int(input('ERRO! Digite um valor entre [0:20]: '))

for pos,valor in enumerate(numeros):
    if pos==posicao:
        print('\n\033[94mVocê digitou o número {}'.format(valor))