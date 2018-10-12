Total_Idade = 0
Mulher20 = 0
HomemVelho = 0
NomeHomem = 'Não foi inserido Homem'
for a in range(1, 5):
    print('\n*** {}º Pessoa ***'.format(a))
    nome = (str(input('Digite seu NOME: ').upper()))
    idade = (int(input('Digite sua IDADE: ')))
    sexo = (str(input('Digite o SEXO [F/M]: ').upper()))
    Total_Idade = Total_Idade + idade
    if idade < 20 and sexo == 'F':
        Mulher20 = Mulher20 + 1
    if idade > HomemVelho and sexo == 'M':
        HomemVelho = idade
        NomeHomem = nome
print('\n\033[95mMédia de IDADE do grupo é: \033[96m{} anos'.format(Total_Idade / 4))
print('\033[95mTotal Mulheres com MENOS de 20 anos: \033[96m{}'.format(Mulher20))
print('\033[95mHomem mais Velho é o:\033[96m {} com {} anos'.format(NomeHomem, HomemVelho))
