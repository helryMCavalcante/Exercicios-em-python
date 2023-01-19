soma = 0
for cont in range(1,7):
    n = int(input('Informe o {}º valor: '.format(cont)))
    if n % 2 == 0:
        soma += n
print('A soma dos número pares é {}'.format(soma))

