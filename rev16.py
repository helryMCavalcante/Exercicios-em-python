from datetime import date
totmaior = 0
totmenor = 0
for c in range(1,8):
    ano = int(input(f'Informe o ano de nascimento da {c}º pessoa: '))
    idade = date.today().year - ano
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1

print(f'O tatol de pessoas com idade maior ou igual a 18 anos são de {totmaior}')
print(f'O total de pessoas com idade menor que 18 são de {totmenor}')