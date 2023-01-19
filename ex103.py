def ficha(jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')

jogador = str(input('Nome do jogador: '))
Ngols = str(input('Número de gols: '))
if Ngols.isnumeric():
    Ngols = int(Ngols)
else:
    Ngols = 0
if jogador.strip() == '':
    ficha(gols=Ngols)
else:
    ficha(jogador, Ngols)