d = int(input('Informe o número de dias: '))
km = int(input('Informe o número de KM rodados: '))
total = (d * 60) + (km * 0.15)
print('Total a pagar é de R$ {:.2f}'.format(total))