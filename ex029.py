veloc = int(input('Qual a velocidade atual do carro? '))
if veloc > 80:
    print('Você excedeu o limite de velocidade da via atigindo {}km'.format(veloc))
    print('O valor da multa será de R${:.2f}'.format(float (veloc-80)*7))
else:
    print('Veiculo dentro dos limites permitidos de velocidade!')
