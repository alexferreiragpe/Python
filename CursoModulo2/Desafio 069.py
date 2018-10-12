print('\n\033[96m********** Análise de Dados ***********\n\n>>> Cadastre uma Pessoa <<<\n')
opc='S'
maior,f,m=0,0,0
while opc=='S':
    idade = int(input('\033[94m\nDigite sua Idade: '))
    sexo = str(input('Digite seu Sexo[M/F]: ').upper())
    while sexo not in ('MF'):
        sexo = str(input('\033[92mDigite seu Sexo CORRETAMENTE BURRO: ').upper())
    if idade>=18:
        maior+=1
    if sexo=='M':
        m+=1
    if sexo=='F'and idade<20:
        f+=1
    opc=str(input('\033[95mDeseja Continuar? [S/N]: ').upper())
print('\n\033[96mPessoas maiores de 18 anos: {}'.format(maior))
print('Homens cadastrados: {}'.format(m))
print('Mulheres com menos de 20 anos: {}'.format(f))