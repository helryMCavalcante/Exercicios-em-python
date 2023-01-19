def leiaint(msg):
    ok=False
    num = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Número informado é invalido.')
        if ok:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'Você acabou de digita o número {n}.')