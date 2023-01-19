from time import sleep

produto = float(input('Informe o valor do produto: R$'))

print('''[1] Dinheiro / cheque.
[2] cartão à vista.
[3] cartão parcelado.''')
opção = int(input('Selecione a opção: '))
sleep(2)

if opção == 1:
    desconto = produto - (produto * 0.10)
    print('O produto no valor de R${:.2f} pago a dinheiro / cheque, receberá 10% de desconto ficando no valor de R${:.2f}.'.format(produto, desconto))
elif opção == 2:
    desconto = produto - (produto * 0.05)
    print('O produto no valor de R${:.2f} pago no cartão a vista, receberá 5% de desconto, ficando no valode de R${:.2f}'.format(produto, desconto))
elif opção == 3:
    parcelas = int(input('informa o número de parcelas: '))
    if parcelas == 2:
        divParcelas = produto / 2
        print('O produto no valor de R${:.2f} parcelado em 2x sem juros, ficará com a parcela de RS{:.2f}.'.format(produto, divParcelas))
    elif parcelas >= 3:
        divParcelas = (produto + (produto * 0.20)) / parcelas
        print('O produto no valor de R${:.2f} parcelado em {}, terá o juros de 20%, a parcela ficará no valor R${:.2f}'.format(produto, parcelas, divParcelas))
else:
    print('Opção inválida! escolhas umas das opções acima!')