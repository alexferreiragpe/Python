from time import sleep

print('\033[1;34m-=-' * 20, '\n        Empréstimo de Financeio - Imóvel        \n', '-=-' * 20)
valor = float(input('\033[1;33m\nQual o valor da Casa? R$ '))
salario = float(input('\033[1;33mQual o salário? R$ '))
anos = float(input('\033[1;33mQuantos anos para pagar? R$ '))
print('\033[1;35m\nProcessando os dados... aguarde\n')
sleep(2)
prestacao = valor / (anos * 12)
if prestacao > (salario * 0.3):
    print('\033[1;31mReprovado!\nPrestação de R$ {:.2f}\nAcima do valor permitido para o salário R$ {:.2f}'.format(
        prestacao, salario))
else:
    print('\033[1;34mEmpréstimo Aprovado!\nTotal Parcelas: {:.0f}\nValor da Prestação: R$ {:.2f}'.format((anos*12),prestacao))
