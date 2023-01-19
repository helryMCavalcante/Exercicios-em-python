def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a}m².')
print('Controle de terrenos')
print('-' * 20)
l = float(input('Largura: '))
c = float(input('Comprimento: '))
área(l,c)