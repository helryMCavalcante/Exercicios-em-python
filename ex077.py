palavras = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR')
for p in palavras:
    print(f'\nNa palavra {p} temos as vogais: ', end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(f'\n{letras}', end=' ')
        else:
            print("...", end=" ")