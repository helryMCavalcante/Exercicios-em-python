cont = soma = maior = menor = 0
opção = 'S'
while opção in 'S':
    num = int(input('Informe um valor:'))
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opção = str(input('Quer continuar? [S / N]')).strip().upper()[0]
    soma += num
    cont += 1
print('Você digitou {} numeros e a media deles é {:.2f}'.format(cont, soma / cont))
print(f'{maior} maior, {menor} menor')




