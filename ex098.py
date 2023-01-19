from time import sleep
def contador(i,f,p):
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(0.25)
    if p < 0:
        p *= -1
    if p == 0:
        p == 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ',end='')
            sleep(0.25)
            cont += p
        print()
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ',end='')
            sleep(0.25)
            cont -= p
        print()

contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input('Inicio: '))
fim = int(input('Fim'))
passo = int(input('Passo: '))
contador(inicio, fim, passo)

