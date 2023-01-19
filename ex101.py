def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade > 65:
        return f'Com {idade} anos, o voto é OPCIONAL.'
    elif idade < 65 and idade >= 16:
        return f'Com {idade} anos, o voto é OBRIGATORIO.'
    else:
         return f'Com {idade} anos, o voto é NEGADO.'


ano = int(input('Informe o ano de nascimento: '))
print(voto(ano))



