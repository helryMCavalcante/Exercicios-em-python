saldo = saque = option = totcedula = totsaque = 0
cedula = 50
option = int(input('Que operação você deseja fazer [1. Deposito / 2. Saque]: '))
while True:
    if option == 1:
        valor = int(input('Informe o valor a ser depositado: '))
        saldo += valor
        print(f'Saldo atual: {saldo}')
    if option == 2:
        saque = int(input('Informe o valor para saque: '))
        saldo -= saque
        totsaque = saque

        while True:
            if totsaque >= cedula:
                totsaque -= cedula
                totcedula += 1
            else:
                if totcedula > 0:
                    print(f'Total de {totcedula} cedulas de R${cedula}')
                if cedula == 50:
                    cedula = 20
                elif cedula == 20:
                    cedula = 10
                elif cedula == 10:
                    cedula = 1
                totcedula = 0
                if totsaque == 0:
                    break
            print(f'Saldo atual: {saldo}')
    option = int(input('Deseja realizar mais alguma operação? [ 0. Encerrar / 1. Despositar / 2. Sacar'))
    if option == 0:
        break







