from time import sleep
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
opção = 0
while opção != 5:
    print(''' ---Opções---
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opção = int(input('Qual sua opção: '))
    if opção == 1:
        soma = n1 + n2
        print('A soma dos valores é: {}'.format(soma))
        sleep(1)
    elif opção == 2:
        mult = n1 * n2
        print('A multiplicação dos valores é {}'.format(mult))
        sleep(1)
    elif opção == 3:
        if n1 > n2:
            maior = n1
            print('O número {} é maior que {}'.format(n1, n2))
            sleep(1)
        else:
            maior = n2
            print('O numero {} é maior que {}'. format(n2, n1))
            sleep(1)
    elif opção == 4:
        n1 = int(input('Informe o primeiro número: '))
        n2 = int(input('Informe o segundo número: '))
    elif opção == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção invalida, tente novamente!')
        sleep(1)
print('-=-'*10,'Programa finalizado, volte sempre!', '-=-'*10)

