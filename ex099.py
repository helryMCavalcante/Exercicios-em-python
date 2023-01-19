from time import sleep
def maior(*valor):
    cont = 0
    print('-=' * 20)
    print('Analisando valores')
    if cont > 1:
        while cont < len(valor):
            cont += 1
    for v in valor:
        print(f'{v} ', end='')
        sleep(0.5)
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi o número {max(valor)}')

maior(0, 0, 0)
maior(7, 60, 10, 25)
maior(7, 6, 0)
maior(5, 8, 36)
maior(12, 24, 69, 51, 45)
maior(0, 0, 0)
