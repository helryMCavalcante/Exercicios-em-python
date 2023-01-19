vCasa = float(input('Valor da casa: R$'))
salComprador = float(input('Informe o salário do comprador: R$'))
anosFinan = int(input('Quantos anos de financiamento?'))
prestação = vCasa / (anosFinan * 12)
minimo = salComprador * 0.30

if prestação <= minimo:
    print('Empresimo concedido')
else:
    print('Emprestimo negado')
