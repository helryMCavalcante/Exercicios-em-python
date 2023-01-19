salario = float(input('Infomorme o salário do funcionario: '))
aumento = salario + (salario * 0.15)
print('O salário do empregado atualmente é de {} R$, com o aumento de 15% passará a ser {:.2f} R$'.format(salario,aumento))