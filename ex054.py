from datetime import date
maior = 0
menor = 0
for c in range(1,8):
    ano = int(input('Digite o ano de nascimento do {}º usuário: '.format(c)))
    idade = date.today().year - ano
    if idade < 18:
        menor += 1
    else:
        maior += 1
print('Um total de {} pessoas são maiores de idade e um total de {} menores de idade.'.format(maior, menor))

