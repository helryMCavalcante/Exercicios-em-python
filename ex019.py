import random
aluno1 = str(input('Primeiro aluno(a): '))
aluno2 = str(input('Segundo aluno(a): '))
aluno3 = str(input('Terceiro aluno(a): '))
aluno4 = str(input('Quarto aluno(a): '))
lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.choice(lista)
print('O alundo(a) escolhido foi {}!'.format(sorteio))