salário = float(input('Informe o salário atual do funcionario: '))
if salário <= 1250.00:
    aumento = salário + (salário * 0.15)
    print('O salário de R${:.2f} foi ajustado para o valor de R${:.2f} '.format(salário, aumento))
if salário > 1250.00:
    aumento = salário + (salário * 0.10)
    print('O salário de R${:.2f} foi ajustado para o valor de R${:.2f}'.format(salário, aumento))