num = int(input('Informe um valor: '))
cont = soma = 0
while num != 999:
    soma += num
    num = int(input('Informe um valor: '))
    cont += 1
print('Você digitou {} números e a soma entre eles é de {}'.format(cont,soma))