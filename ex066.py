cont = soma = 0
while True:
    num = int(input('Informe um valor:'))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Você digitou {cont} a soma entre eles é de {soma}')

