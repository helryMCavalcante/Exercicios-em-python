pMaior = float(0)
pMenor = float(0)

for c in range(1, 6):
    peso = float(input('Informe o peso da {} pessoa: '.format(c)))
    if c == 1:
        pMaior = peso
        pMenor = peso
    else:
        if peso > pMaior:
            pMaior = peso
        if peso < pMenor:
            pMenor = peso
print('O maior peso é {} e o menor peso é {}'.format(pMaior, pMenor))