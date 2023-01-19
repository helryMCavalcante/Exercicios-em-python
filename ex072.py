num = ('zero','um', 'dois', 'três', 'quatro',
       'cinco',' seis', 'sete', 'oito', 'nove',
       'dez','onze', 'doze', 'treze', 'quartoze',
       'quinze','dezesseis', ' dezessete', 'dezoito'
       , 'dezenove','vinte')
valor = int(input('Informe um valor de 0 a 20: '))
while True:
    if 0 <= valor <= 20:
        print(f'O valor informado é {valor} e seu nome por extenso é {num[valor]}')
        break
    else:
        print('Valor invalido, ', end=' ')
    valor = int(input('Informe outro valor'))