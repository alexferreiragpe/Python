preco=float(input('Digite o Valor: R$ ').replace(',','.'))
print('\nSelecione a Forma de Pagamento:\n'
      '1 - Á vista Dinheiro/Cheque (10% desconto):\n'
      '2 - Á vista no Cartão (5% desconto):\n'
      '3 - Até 2x no Cartão (Preço Normal):\n'
      '4 - 3x ou Mais no Cartão (20% de Juros):\n')
opcao=int(input('Digite a Opção: \033[94m'))

while opcao<1 or opcao>4:
    print('Opção Inválida! Digite Novamente')
    opcao = int(input('Digite a Opção Desejada: '))

if opcao==1:
    print('\nPagamento em Dinheiro/Cheque: R$ {:.2f}'.format(preco-(preco*0.1)))
elif opcao==2:
    print('\nPagamento Á vista no Cartão: R$ {:.2f}'.format(preco-(preco*0.05)))
elif opcao==3:
    print('\nPagamento até 2x no Cartão: R$ {:.2f}'.format(preco))
elif opcao==4:
    print('\nPagamento 3x ou Mais no Cartão: R$ {:.2f}'.format(preco + (preco * 0.2)))
    par=int(input('\nQtd Parcelas: '))
    while par>4:
        print('Parcelamento máximo 4x')
        par = int(input('\nQtd Parcelas: '))
    print('\n')
    print('Valor do Produto: {:.2f}'.format(preco))
    print('Valor da Parcela: {:.2f}'.format((preco + (preco * 0.2))/par))
    print('Total com Juros: {:.2f}'.format((preco + (preco * 0.2))))
    print('Total de Juros: {:.2f}'.format((preco + (preco * 0.2))-preco))


